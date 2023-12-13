from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt

x = read_csv('NewsVendor.csv', header=0, index_col=0, parse_dates=True)
x.squeeze('columns')

fig, ax = plt.subplots(figsize=(12, 6))

mu = x.mean()[0]
sigma = x.std()[0]

n_bins = 50

# Plot the histogram
n, bins, patches = ax.hist(x, n_bins, density=True, histtype='step',
                           cumulative=False)

# Add a line showing the expected normal distribution.
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

ax.plot(bins, y, 'k--', linewidth=1.5)

ax.grid(True)

ax.set_title('Distributions')
ax.set_xlabel('Daily demand')
ax.set_ylabel('Probability of occurrence')

plt.show()