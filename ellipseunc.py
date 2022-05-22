import numpy as np
import ellipse as el
from uncertainties import ufloat,umath
import matplotlib.pyplot as plt

def fit(x,y):
    fit = el.LsqEllipse().fit(np.vstack([x,y]).T).coefficients
    m = len(x)
    z = np.array([x**2,x*y,y**2,x,y,np.ones(m)])
    numerator = np.sum(((fit @ z)-1)**2)
    denominator = (m-6)*np.sum(z**2,axis=1)
    unc = np.sqrt(numerator/denominator)
    a,b,c,d,f,g = [ufloat(i,j) for i,j in zip(fit,unc)]
    b /= 2
    d /= 2
    f /= 2
    x0 = (c*d - b*f) / (b**2. - a*c)
    y0 = (a*f - b*d) / (b**2. - a*c)
    center = (x0, y0)
    numerator = 2 * (a*f**2 + c*d**2 + g*b**2 - 2*b*d*f - a*c*g)
    denominator1 = (b*b-a*c)*((c-a)*umath.sqrt(1+4*b*b/((a-c)*(a-c)))-(c+a))
    denominator2 = (b*b-a*c)*((a-c)*umath.sqrt(1+4*b*b/((a-c)*(a-c)))-(c+a))
    width = umath.sqrt(numerator/denominator1)
    height = umath.sqrt(numerator/denominator2)    
    phi = .5*umath.atan((2*b)/(a-c))
    if width > height:
        return center, width, height, phi
    else:
        return center, height, width, np.pi/2+phi