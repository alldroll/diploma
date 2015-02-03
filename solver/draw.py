#/usr/bin/python

import pde
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

def draw(f, name, text = ''):
  fig = plt.figure(name)
  ax = fig.gca(projection='3d')
  x = np.arange(pde.x1, pde.x2 + pde.dx, pde.dx)
  t = np.arange(pde.t1, pde.t2 + pde.dt, pde.dt)
  x, t = np.meshgrid(x, t)

  surf = ax.plot_surface(x, t, f, rstride=1, cstride=1, cmap=cm.coolwarm,
          linewidth=0, antialiased=False)

  xLabel = ax.set_xlabel('x', linespacing=3.2)
  yLabel = ax.set_ylabel('t', linespacing=3.1)
  zLabel = ax.set_zlabel('u', linespacing=3.4)


def show():
  plt.show()