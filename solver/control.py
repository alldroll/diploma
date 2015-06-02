#/usr/bin/python

import integration as intg
import math
from pde import *


class Omega(object):
  """docstring for Omega"""
  def __init__(self, intervals):
    self.intervals = intervals

def chi(omega, x):
  success = False
  for interval in omega.intervals:
    success = (x >= interval[0] and x <= interval[1])
    if success: 
      #print "%f in [%f, %f]" % (x, interval[0], interval[1])
      break
  return success

def pm(m, u, x1, x2, x):
  l = x2 - x1
  c = lambda i : math.sqrt(2. / l) * intg.integrate_sin(u, x1, x2, i)
  ans = [c(i) * math.sin(math.pi * i * x) for i in range(1, m + 1)]
  return math.sqrt(2. / l) * sum(ans)

def extended_control(u, p):
    p_m = [pm(p, u, x1, x2, x1 + i * dx) for i in range(n + 1)]
    u2 = [u[i] * u[i] for i in range(n + 1)]
    n_u = np.trapz(u2, dx=dx)
    n_p = np.trapz([u[i] * p_m[i] for i in range(n + 1)], dx=dx)
    n_q = n_u - n_p
    return p_m if n_p >= 4 * n_q else [0. for i in range(n + 1)]
