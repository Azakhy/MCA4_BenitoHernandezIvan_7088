#!/usr/bin/python3
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq
from sympy.plotting import plot_implicit
import math

x, y = symbols('x y')

p1 = plot_implicit(Eq(y**3 - 5*y + x**2 - 4*x, -6), (x, -2, 6),
                   (y, -3, 3), line_color='darkgoldenrod',
                   title="y^3 - 5y + x^2 - 4x = -6",
                   fontsize='medium', show=False)
p2 = plot_implicit(Eq(y**3 - 5*y + x**2 - 4*x, 0), (x, -2, 6),
                   (y, -3, 3), line_color='darkorange',
                   title="y^3 - 5y + x^2 - 4x = 0",
                   fontsize='medium', show=False)
p4 = plot_implicit(Eq(y**3 - 5*y + x**2 - 4*x, 6), (x, -2, 6),
                   (y, -3, 3), line_color='crimson',
                   title="Gráficas de la solución y^3 - 5y + x^2 - 4x = 6",
                   fontsize='medium', show=False)
p7 = plot_implicit(Eq(y**3 - 5*y + x**2 - 4*x, -6), (x, -2, 6),
                   (y, -3, 3), line_color='darkgoldenrod',
                   title="Gráficas de la solución y^3 - 5y + x^2 - 4x = c",
                   fontsize='medium', show=False)
p7.append(p2[0])
p7.append(p4[0])
p7.show()

