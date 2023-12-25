from matplotlib import pyplot
from pandas import read_csv
from statsmodels.tsa.api import SimpleExpSmoothing

series = read_csv('stock-market-turnover-ratio.csv', header=0, 
                  index_col=0, parse_dates=True)
series.squeeze('columns')

series.plot()
pyplot.show()

fit1 = SimpleExpSmoothing(series).fit(smoothing_level=0.2,optimized=False)
fcast1 = fit1.forecast(30).rename(r'$\alpha=0.2$')
# plot
fcast1.plot(marker='o', color='blue', legend=True)
fit1.fittedvalues.plot(marker='o',  color='blue')

fit2 = SimpleExpSmoothing(series).fit(smoothing_level=0.6,optimized=False)
fcast2 = fit2.forecast(30).rename(r'$\alpha=0.6$')
# plot
fcast2.plot(marker='o', color='red', legend=True)
fit2.fittedvalues.plot(marker='o', color='red')

fit3 = SimpleExpSmoothing(series).fit()
fcast3 = fit3.forecast(30).rename(r'$\alpha=%s$'%fit3.model.params['smoothing_level'])
# plot
fcast3.plot(marker='o', color='green', legend=True)
fit3.fittedvalues.plot(marker='o', color='green')

pyplot.show()

series.plot()
fcast3.plot(marker='o', color='green', legend=True)
fit3.fittedvalues.plot(marker='o', color='green')

pyplot.show()