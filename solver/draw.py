#/usr/bin/python

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

def draw_surface(f, name, x1, x2, dx, t1, t2, dt):
  fig = plt.figure(name)
  ax = fig.gca(projection='3d')
  x = np.arange(x1, x2 + dx, dx)
  t = np.arange(t1, t2 + dt, dt)

  x, t = np.meshgrid(x, t)

  ax.plot_surface(x, t, f, rstride=1, cstride=1, cmap=cm.coolwarm,
          linewidth=0, antialiased=False)

  ax.set_xlabel('x', linespacing=3.2)
  ax.set_ylabel('t', linespacing=3.1)
  ax.set_zlabel('u', linespacing=3.4)

def draw_subplots(name, x, fn, labels):
  fig = plt.figure(name)

  i = iter(labels)
  for f in fn:
    ax = fig.add_subplot(111)
    ax.plot(x, f, label=r'' + next(i))

  plt.legend(loc='upper right')

  x1, x2, y1, y2 = plt.axis()
  a = (x2 - x1) / 8
  b = (y2 - y1) / 8
  plt.axis((x1 - a, x2 + a, y1 - b, y2 + b)) 
  plt.xticks(np.arange(x1, x2, 2))

  #fig.savefig('images/%s.png' % name) 


def show():
  plt.show()