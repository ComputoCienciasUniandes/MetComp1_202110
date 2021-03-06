import numpy as np
import matplotlib.pyplot as plt

def L(x, x_values, y_values):
    """Polinomio de Lagrange
    """
    n_points = len(x_values)
    y = 0.0
    for i in range(n_points):
        l_i = 1.0
        for j in range(n_points):
            if i!=j:
                l_i = l_i * (x-x_values[j])/(x_values[i]-x_values[j])
        y = y + l_i*y_values[i]
    return y

def dL(x, x_values, y_values):
    """Primera derivada del polinomio de Lagrange
    """
    h = 1E-3
    d = (L(x+h, x_values, y_values) - L(x-h, x_values, y_values))/(2.0*h)
    return d

def ddL(x, x_values, y_values):
    """Segunda derivada del polinomio de Lagrange
    """
    h = 1E-3
    dd = (dL(x+h, x_values, y_values) - dL(x-h, x_values, y_values))/(2.0*h)
    return dd

def find_max(x_values, y_values):
    """Encuentra un maximo del polinomio de Lagrange.
    """
    x = x_values.mean()
    while np.abs(dL(x, x_values, y_values))>1E-6:
        x = x  - dL(x, x_values, y_values)/ddL(x, x_values, y_values)
    return x

def find_half_max_width(x_values, y_values):
    """Encuentra el ancho a mitad de altura del polinomio de Lagrange.
    """
    epsilon = 1E-6
    x_max = find_max(x_values, y_values)
    y_max = L(x_max,x_values,y_values)
    x = x_max-10
    while np.abs(L(x, x_values, y_values) - 0.5*y_max)>epsilon: 
        x = x - (L(x,x_values,y_values) - 0.5*y_max)/dL(x, x_values, y_values)
    x_half_1 = x

    x = x_max+10
    while np.abs(L(x, x_values, y_values) - 0.5*y_max)>epsilon:        
        x = x - (L(x,x_values,y_values) - 0.5*y_max)/dL(x, x_values, y_values)
    x_half_2 = x
    gamma = x_half_2 - x_half_1
    return gamma
        

x_values = np.array([  0.,  20.,  40.,  60.,  80., 100., 120., 140., 160., 180., 200.])
y_values = np.array([ 2.44, 3.91, 7.05, 14.77, 29.67, 25.18, 11.66, 5.84, 3.39, 2.15, 1.50])


n_points = 200
x_line = np.linspace(x_values.min(), x_values.max(), n_points)
y_line = np.zeros(n_points)
for i in range(n_points):
    y_line[i] = L(x_line[i], x_values, y_values)
x_max = find_max(x_values, y_values)
gamma = find_half_max_width(x_values, y_values)


plt.figure()
plt.scatter(x_values, y_values, label="Data")
plt.plot(x_line, y_line, label="Lagrange")
plt.legend()
plt.title("E_0 = {:.2f}, Gamma = {:.2f}".format(x_max, gamma))
plt.xlabel("Energy")
plt.ylabel("Cross Section")
plt.savefig("ajuste_lagrange.png")    
