import numpy as np
from uncertainties import ufloat,umath
from matplotlib.patches import Ellipse

def generate(a,b,center=(0,0),n=100,phi=0,weight=0.2):
    t = np.linspace(0,2*np.pi,n)[:-1]
    x = a*np.cos(t)*np.cos(phi) - b*np.sin(t)*np.sin(phi) + center[0]
    y = a*np.cos(t)*np.sin(phi) + b*np.sin(t)*np.cos(phi) + center[1]
    x += np.random.randn(len(t))*weight
    y += np.random.randn(len(t))*weight
    return x,y

def fit(x,y):
    D1 = np.vstack([x**2,x*y,y**2]).T
    D2 = np.vstack([x,y,np.ones_like(x)]).T
    S1,S2,S3 = D1.T @ D1, D1.T @ D2, D2.T @ D2
    C1 = np.array([[0,0,2],[0,-1,0],[2,0,0]])
    M = np.linalg.inv(C1) @ (S1 - S2 @ np.linalg.inv(S3) @ S2.T)
    vec = np.linalg.eig(M)[1]
    cond = 4*(vec[0]*vec[2]) - vec[1]**2
    a1 = vec[:,np.nonzero(cond > 0)[0]]
    return np.vstack([a1,np.linalg.inv(-S3) @ S2.T @ a1]).flatten()

def errors(x,y,coeffs):
    z = np.vstack((x**2,x*y,y**2,x,y,np.ones_like(x)))
    numerator = np.sum(((coeffs @ z)-1)**2)
    denominator = (len(x)-6)*np.sum(z**2,axis=1)
    unc = np.sqrt(numerator/denominator)
    return tuple(ufloat(i,j) for i,j in zip(coeffs,unc))

def convert(coeffs):
    a,b,c,d,e,f = coeffs
    b /= 2
    d /= 2
    e /= 2
    x0 = (c*d - b*e) / (b**2 - a*c)
    y0 = (a*e - b*d) / (b**2 - a*c)
    center = (x0, y0)
    numerator = 2 * (a*e**2 + c*d**2 + f*b**2 - 2*b*d*e - a*c*f)
    denominator1 = (b*b-a*c)*((c-a)*umath.sqrt(1+4*b*b/((a-c)*(a-c)))-(c+a))
    denominator2 = (b*b-a*c)*((a-c)*umath.sqrt(1+4*b*b/((a-c)*(a-c)))-(c+a))
    major = umath.sqrt(numerator/denominator1) if numerator/denominator1 > 0 else 0
    minor = umath.sqrt(numerator/denominator2) if numerator/denominator2 > 0 else 0
    phi = .5*umath.atan((2*b)/(a-c))
    major, minor, phi = (major, minor, phi) if major > minor else (minor, major, np.pi/2+phi)
    return center, major, minor, phi

def line(coeffs,n=100):
    t = np.linspace(0,2*np.pi,n)
    center,major,minor,phi = convert(coeffs)
    x = major*np.cos(t)*np.cos(phi) - minor*np.sin(t)*np.sin(phi) + center[0]
    y = major*np.cos(t)*np.sin(phi) + minor*np.sin(t)*np.cos(phi) + center[1]
    return x,y

def artist(coeffs,*args,**kwargs):
    center,major,minor,phi = convert(coeffs)
    return Ellipse(xy=(center[0],center[1]),width=2*major,height=2*minor,
                     angle=np.rad2deg(phi),*args,**kwargs)

def confidence_area(x,y,coeffs,f=1):
    c = coeffs
    res = c[0]*x**2 + c[1]*x*y + c[2]*y**2 + c[3]*x + c[4]*y + c[5]
    c_up = np.array([c[0],c[1],c[2],c[3],c[4],c[5] + f*np.std(res)])
    c_do = np.array([c[0],c[1],c[2],c[3],c[4],c[5] - f*np.std(res)])
    if convert(c_do) > convert(c_up):
        c_do, c_up = c_up,c_do
    return c_up,c_do

class ellipse_fit:
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.c = fit(x,y)
        self.coeffs = errors(self.x,self.y,self.c)
        self.params = convert(self.coeffs)
        self.p = ((self.params[0][0].n,self.params[0][1].n),
                    self.params[1].n,self.params[2].n,self.params[3].n)
        
    def confidence_area(self,f):
        return confidence_area(self.x,self.y,self.c,f)