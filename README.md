# Ellipse Fitting with Errors and Confidence Region

Python library for fitting a 2D ellipse data, estimate the errors for the physical ellipse parameters, and calculate the confidence interval/area. This library was developed for the analysis of VLBI bowshock maser data in tracking a protostellar bowshock.

## Process
1. Ellipse fitting using numerically stable direct least squares based on Fitzgibbon, Pilu, & Fisher, 1996 and Halir & Flusser, 1998.
2. Estimation of errors by minimizing the $\chi^2$ function based on McDonald, 2014.
3. Converting the fit parameters to the usual ellipse parameters while propagating the error using the `uncertainties` package. 
4. Calculation of confidence interval/area using the two-norm distance approximation with a Gaussianly-distributed residuals based on O'Leary & Zsombor-Murray, 2004.

Other convienence functions:
* Generating an ellipse with noise
* Generating coordinates of the ellipse based on fit parameters
* Generating a `matplotlib` Ellipse patch based on fit parameters

## Related publication

The code was developed for (To be added).

## Usage

Add the ellipseunc.py in the working directory and import in the Python code using 

```python
from ellipseunc import *
``` 

For detailed descriptions of the functions, refer to the `derivation.ipynb`.

## References
* Fitzgibbon, A., Pilu, M., & Fisher, R. B. (1996). Direct least square fitting of ellipses. IEEE Transactions on Pattern Analysis and Machine Intelligence, 21(5), 476–480). https://doi.org/10.1109/34.765658
* Halir, R., & Flusser, J. (1998). Numerically stable direct least squares fitting of ellipses. Retrieved from https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.1.7559
* Hammel, B., & Sullivan-Molina, N. (2020). bdhammel/least-squares-ellipse-fitting (v2.0.0) [Computer software]. https://doi.org/10.5281/ZENODO.3723294
* McDonald, K. T. (2014). Error Estimation in Fitting of Ellipses [Lab note]. https://scholar.google.com/citations?view_op=view_citation&hl=en&user=W9iFjWQAAAAJ&cstart=400&pagesize=100&citation_for_view=W9iFjWQAAAAJ:SgM-ki2adj0C
* Lebigot, E. O. (2019). Uncertainties: a Python package for calculations with uncertainties (v3.0.3) [Computer software]. Retrieved from http://pythonhosted.org/uncertainties/
* O'Leary, P. L., & Zsombor-Murray, P. J. (2004). Direct and specific least-square fitting of hyperbolæ and ellipses. Journal of Electronic Imaging, 13 (3), 492 - 503. https://doi.org/10.1117/1.1758951
