
from pandas import read_csv
from matplotlib import pyplot

series = read_csv('daily-minimum-temperatures_88-90.csv', header=0, 
                  index_col=0, parse_dates=True)
series.squeeze('columns')

series.plot()
pyplot.show()