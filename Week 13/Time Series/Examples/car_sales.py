
from pandas import read_csv
from matplotlib import pyplot

series = read_csv('car-sales.csv', header=0, 
                  index_col=0, parse_dates=True)
series.squeeze('columns')

series.plot()
pyplot.show()