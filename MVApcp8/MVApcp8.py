#works on numpy 1.23.5, matplotlib 3.6.2 and scipy 1.9.3
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

z1 = np.array([0, 2, 3, 2])
z2 = np.array([3, 2, 2, 1])
n = 400

x1 = np.linspace(1, 4, n)
y1 = CubicSpline(np.arange(len(z1)), z1)(np.linspace(0, len(z1) - 1, n))
x2 = np.linspace(1, 4, n)
y2 = CubicSpline(np.arange(len(z2)), z2)(np.linspace(0, len(z2) - 1, n))

fig, ax = plt.subplots(figsize = (12,10))

ax.plot(x1, y1, lw=2)
ax.plot(x2, y2, lw=2, color="red")

ax.scatter(1,0)
ax.scatter(1,3)
ax.scatter(2,2)
ax.scatter(3,2)
ax.scatter(3,3)
ax.scatter(4,1)
ax.scatter(4,2)

ax.yaxis.set_ticks(np.arange(0, 3.1, 1))
ax.xaxis.set_ticks(np.arange(1, 4.1, 1))
ax.set_xlabel("Coordinate", fontsize = 25)
ax.set_ylabel("Coordinate Value", fontsize = 25)
ax.tick_params(axis='both', labelsize = 25)
ax.set_title("Parallel Coordinates Plot with Cubic Spline",fontsize = 30, fontweight = "bold", pad = 15)
plt.show()
