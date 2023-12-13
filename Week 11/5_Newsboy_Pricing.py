from scipy.stats import norm
from pandas import read_csv
import matplotlib.pyplot as plt
import numpy as np

x = read_csv('NewsVendor.csv', header=0, index_col=0, parse_dates=True)
x.squeeze('columns')

n_bins=25
fig, ax = plt.subplots(figsize=(12, 6))

n, bins, patches = ax.hist(x, n_bins, density=True, histtype='step', cumulative=False)
plt.show()

p = 1.
c = 0.325
s = 0.1

c_u = p - c
c_o = c - s

mu=x.mean()[0]
sigma=x.std()[0]
#sigma=50

G = norm(mu,sigma)
pr = G.pdf(range(300))

plt.plot(pr)
plt.show()

def W(Q):
    ES = sum((min(Q,i)*pr[i] for i in range(len(pr))))
    return (c_o+c_u)*ES - c_o*Q

profit = [W(Q) for Q in range(len(pr))]

plt.plot(profit)
plt.show()

Qstar = int(np.ceil(G.ppf(c_u/(c_o+c_u))))
#Qstar = 150

print(Qstar)

print('order','profit')
for Q in range(Qstar-3, Qstar+5):
#for Q in range(len(pr)):
    print(Q, W(Q))
    

    


