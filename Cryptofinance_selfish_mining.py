#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random
import matplotlib.pyplot as plt

hashrate_S = 0.01 # S hashrate
# hashrate_honest_miners = 1 - hashrate_S # honest miners hashrate
n_cycles = 1000  # number of cycles to do

q_values = []
r_values = []

# Beginning of strategy
for i in range(49):
    g_blocks = 0
    h_blocks = 0
    for j in range(n_cycles):
        g = 0
        h = 1
        if (random.random() <= hashrate_S): # S can mine first else it is the end of the cycle
            if (random.random() > hashrate_S): # S is first to validate a block but then H mines one block before S
                g = 1 # S broadcast the secret block
                # end of the cycle
            else: # S mines two in a row
                h = 2
                fork = 2
                legacy = 0
                while fork - legacy > 1: # while S advances > 1 : mine
                    if (random.random() <= hashrate_S): # S mines
                        fork += 1
                    else: # H mines
                        legacy += 1
                    h += 1
                # that means S lost the advance
                g = fork # broadcast the fork

        g_blocks += g
        h_blocks += h

    r = g_blocks / h_blocks
    r_values.append(r)
    q_values.append(hashrate_S)
    hashrate_S += 0.01

fig, ax = plt.subplots()
ax.plot(q_values, r_values, color='red') 
ax.set(xlabel='q', ylabel='R')
plt.show()

