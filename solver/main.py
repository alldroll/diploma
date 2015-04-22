#/usr/bin/python

from solver import *
from draw import *

def main():


  ##shock-like solutions fig2
  # x = np.arange(0, 1, 0.01)
  # draw_subplots('fig1', x, 
  #   [[U(3, i) for i in x], [U(8, i) for i in x], [U(15, i) for i in x]], 
  #   ['$\sigma = 3$', '$\sigma = 8$', '$\sigma = 15$']
  # )

  ##reaction coeff fig1
  # x = np.arange(0, 1, 0.01)
  # draw_subplots('fig2', x, 
  #   [[reac_term(4, i) for i in x], [reac_term(10, i) for i in x]], 
  #   ['$\sigma = 4$', '$\sigma = 10$']
  # ) 


  ##linear heat equation stabilization 
  #u = implicit_heat_equation(Omega([[0., 0.2]]), 10., 3, alpha)
  e = implicit_heat_equation(Omega([[0., 0.]]), 0., 0, alpha)
  u = implicit_heat_equation(Omega([[0., 0.4]]), 8., 2, alpha)
  #e = implicit_perturbation_burger_equation(Omega([[0, 0.2]]), 0, 0)
  #u = implicit_perturbation_burger_equation(Omega([[0, 0.2]]), 10., 3)
  draw_surface(e, 'exactly', x1, x2, dx, t1, t2, dt)  
  draw_surface(u, 'repaired', x1, x2, dx, t1, t2, dt)

  ##show on chosed time several plots
  # x = np.arange(x1, x2 + dx, dx)
  # draw_subplots('', x, [[c[m][i] for i in range(n + 1)], [c[100][i] for i in range(n + 1)], [c[400][i] for i in range(n + 1)]])

  ##burger equation (fig.5)
  
  #u = implicit_burger_equation()
  # draw_surface(u, 'expl', x1, x2, dx, t1, t2, dt)

  ##burger equation (fig.7)
  #u = implicit_perturbation_burger_equation(Omega([[0, 0.2]]), 2, 2)
  #s = implicit_perturbation_burger_equation(Omega([[0, 0.2]]), 0, 1)
  # draw_surface(u, 'impl', x1, x2, dx, t1, t2, dt)
  
  #x = np.arange(x1, x2 + dx, dx)

  #draw_subplots('', x, [[reac_term(sigma, x1 + i * dx) for i in range(n + 1)]])
  #draw_surface(u, 'impl', x1, x2, dx, t1, t2, dt)

  # u = implicit_heat_equation(Omega([[0, 2]]), 0, 1, alpha)

  #draw_surface(u, 'repair', x1, x2, dx, t1, t2, dt)
  #draw_surface(e, 'exactly', x1, x2, dx, t1, t2, dt)
  #draw_surface(u, 'new', x1, x2, dx, t1, t2, dt)

  #draw_subplots('', x, [[0.5 * (dus(i * dx + x1) + us(i * dx + x1)**2 / 2) for i in range(n + 1)]])
  show()



if __name__ == '__main__':
  main()
