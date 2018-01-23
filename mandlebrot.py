import matplotlib as plt
from matplotlib import colors
import numpy as np

def mandlebrot(x,y):
    for xval in range(x):
        for yval in range(y):
            val = 0
            iteration = 0
            while val in range(20):
                val = val * val + x + y*1j
                iteration = iteration + 1
            plt.scatter(x,y,color=(0,0,255,iteration))
    plt.show

mandlebrot(500,1000)
