#/usr/bin/python

import integration as intg
import math

class Omega(object):
  """docstring for Omega"""
  def __init__(self, low, high):
    self.low = low
    self.high = high

def chi(omega, x):
  return int(x >= omega.low and x <= omega.high)

def pm(m, u, x1, x2):
  l = x2 - x1
  c = lambda i : math.sqrt(2. / l) * intg.integrate_sin(u, x1, x2, i)
  ans = [c(i) for i in range(1, m + 1)]
  return math.sqrt(2. / l) * sum(ans)