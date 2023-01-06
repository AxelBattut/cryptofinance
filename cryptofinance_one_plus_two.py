#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import matplotlib.pyplot as plt

# inputs: number of attack cycles n
# q: hashrate

# output: yield: (G1 + Gn) / (H1 + Hn)

num_attacks = 1000
q = 0.01 
hash_rates = []
yields = []
theoretical_yields = []
for _ in range(100):
    G = 0
    H = 0

    for i in range(num_attacks):

        round = []

        for _ in range(3):
            round.append(random.random() <= q)

            if not round[0]:
                break

        mined = sum(round)
        if mined < 2: 
            g = 0
        else:
            g = mined
            h = 3

        if len(round) == 1:
            h = 1
        elif mined < 3:
            h = 2

        G += g
        H += h

    r = G/H
    t = (q**2*(4 - q)) / (1 + q + q**3)
    yields.append(r)
    hash_rates.append(q)
    theoretical_yields.append(t)
    q += 0.01

fig, ax = plt.subplots()
ax.plot(yields, hash_rates, color='red')
fig2, ax2 = plt.subplots()
ax2.plot(theoretical_yields, hash_rates, color='red')

ax.set(xlabel='hash rate', ylabel='yield')
ax2.set(xlabel='hash rate', ylabel='theoretical yield')
ax.grid()
ax2.grid()
plt.show()

