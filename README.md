# Estimation of Errors in Ellipse Fitting

Ellipse fitting with parameter uncertainties, meant for bowshock maser fitting

## Process
* Ellipse fitting on 2D data using [`lsq-ellipse`](https://pypi.org/project/lsq-ellipse/)
* Estimates the error using the $\chi^2$ distribution based on [McDonald, 2014](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=W9iFjWQAAAAJ&cstart=400&pagesize=100&citation_for_view=W9iFjWQAAAAJ:SgM-ki2adj0C)
* Convert the fitting coefficients into physical ellipse paramters while propagating errors using [`uncertainties`](https://pythonhosted.org/uncertainties/)

## Related publication

The code was developed for (To be added).

## Usage

Add the ellipseunc.py in the working directory and import in the Python code using 

```python
from ellipseunc import fit
``` 

To perform the fitting, execute the function

```python
fit(x,y)
``` 

where `x` and `y` are the x- and y-coordinates of the input data. The function will return a 4-tuple consisting of 
* Center coordinates (a 2-tuple of the x- and y-coordinate of the center of the ellipse)
* Semi major axis of the ellipse
* Semi minor axis of the ellipse
* Rotation angle in radians counter-clockwise w.r.t. to the horizontal axis

## Example

To test the fitting, utilize `test_data.txt` as an input,

```python
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
```

### Parameters obtained: 

Center, ($-1.26 \pm 0.06$, $0.74 \pm 0.05$)  
Semi major axis, $4.97 \pm 0.08$  
Semi minor axis, $3.13 \pm 0.04$  
Rotation angle of $(-0.420 \pm 0.016)$ rad.


### Output plot:
![fitting output](https://github.com/affanadly/Ellipse-Fit-Uncertainty/blob/main/Output.png)

## References
* Hammel, B., & Sullivan-Molina, N. (2020). bdhammel/least-squares-ellipse-fitting: v2.0.0 (v2.0.0) (Computer software). Zenodo. https://doi.org/10.5281/ZENODO.3723294
* McDonald, K. T. (2014). Error Estimation in Fitting of Ellipses (Lab note). https://scholar.google.com/citations?view_op=view_citation&hl=en&user=W9iFjWQAAAAJ&cstart=400&pagesize=100&citation_for_view=W9iFjWQAAAAJ:SgM-ki2adj0C
* do Couto, F. M., & da Silva, J. F. (2021). Uso do Módulo Python Uncertainties no cálculo de incertezas experimentais da diferença de potencial e corrente elétrica de um protótipo experimental. In Revista Brasileira de Ensino de Física (Vol. 43). FapUNIFESP (SciELO). https://doi.org/10.1590/1806-9126-rbef-2020-0415
