#/usr/bin/python

from solver import *
from draw import *


def main():

  ##linear heat equation stabilization 
  # u = implicit_heat_equation(Omega(0., 0.4), 1, 1, alpha)
  # e = implicit_heat_equation(Omega(0., 0.0), 0, 0, alpha)
  # draw_surface(e, 'exactly', x1, x2, dx, t1, t2, dt)  
  # draw_surface(u, 'repaired', x1, x2, dx, t1, t2, dt)

  ##shock-like solutions
  # x = np.arange(0, 1, 0.01)
  # draw_subplots('static', x, [[us(3, i) for i in x], [us(8, i) for i in x], [us(15, i) for i in x]])

  ##reaction coeff
  # x = np.arange(0, 1, 0.01)
  # draw_subplots('fig2', x, [[reac_term(4, i) for i in x], [reac_term(10, i) for i in x]]) 

  ##show on chosed time several plots
  # x = np.arange(x1, x2 + dx, dx)
  # draw_subplots('', x, [[c[m][i] for i in range(n + 1)], [c[100][i] for i in range(n + 1)], [c[400][i] for i in range(n + 1)]])

  ##burger equation (fig.5)
  
  u = implicit_burger_equation()
  # draw_surface(u, 'expl', x1, x2, dx, t1, t2, dt)

  ##burger equation (fig.7)
  #u = implicit_perturbation_burger_equation(Omega([[0, 2]]), 2, 1)
  # draw_surface(u, 'impl', x1, x2, dx, t1, t2, dt)
  
  #x = np.arange(x1, x2 + dx, dx)

  #draw_subplots('', x, [[1./2 * (dus(x1 + i * dx) + (us(x1 + i * dx)**2) / 2) for i in range(n + 1)]])
  draw_surface(u, 'impl', x1, x2, dx, t1, t2, dt)

  #draw_subplots('', x, [[0.5 * (dus(i * dx + x1) + us(i * dx + x1)**2 / 2) for i in range(n + 1)]])
  show()



if __name__ == '__main__':
  main()