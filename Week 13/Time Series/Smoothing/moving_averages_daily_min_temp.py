
from pandas import read_csv
from matplotlib import pyplot

series = read_csv('../Examples/daily-minimum-temperatures_88-90.csv', header=0, index_col=0, parse_dates=True)
series.squeeze('columns')

# compute rolled (smoothed) series for window length of 100 (n=100 observations)
rolling = series.rolling(window = 100)
rolling_mean = rolling.mean()

# plot original and transformed dataset
pyplot.plot(series)
pyplot.plot(rolling_mean,color='red')
pyplot.show()

# zoomed plot original and transformed dataset
pyplot.plot(series[250:300])
pyplot.plot(rolling_mean[250:300],color='red')
pyplot.show()