import numpy as np

def f(x):
  return x**4 - 2*x + 1

nodos = 11
x_ini = 0
x_fin = 2

def simpson_integrate_f(f, x_ini, x_fin, nodos):
  x, h = np.linspace(x_ini, x_fin, num = nodos, retstep=True)
  return (f(x[0]) + 2*np.sum(f(x[2:-1:2])) + 4*np.sum(f(x[1:len(x):2])) + f(x[-1]))*h/3

integral = simpson_integrate_f(f, x_ini, x_fin, nodos)

print(f"integral = {integral}")