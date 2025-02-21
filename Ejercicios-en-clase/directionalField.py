#!/usr/bin/python3
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import argparse

"""
Ejercicios para la clase de matemáticas IV
5 de febrero del 2025
y, -y/x, y/x
"""
parser = argparse.ArgumentParser(description="Descripción del programa")
parser.add_argument('ecuacion')
args = parser

def f(x, y):
    return ((3 * x * y) + 1) / x

def g(x, y):
    return (4 - 2 * x) / (3 * y**2 - 5)

nx, ny = .2, .2
x = np.arange(-2.5, 4.6, nx)
y = np.arange(-3, 3, ny)

# Puntos de evaluación
X, Y = np.meshgrid(x, y)

# Derivadas para f y g
dy_f = f(X, Y)
dy_g = g(X, Y)
dx = np.ones(X.shape)

# Normalizar
dyu_f = dy_f / np.sqrt(dx**2 + dy_f**2)
dxu_f = dx / np.sqrt(dx**2 + dy_f**2)
dyu_g = dy_g / np.sqrt(dx**2 + dy_g**2)
dxu_g = dx / np.sqrt(dx**2 + dy_g**2)

# Graficas
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.quiver(X, Y, dxu_f, dyu_f, color="orange", headwidth=2)
plt.xticks(x, rotation=60)
plt.yticks(y, fontsize=7)
plt.title("Campo Direccional de y' = f(x, y)", color="blue", fontsize="x-large")

plt.subplot(1, 2, 2)
plt.quiver(X, Y, dxu_g, dyu_g, color="purple", headwidth=2)
plt.xticks(x, rotation=60)
plt.yticks(y, fontsize=7)
plt.title("Campo Direccional de y' = g(x, y)", color="green", fontsize="x-large")

plt.tight_layout()
plt.show()
