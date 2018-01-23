import matplotlib as plt
from matplotlib import figure
import numpy as np

X = [0, 1, 2]
Y = [0, 1, 2]
Z = [0, 1, 2]
C = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]])
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.scatter(X, Y, Z, c = C/255.0)
plt.show()
