# import packages
import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# define independent variable m_lim, defined as the Gaia magnitude of asterism stars, provided in lab assignment
# m_lim = [5.41, 7.00, 7.91, 8.94, 9.81, 10.63, 11.63, 12.88]
m_lim = [5.41, 7.00, 7.91, 8.94, 9.81, 10.63, 11.63]  # exclude 12.88 because H star was not visible on baseline 14-inch

# define dependent variable d, the smallest aperture diameter through which each star could be seen
d = [0.67, 1.5, 2, 3.5, 4, 14, 14]
# convert to logspace
log_d = np.log(d)
print(log_d)

# create scatter plot
'''
plt.scatter(m_lim, log_d)
plt.show()
'''


# define function for ordinary least squares regression, y = mx + b form
def linear_function(x, m, b):
    return m * x + b


# fit curve, extract beta coefficients for ordinary least squares regression
popt, pcov = curve_fit(linear_function, m_lim, log_d)
m, b = popt

# plot scatter plot
plt.scatter(m_lim, log_d, label='Data')

# plot OLS fit line
x_regression = np.linspace(min(m_lim), max(m_lim), 100)
y_regression = linear_function(x_regression, m, b)
# programmatically define string for fit line label
line_label = 'Fit line: log(d) = ' + str(round(m, 2)) + '$\mathregular{m_{lim}}$ + ' + str(round(b, 2))
plt.plot(x_regression, y_regression, color='orange', label=line_label)

# chart title, labels, legend
plt.title('Logarithm of Aperture Diameter as a Function of Limiting Magnitude')
plt.xlabel('Limiting Magnitude, $\mathregular{m_{lim}}$')
plt.ylabel('Logarithm of Aperture Diameter, log(d)')
plt.legend()

# show plot
plt.show()
