#/usr/bin/python

import numpy as np
import math

n, m = 50, 200
x1, x2 = 0., 1.0
t1, t2 = 0., 1.0
dx, dt = (x2 - x1) / n, (t2 - t1) / m
sigma = 15.
v = 1.0

eps = 0.0001

def alpha(x):
  return sigma**2 * (2. / (np.cosh(sigma * (x - 0.5)))**2 - 1)#np.pi**2 + 3

def U(sigma, x):
  return -2 * sigma * np.tanh(sigma * (x - 0.5)) 

def us(x):
  return U(sigma, x)

def dus(x):
  return -2 * (sigma**2) * (1 - (np.tanh(sigma / 2)**2))

def yt0(x):
  return x**2 #+ us(x)#us(x1) + 2 + (us(x2) - us(x1) - 4) * x

def yx0(t):
  return 0.#-2 * (sigma**2) * (1 - (np.tanh(sigma / 2)**2))

def yxl(t):
  return 0.#-2 * (sigma**2) * (1 - (np.tanh(sigma / 2)**2))

def sreac_term(sigma, x):
  return sigma**2 * (2 / (np.cosh(sigma * (x - 0.5))**2) - 1)

def reac_term(x):
  return sreac_term(sigma, x)

def G(x):
  return np.cosh(sigma * (x - 0.5)) / np.cosh(sigma / 2)

def theta(u):
  theta = []
  for j in range(m + 1):
    theta.append([u[j][i] / G(x1 + i * dx) for i in range(n + 1)])
  return theta
