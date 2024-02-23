# import packages
import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# define independent variable m_lim, defined as the Gaia magnitude of asterism stars, provided in lab assignment
m_lim = [5.41, 7.00, 7.91, 8.94, 9.81, 10.63, 11.63, 12.88]

# define dependent variable t, the shortest exposure time before loss of visibility
t = [20, 30, 50, 200, 900, 2000, 5000, 12000]
# convert to logspace
log_t = np.log(t)
# print(log_t)

# scatter data points
plt.scatter(m_lim, log_t, label='Data')


# define function for ordinary least squares regression, y = mx + b form
def linear_function(x, m, b):
    return m * x + b


# fit curve, extract beta coefficients for ordinary least squares regression
popt, pcov = curve_fit(linear_function, m_lim, log_t)
m, b = popt

# plot OLS fit line
x_regression = np.linspace(min(m_lim), max(m_lim), 100)
y_regression = linear_function(x_regression, m, b)
# programmatically define string for fit line label
line_label = 'Fit line: log(t) = ' + str(round(m, 2)) + '$\mathregular{m_{lim}}$ + ' + str(round(b, 2))
plt.plot(x_regression, y_regression, color='orange', label=line_label)

# chart title, labels, legend
plt.title('Log-Integration Time as a Function of Limiting Magnitude')
plt.xlabel('Limiting Magnitude, $\mathregular{m_{lim}}$')
plt.ylabel('Logarithm of Aperture Diameter, log(t)')
plt.legend()

# show plot
plt.show()
