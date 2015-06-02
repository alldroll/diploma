#/usr/bin/python

from solver import *
from draw import *

def main():

    #shock-like sol
    #x = np.arange(0, 1, 0.01)
    #draw_subplots('fig1', x, 
        #[[U(3, i) for i in x], [U(8, i) for i in x], [U(15, i) for i in x]], 
        #['$\\tau = 3$', '$\\tau = 8$', '$\\tau = 15$']
    #)

    #reaction coeff fig2
    x = np.arange(0, 1, 0.01)
    draw_subplots('fig2', x, 
        [[sreac_term(4, i) for i in x], [sreac_term(10, i) for i in x]], 
        ['$\\tau = 4$', '$\\tau = 10$']
    )

    #example of stabilazing burger equation
#    u = implicit_perturbation_heat_equation(Omega([[0, 0.4]]), 15, 3, alpha)
#    draw_surface(theta(u), '', x1, x2, dx, t1, t2, dt)
    show()

    return

if __name__ == '__main__':
    main()
