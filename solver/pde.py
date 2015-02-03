#/usr/bin/python

import numpy as np

n, m = 10, 50
x1, x2 = 0., 1.
t1, t2 = 0., 10.
dx, dt = (x2 - x1) / n, (t2 - t1) / m
alpha = np.pi**2 + 1

def f(x, t):
  return 0.

def yt0(x):
  return np.sin(np.pi * x)

def yx0(t):
  return 0.

def yxl(t):
  return 0.