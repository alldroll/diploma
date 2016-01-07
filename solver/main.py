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
    #result = []
    #rs = [r for r in np.arange(0.5, 50.05, 5)]
    #for r in rs:
        #u = implicit_perturbation_heat_equation(Omega([[0, 0.3]]), r, 3, alpha)
        #result.append(u[m][n / 2] / G(x1 + n/2 * dx))
    #draw_subplots('r_m', rs, [result], [''])

    #result = []
    #r = 100.
    #ms = [m for m in range(1, 20)]
    #for m in ms:
        #u = implicit_perturbation_heat_equation(Omega([[0, 0.3]]), r, m, alpha)
        #result.append(u[m][n / 2] / G(x1 + n/2 * dx))
    #draw_subplots('m_r', ms, [result], [''])


    #draw_surface(theta(u), '', x1, x2, dx, t1, t2, dt)


    #analysis stabilization's params
    show()

    return

if __name__ == '__main__':
    main()
