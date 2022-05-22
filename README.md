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

```from ellipseunc import fit```. 

To perform the fitting, execute the function

```fit(x,y)``` 

where `x` and `y` are the x- and y-coordinates of the input data. The function will return a 4-tuple consisting of 
* Center coordinates (a 2-tuple of the x- and y-coordinate of the center of the ellipse)
* Semi major axis of the ellipse
* Semi minor axis of the ellipse
* Rotation angle in radians counter-clockwise w.r.t. to the horizontal axis

## Example

(To be added)

## References

(To be added) 
