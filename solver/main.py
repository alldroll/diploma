#/usr/bin/python


from integration import *
from draw import *
from control import *
from pde import *

def solve(om, r, p, alpha):
  g = dt / (dx ** 2)
  b = [(1. + 2 * g - alpha * dt)] * (n + 1)
  a = [-g] * (n + 1)
  c = [-g] * (n + 1)

  u = [[0. for x in range(n + 1)] for x in xrange(m + 1)]

  for i in range(n + 1):
    u[0][i] = yt0(x1 + i * dx)

  d = lambda i, j : u[j - 1][i] + dt * f(x1 + i * dx, t1 + j * dt) - r * chi(om, x1 + i * dx) * pm(p, u[j - 1], x1, x2)

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

def main():

  u = solve(Omega(0., 0.4), 1, 1, alpha)
  e = solve(Omega(0., 0.0), 0, 0, alpha)

  draw(e, 'exactly', '')  
  draw(u, 'repaired', '$\omega = [0, 0.1], r = 1.0$')
  show()

if __name__ == '__main__':
  main()