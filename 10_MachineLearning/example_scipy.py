# The optimization package in SciPy allows us to solve minimization problems easily and
# quickly. But wait: what is minimization and how can it help you with your work? Some
# classic examples are performing linear regression, finding a function’s minimum and
# maximum values, determining the root of a function, and finding where two functions
# intersect. Below we begin with a simple linear regression and then expand it to fitting
# non-linear data.

# There are several ways to fit data with a linear regression. In this section we will use
# curve_fit, which is a χ2-based method (in other words, a best-fit method). In the
# example below, we generate data from a known function with noise, and then fit the
# noisy data with curve_fit. The function we will model in the example is a simple linear
# equation, f (x) = ax + b.
import numpy as np
from scipy.optimize import curve_fit
# Creating a function to model and create data
def func(x, a, b):
   return a * x + b
# Generating clean data
x = np.linspace(0, 10, 100)
y = func(x, 1, 2)
# Adding noise to the data
yn = y + 0.9 * np.random.normal(size=len(x))
# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, yn)
# popt returns the best fit values for parameters of
# the given model (func).
print(popt)