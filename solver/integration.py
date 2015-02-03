#/usr/bin/python

from cmath import *

def mpow(a, b):
  return exp(b * log(a))

def d1(p):
  return mpow(p, -3) * complex(2 * p * cos(p) - sin(p) * (2 - mpow(p, 2)), mpow(p, 2) * cos(p) - p * sin(p))

def d2(p):
  return complex(mpow(p, -3) * (4 * sin(p) - 4 * cos(p) * p), 0)

def d3(p):
  return mpow(p, -3) * complex(2 * p * cos(p) + sin(p) * (mpow(p, 2) - 2), p * sin(p) - mpow(p, 2) * cos(p))

def integrate(arr, a, b, j):
  i = complex(0, 1)
  l = (b - a) / 2
  half = (a + b) / 2
  ll = len(arr) - 1
  return l * exp(i * j * half) * (d1(j * l) * arr[0] + d2(j * l) * arr[ll / 2] + d3(j * l) * arr[ll])

def integrate_sin(arr, a, b, j):
  return integrate(arr, a, b, j).imag

def integrate_cos(arr, a, b, j):
  return integrate(arr, a, b, j).real       