from scipy.stats import expon
from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np

x = read_csv('Exercise #2_Newsvendor_Problem.csv', header=0, index_col=0, parse_dates=True).squeeze()

n_bins=100
fig, ax = plt.subplots(figsize=(12, 6))

n, bins, patches = ax.hist(x, n_bins, histtype='step', cumulative=False) #density=True,
plt.show()

p = 1.
c = 0.325
s = 0.1

c_u = p - c 
c_o = c - s

mu = x.mean()

G = expon(0, mu)
pr = G.pdf(range(400))

plt.plot(pr)
plt.show()


def W(Q):
    ES = sum((min(Q, i) * pr[i] for i in range(len(pr))))
    return (c_o + c_u) * ES - c_o * Q

profit = [W(Q) for Q in range(len(pr))]


plt.plot(profit)
plt.show()

print('order','profit')
for Q in range(115, 125):
    print(Q, W(Q))

Qstar = int(np.ceil(G.ppf(c_u / (c_o + c_u))))

print("The Q star is", Qstar)


    

    


