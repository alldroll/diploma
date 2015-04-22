#/usr/bin/python

import integration as intg
import math

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

def pm(m, u, x1, x2):
  l = x2 - x1
  c = lambda i : math.sqrt(2. / l) * intg.integrate_sin(u, x1, x2, i)
  ans = [c(i) for i in range(1, m + 1)]
  return math.sqrt(2. / l) * sum(ans)
