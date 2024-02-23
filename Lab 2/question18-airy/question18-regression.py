# import packages
import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# define independent variable x, 1/d with d in inches
d = [14, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5, 0.25]
x = np.reciprocal(d)
# print(x)

# define dependent variable, the angular diameter of airy disk in arcseconds
y = [2.03, 2.35, 5.20, 3.82, 5.12, 3.57, 5.77, 5.93, 8.44, 16.40, 38.57]
# print(y1)

# define error bars
yerr = [0.81, 0.44, 2.30, 1.39, 1.10, 0.6, 2.57, 0.46, 0.67, 0.84, 2.03]

# scatter data points
# plt.scatter(x, y, label='Airy disk data')
plt.errorbar(x, y, yerr, fmt='o', label='Airy disk data')

# define x and y coordinates for airy disk points
d_airy = [1.5, 1, 0.5, 0.25]
x_airy = np.reciprocal(d_airy)
y_airy = [6.44, 11, 23.4, 57]
y_airy_err = [2.09, 1.00, 2.07, 3.61]
# plt.scatter(x_airy, y_airy, label='Airy ring data', marker='*')
plt.errorbar(x_airy, y_airy, fmt='*', label='Airy ring data')

# define function for ordinary least squares regression, y = mx + b form
def linear_function(x, m, b):
    return m * x + b


# chart title, labels, legend
plt.title('Airy Diameter as a Function of Inverse Objective Diameter')
plt.xlabel('Inverse Objective Diameter, 1/d (d in inches)')
plt.ylabel('Angular Size, $\\theta$ (arcseconds)')
plt.legend()

# show plot
plt.show()
