# import packages
import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# define independent variable x, 1/d with d in inches
# d = [14, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5, 0.25]
d = [14, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1]
d_outliers = [0.5, 0.25]
x = np.reciprocal(d)
x_outliers = np.reciprocal(d_outliers)
# print(x)

# define dependent variable, the angular diameter of airy disk in arcseconds
# y = [2.03, 2.35, 5.20, 3.82, 5.12, 3.57, 5.77, 5.93, 8.44, 16.40, 38.57]
y = [2.03, 2.35, 5.20, 3.82, 5.12, 3.57, 5.77, 5.93, 8.44]
y_outliers = [16.40, 38.57]

# define error bars
yerr = [0.81, 0.44, 2.30, 1.39, 1.10, 0.6, 2.57, 0.46, 0.67]
y_outliers_err = [0.84, 2.03]

# scatter data points
# plt.scatter(x, y, label='Airy disk data')
# plt.scatter(x_outliers, y_outliers, label='Outlier airy disk data', color='red')
plt.errorbar(x, y, yerr, fmt='o', label='Airy disk data')
plt.errorbar(x_outliers, y_outliers, y_outliers_err, fmt='o', color='red', label='Outlier airy disk data')

# define x and y coordinates for airy disk points
# d_airy = [1.5, 1, 0.5, 0.25]
d_airy = [1.5, 1]
x_airy = np.reciprocal(d_airy)
# y_airy = [6.44, 11, 23.4, 57]
y_airy = [6.44, 11]
y_airy_err = [2.09, 1.00]
y_airy_outliers = [23.4, 57]
y_airy_outliers_err = [2.07, 3.61]
# plt.scatter(x_airy, y_airy, label='Airy ring data', marker='*')
# plt.scatter(x_outliers, y_airy_outliers, label='Outlier Airy ring data', marker='*', color='red')
plt.errorbar(x_airy, y_airy, y_airy_err, fmt='*', label="Airy ring data")
plt.errorbar(x_outliers, y_airy_outliers, y_airy_outliers_err, label='Outlier Airy ring data', fmt='*', color='red')

# define function for ordinary least squares regression, y = mx + b form
def linear_function(x, m, b):
    return m * x + b


# fit curve, extract beta coefficients for ordinary least squares regression
popt, pcov = curve_fit(linear_function, x, y)
m, b = popt

# plot OLS fit line
x_regression = np.linspace(min(x), 4, 100)
y_regression = linear_function(x_regression, m, b)
# programmatically define string for fit line label
line_label = 'Airy Disk Fit line: $\\theta$ = ' + str(round(m, 2)) + '(1/d) + ' + str(round(b, 2))
plt.plot(x_regression, y_regression, color='orange', label=line_label)

# Compute OLS for airy ring
popt, pcov = curve_fit(linear_function, x_airy, y_airy)
m_airy, b_airy = popt
x_airy_reg = np.linspace(min(x_airy), 4, 100)
y_airy_reg = linear_function(x_airy_reg, m_airy, b_airy)
line_label = 'Airy Ring Fit line: $\\theta$ = ' + str(round(m_airy, 2)) + '(1/d) + ' + str(round(b_airy, 2))
plt.plot(x_airy_reg, y_airy_reg, color='orange', label=line_label, ls='--')

# chart title, labels, legend
plt.title('Airy Diameter as a Function of Inverse Objective Diameter')
plt.xlabel('Inverse Objective Diameter, 1/d (d in inches)')
plt.ylabel('Airy Diameter, $\\theta$ (arcseconds)')
plt.legend()

# show plot
plt.show()
