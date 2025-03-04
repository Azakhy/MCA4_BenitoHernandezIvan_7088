#!/usr/bin/python3
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

def edo_autonoma(fy,yx,x_val,y_val,step,c_val,sol_eq):
  x=np.linspace(x_val[0],x_val[1],step)
  y=np.linspace(y_val[0],y_val[1],step)
  X,Y=np.meshgrid(x,y)

  dy=f(Y)
  dx=np.ones_like(X)

  length=np.sqrt(dx**2+dy**2)
  dx,dy=dx/length,dy/length

  #Generar puntos para las curvas de solucion
  if yx=='None':
    for sol in sol_eq:
      plt.axhline(y=sol, linestyle='--')
    plt.quiver(X, Y, dx, dy, color='black', headlength=3)
    plt.title("Direction Field and Solution Curves")
    plt.xlim(x_val[0],x_val[1])
    plt.ylim(y_val[0],y_val[1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()
  else:
    x_curves=np.linspace(x_val[0],x_val[1],step)
    for c in c_val:
      y_curves=yx(x_curves,c)
      plt.plot(x_curves,y_curves)
    # Graficar las soluciones de equilibrio
    for sol in sol_eq:
      plt.axhline(y=sol, linestyle='--')
    plt.quiver(X, Y, dx, dy, color='black', headlength=3)
    plt.title("Campo Direccional y Curvas Solucion")
    plt.xlim(x_val[0],x_val[1])
    plt.ylim(y_val[0],y_val[1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='best')
    plt.show()

def f(y):
    k = 2 #capacidad de carga
    r = 1 #Tasa de crecimiento:with
    return y*(1-y/k)

def y(x,c):
    return (c*2*np.exp(x)) / (1+c*np.exp(x))

x_val=[-5,5]
y_val=[-5,5]
step=30
c_val=[-2,-1,1,2]
sol_eq=[0,2]

edo_autonoma(f,y,x_val,y_val,step,c_val,sol_eq)
