import numpy as np
from d2l import torch as d2l
import matplotlib.pyplot as plt
# Quick Implementation of creating class A and instance a 
class A:
    def __init__(self):
        self.b = 1
a = A()
# Calling the fully implemented hyperparameters class
class B(d2l.HyperParameters):
    def __init__(self, a, b, c):
        self.save_hyperparameters()
        self.a = a
        self.b = b
        self.c = c
# For progress Board 
board = d2l.ProgressBoard('x')
fig, ax = plt.subplots()
for x in np.arange(0, 10, 0.1):
    ax.plot(x, np.sin(x), 'ro', label='sin')  # Red dots for sine
    ax.plot(x, np.cos(x), 'bo', label='cos')  # Blue dots for cosine
    if int(x * 10) % 2 == 0:
        plt.pause(0.1)  
        plt.draw()
plt.show()