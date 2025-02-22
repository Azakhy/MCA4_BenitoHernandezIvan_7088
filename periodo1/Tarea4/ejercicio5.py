#!/usr/bin/python3
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
"""
Ejercicios para la clase de matemáticas IV
5 de febrero del 2025
"""
def f(x, y):
        return (4-2*x)/(3*y**2-5)


nx, ny = .2, .2
x = np.arange(-3, 3, nx)
y = np.arange(-3, 3, ny)

X, Y = np.meshgrid(x, y)

dy_f = f(X, Y)
dx = np.ones(X.shape)

dyu_f = dy_f / np.sqrt(dx**2 + dy_f**2)
dxu_f = dx / np.sqrt(dx**2 + dy_f**2)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.quiver(X, Y, dxu_f, dyu_f, color="orange", headwidth=2)
plt.xticks(x, rotation=60)
plt.yticks(y, fontsize=7)
plt.title("Campo Direccional de $y'=\\frac{4-2x}{3y^2-5}$", color="blue", fontsize="x-large")
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-3,3)
plt.ylim(-3,3)
plt.show()
