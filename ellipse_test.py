import numpy as np
import matplotlib.pyplot as plt
from ellipseunc import fit

# import test ellipse data
data = np.genfromtxt('test_data.txt')

# performing fit
center, a, b, phi = fit(data[:,0],data[:,1])
print(center, a, b, phi)

# fit ellipse
t = np.linspace(0,2*np.pi,100)
xx = center[0].n+a.n*np.cos(t)*np.cos(phi.n)-b.n*np.sin(t)*np.sin(phi.n)
yy = center[1].n+a.n*np.cos(t)*np.sin(phi.n)+b.n*np.sin(t)*np.cos(phi.n)

# plotting
fig,ax = plt.subplots()
ax.plot(data[:,0],data[:,1],'xr',label='Data')
ax.plot(xx,yy,'--b',lw=1,label='Fit')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_aspect('equal')
plt.savefig('Output.png')
plt.show()
