# import packages
import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# define dependent variable 1/cos(dec)
dec_deg = [4.0897, 45.9981, 60.2353, 77.6322]  # degree values obtained by converting sexagesimal values to decimal
dec_rad = np.deg2rad(dec_deg)  # convert degree values to radians, which np.cos() requires the input to be in
print(dec_rad)
cos_dec = np.cos(dec_rad)  # define cosine of declinations

# create array for x-axis values and append value using for-loop
x = []
for i in range(len(cos_dec)):
    x.append(1 / cos_dec[i])

# define array for mean transit time values for y-axis as calculated using Google Sheets,
#   and enumerated in Table 3 of lab report
y = [68.48, 99.31, 141.50, 323.50]

# create scatter plot
# plt.scatter(x, y)
# plt.show()

# define error bars, also calculated in-spreadsheet
y_error = [0.21, 0.92, 0.21, 0.48]


# define function for ordinary least squares regression, y = mx + b form
def linear_function(x, m, b):
    return m * x + b


# fit curve, extract beta coefficients for ordinary least squares regression
popt, pcov = curve_fit(linear_function, x, y)
m, b = popt

# plot scatter plot
plt.errorbar(x, y, yerr=y_error, fmt='o', capsize=5, label='data')

# plot OLS fit line
x_regression = np.linspace(min(x), max(x), 100)
y_regression = linear_function(x_regression, m, b)
# programmatically define string for fit line label
line_label = 'Fit line: t = ' + str(round(m, 2)) + 'x + ' + str(round(b, 2))
plt.plot(x_regression, y_regression, color='orange', label=line_label)

# chart title, labels, legend
plt.title('Mean Transit Time as a Function of 1/cos(Dec)')
plt.xlabel('1/cos(Dec), x (scalar)')
plt.ylabel('Mean Transit Time, t (seconds)')
plt.legend()

# show plot
plt.show()
