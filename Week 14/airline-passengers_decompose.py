from pandas import read_csv
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose

series = read_csv('airline-passengers.csv', header=0, index_col=0, parse_dates=True)
series.squeeze('columns')
series.plot()
pyplot.show()

# Additive decompose
result = seasonal_decompose(series, model='additive')
result.plot()
pyplot.show()

# Show the residuals in a separate plot
result.resid.plot()
pyplot.show()

# Multiplicative decompose (For this dataset, multiplicative is better)
result = seasonal_decompose(series, model='multiplicative')
result.plot()
pyplot.show()

# Show the residuals in a separate plot
result.resid.plot()
pyplot.show()