# Use a polynomial function to detrend a time series
from pandas import read_csv
from matplotlib import pyplot
from numpy import polyfit

series = read_csv('shampoo-sales.csv', header=0, index_col=0, parse_dates=True)
series.squeeze('columns')

# Fit polynomial: x^2*b1 + x*b2 + ... + bn
X = [i % 365 for i in range(0, len(series))]
y = series.values
degree = 2
coef = polyfit(X, y, degree)
print(coef)

# Create curve
curve = list()
for i in range(len(X)):
	value = coef[-1][0]
	for d in range(degree):
		value += X[i]**(degree-d) * coef[d][0]
	curve.append(value)

pyplot.plot(series)
pyplot.plot(curve)
pyplot.show()

# Detrend time series
values = series.values
diff = list()
for i in range(len(values)):
	value = values[i] - curve[i]
	diff.append(value)
pyplot.plot(diff)
pyplot.show()