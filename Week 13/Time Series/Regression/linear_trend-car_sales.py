# Use a linear model to detrend a time series
from pandas import read_csv
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot
import numpy

series = read_csv('car-sales.csv', header=0, index_col=0) 

# Fit linear model
X = [i for i in range(0, len(series))]
X = numpy.reshape(X, (len(X), 1))
y = series.values
model = LinearRegression()
model.fit(X, y)

print()
print(model.coef_)
print(model.intercept_)

# Calculate trend
trend = model.predict(X)

# Plot trend
pyplot.plot(y)
pyplot.plot(trend)
pyplot.show()

# Detrend
detrended = [y[i]-trend[i] for i in range(0, len(series))]

# Plot detrended
pyplot.plot(detrended)
pyplot.show()
