from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt

# Part a)
# Read the data and plot the histogram
n_bins = 400
x = read_csv('daily-minimum-temperatures.csv', header=0, index_col=0, parse_dates=True)
x.squeeze('columns')

fig, ax = plt.subplots(figsize=(12, 6))
ax.grid(True)

# Plot the histogram
# n, bins, patches = ax.hist(x, n_bins, density=False, histtype='step', cumulative=False)  # Part a

# Part b)
# Plot the cumulative histogram
n, bins, patches = ax.hist(x, n_bins, density=True, histtype='step', cumulative=True)  # Part b

# Part e)
mu = x.mean()[0]
sigma = x.std()[0]
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
y = y.cumsum()
y /= y[-1]

ax.plot(bins, y, 'k--', linewidth=1.5)


plt.show()

print(mu, sigma)  # Part c