#/usr/bin/python

from integration import *
from control import *
from pde import *

def tdma(a, b, c, d):
  nf = len(a)
  ac, bc, cc, dc = map(np.array, (a, b, c, d))
  
  for i in xrange(1, nf):
    mc = ac[i] / bc[i - 1]
    bc[i] = bc[i] - mc * cc[i - 1]
    dc[i] = dc[i] - mc * dc[i - 1]
   
  xc = ac
  xc[-1] = dc[-1] / bc[-1]
   
  for i in xrange(nf - 2, -1, -1):
    xc[i] = (dc[i] - cc[i] * xc[i + 1]) / bc[i]
   
  del bc, cc, dc
  return xc 

#it works
#TODO use tdma, refactor
def implicit_heat_equation(om, r, p, alpha):
  g = dt / (dx ** 2)
  b = [(1. + 2 * g - alpha * dt)] * (n + 1)
  a = [-g] * (n + 1)
  c = [-g] * (n + 1)

  u = [[0. for x in range(n + 1)] for x in xrange(m + 1)]

  for i in range(n + 1):
    u[0][i] = yt0(x1 + i * dx)

  d = lambda i, j : u[j - 1][i] - dt * r * chi(om, x1 + i * dx) * pm(p, u[j - 1], x1, x2)

  for j in range(1, m + 1):
    al, be = [0.] * n, [0.] * n
    be[0] = yx0(t1 + j * dt)

    for i in range(1, n):
      g = b[i] + c[i] * al[i - 1]
      al[i] = - a[i] / g
      be[i] = (d(i, j) - c[i] * be[i - 1]) / g

    u[j][n] = yxl(t1 + j * dt)

    for i in range(n - 1, -1, -1):
      u[j][i] = al[i] * u[j][i + 1] + be[i]

  return u

#it works
def explicit_burger_equation():
  u = [[0. for x in range(n + 1)] for x in xrange(m + 1)]
  g = dt / (dx**2)
  f = lambda u: u**2 / 2

  for i in range(n + 1):
    u[0][i] = yt0(x1 + i * dx)

  for j in range(1, m + 1):
    for i in range(1, n):
      uxx = u[j - 1][i + 1] - 2 * u[j - 1][i] + u[j - 1][i - 1]
      ux = (f(u[j - 1][i - 1]) - f(u[j - 1][i + 1])) / 2
      u[j][i] = u[j - 1][i] + g * (v * uxx +  dx * ux)
    u[j][0] = u[j][1] - dx * yx0(t1 + dt * j)
    u[j][n] = u[j][n - 1] + dx * yxl(t1 + dt * j)
  return u

#TODO refactor
def implicit_burger_equation():
  u = [[0. for x in range(n + 1)] for x in xrange(m + 1)]
  g = v * dt / (dx**2)
  k = dt / (2 * dx)

  for i in range(n + 1):
    u[0][i] = yt0(x1 + i * dx)

  a = [0.] * (n + 1)
  b = [1 + 2 * g] * (n + 1)
  c = [0.] * (n + 1)
  d = [0.] * (n + 1) 

  for j in range(1, m + 1):
    a[1:-1] = [(-g - k * u[j - 1][i]) for i in range(1, n)]

    # Dirichlet    
    # a[0] = 0
    # b[0] = 1
    # c[0] = 0
    # d[0] = 0.

    # Neumann   
    b[0] = -1
    c[0] = 1
    d[0] = dx * yx0(t1 + j * dt)
    a[-1] = -1
    b[-1] = 1
    d[-1] = dx * yxl(t1 + j * dt)

    c[1:-1] = [(-g + k * u[j - 1][i]) for i in range(1, n)]
    d[1:-1] = [u[j - 1][i] for i in range(1, n)]

    u[j] = tdma(a, b, c, d)

  return u

#TODO refactor
def implicit_perturbation_burger_equation(om, r, p):
  u = [[0. for x in range(n + 1)] for x in xrange(m + 1)]
  g = v * dt / (dx**2)
  k = dt / (2 * dx)

  for i in range(n + 1):
    u[0][i] = yt0(x1 + i * dx) - us(x1 + i * dx)

  a = [0.] * (n + 1)
  b = [1 + 2 * g] * (n + 1)
  c = [0.] * (n + 1)
  d = [0.] * (n + 1) 

  s = lambda i: k * (us(x1 + i * dx) + u[j - 1][i])

  for j in range(1, m + 1):
    a[1:-1] = [-(g + s(i)) for i in range(1, n)]

    # Dirichlet    
    a[0] = 0
    b[0] = 1
    c[0] = 0
    d[0] = 0.

    a[-1] = 0
    b[-1] = 1
    c[-1] = 0
    d[-1] = 0.

    # Neumann
    # d[0] = 0
    # d[-1] = 0
    # b[0] = -1
    # c[0] = 1
    # a[-1] = -1
    # b[-1] = 1

    c[1:-1] = [(s(i) - g) for i in range(1, n)]
    d[1:-1] = [u[j - 1][i] * (1 - dt * dus(x1 + i * dx)) for i in range(1, n)] #- dt * r * chi(om, x1 + i * dx) * pm(p, u[j - 1], x1, x2) 

    u[j] = tdma(a, b, c, d)

  return u

# def implicit_perturbation_burger_equation(om, r, p):
#   u = [[0. for x in range(n + 1)] for x in xrange(m + 1)]
#   g = v * dt / (dx**2)
#   k = dt / (2 * dx)

#   for i in range(n + 1):
#     u[0][i] = yt0(x1 + i * dx) - us(x1 + i * dx)

#   a = [0.] * (n + 1)
#   b = [1 + 2 * g] * (n + 1)
#   c = [0.] * (n + 1)
#   d = [0.] * (n + 1) 

#   s = lambda i: k * (us(x1 + i * dx) + u[j - 1][i])

#   for j in range(1, m + 1):
#     a[1:-1] = [-(g + s(i)) for i in range(1, n)]
#     a[-1] = b[0] = 1
#     b[-1] = c[0] = -1
#     c[1:-1] = [(s(i) - g) for i in range(1, n)]
#     d[0] = 0.
#     d[1:-1] = [u[j - 1][i] * (dt * dus(x1 + i * dx) - 1) - dt * r * chi(om, x1 + i * dx) * pm(p, u[j - 1], x1, x2) for i in range(1, n)]
#     d[-1] = 0.
#     u[j] = tdma(a, b, c, d)

#   return u

#TODO implement
def crank_nicolson_burger_equation(om, r, p, alpha):
  return 0

