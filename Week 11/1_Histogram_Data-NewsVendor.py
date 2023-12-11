from pandas import read_csv
import matplotlib.pyplot as plt

x = read_csv('NewsVendor.csv', header=0, index_col=0, parse_dates=True)
x.squeeze('columns')

print(x.mean()[0], x.std()[0])

fig, ax = plt.subplots(figsize=(12, 6))

# Plot the histogram
n_bins = 100
# density=True to plot pdf instead of number of occurrences (probilities)
# cumulative=True to plot the cumulative distribution function instead of the probability density function
n, bins, patches = ax.hist(x, n_bins, density=False, histtype='step', cumulative=False)


ax.grid(True)

ax.set_title('Histogram of daily demand')
ax.set_xlabel('Daily demand')
ax.set_ylabel('Number of occurrences')

plt.show()
