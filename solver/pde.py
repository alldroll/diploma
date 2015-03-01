#/usr/bin/python

import numpy as np
import math

n, m = 200, 200
x1, x2 = 0., 1.0
t1, t2 = 0., 1.6
dx, dt = (x2 - x1) / n, (t2 - t1) / m
alpha = np.pi**2 + 1
sigma = 3.
v = 1.0

eps = 0.0001


def us(x):
  return -2 * sigma * np.tanh(sigma * (x - 0.5))

def dus(x):
  return -2 * (sigma**2) * (1 - (np.tanh(sigma / 2)**2))

def yt0(x):
  return us(x1) + 2 + (us(x2) - us(x1) - 4) * x

def yx0(t):
  return -2 * (sigma**2) * (1 - (np.tanh(sigma / 2)**2))

def yxl(t):
  return -2 * (sigma**2) * (1 - (np.tanh(sigma / 2)**2))

def reac_term(sigma, x):
  return sigma**2 * (2 / (np.cosh(sigma * (x - 0.5))**2) - 1)