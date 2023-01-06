#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
import numpy as np

def max(a, b):
  if a > b:
    return a
  else:
    return b
    
def E(a, h, n, q, c):
  if n == 0:
    if a > h:
      return a - (a - h) * c
    else:
      return 0
  else:
    if a > h:
      return max(h + 1 - c + E(a - h - 1, 0, n, q, c), 
                 q * E(a + 1, h, n - 1, q, c) + (1 - q) * (E(a, h + 1, n - 1, q, c) - c))
    if a == (h + 1):
      return max(h + 1 - c, q * E(a + 1, h, n - 1, q, c) + (1 - q) * (E(a, h + 1, n - 1, q, c) - c))
    if a <= h:
      return max(0, q * E(a + 1, h, n - 1, q, c) + (1 - q) * (E(a, h + 1, n - 1, q, c) - c))

# We look for q min such that E(0, 0, n, q, q) > 0

def curve_simulation():
  x_values = np.arange(0, 0.6, 0.1)
  y_values = []

  for q in range (0, 6):
    y_values.append(E(0, 0, 3, q / 10, q / 10))
    
  
  plt.plot(x_values, y_values, color='red') 
  plt.xlabel('q')
  plt.ylabel('expected gain')
  plt.show()


curve_simulation()



