import numpy as np
import matplotlib.pyplot as plt


# Soluciones a los ejercicios de la seccion 6.2.5 
# del libro A Survey of Computational Physics Introductory Computational Science
# de Landau, Paez, Bordeianu (Python Multimodal eTextBook Beta4.0)

#1. Write a double-precision program to integrate an arbitrary function numerically 
# using the trapezoid rule, the Simpson rule, and Gaussian quadrature.
def integral(f, a, b, n_points=10, metodo="trapecio"):
    # Genera siempre un numero impar de puntos
    if n_points%2 == 0:
        n_points = n_points + 1

    if metodo=="trapecio":
        x = np.linspace(a, b, n_points)
        h = x[1] - x[0]
        w = np.ones(n_points) * h
        w[0] = h/2
        w[-1] = h/2
    elif metodo=="simpson":
        x = np.linspace(a, b, n_points)
        h = x[1] - x[0]
        w = np.ones(n_points) 
        ii = np.arange(n_points)
        w[ii%2!=0] = 4.0*h/3.0
        w[ii%2==0] = 2.0*h/3.0
        w[0] = h/3
        w[-1] = h/3
    elif metodo=="cuadratura":
        y, wprime = np.polynomial.legendre.leggauss(n_points)
        x = 0.5*(b+a) + 0.5*(b-a)*y
        w = 0.5*(b-a)*wprime
    else:
        print('metodo no implementado')
        x = np.zeros(n_points)
        y = np.zeros(n_points)

    return np.sum(f(x)*w)

def func(x):
    return np.cos(x)

def error(x):
    return np.abs(1-x)

# 2 Compute the relative error (epsilon=abs(numerical-exact)/exact) in each case. 
# Present your data in tabular form for N=2,10,20,40,80,160

def integra():
    N = [2,10,20,40,80,160]
    print("Primera Parte")
    out = open("/tmp/tabla_resultados.dat", "w")
    print("# N\t e_T\t e_S \t e_G")
    for n_points in N:
        a = integral(func, 0, np.pi/2, n_points=n_points, metodo="trapecio")
        b = integral(func, 0, np.pi/2, n_points=n_points, metodo="simpson")
        c = integral(func, 0, np.pi/2, n_points=n_points, metodo="cuadratura")
        print("{:d}\t {:.1e} {:.1e} {:.1e}".format(n_points, error(a), error(b), error(c)))
        out.write("{:d}\t {:.1e} {:.1e} {:.1e}\n".format(n_points, error(a), error(b), error(c)))
    out.close()
    print("")

    # 3 Make a log-log plot of relative error versus N
    data = np.loadtxt("/tmp/tabla_resultados.dat")
    plt.figure()
    plt.plot(data[:,0], data[:,1], label="Trapecio")
    plt.plot(data[:,0], data[:,2], label="Simpson")
    plt.plot(data[:,0], data[:,3], label="Cuadratura")

    plt.xlabel('N')
    plt.ylabel('|error|')
    plt.loglog()
    plt.legend()
    plt.savefig("error_loglogplot.png")


    # 4. Use your plot or table to estimate the power-law dependence of the error on N and
# to determine the nuber of decimal places of precision.

    for i,m in zip([1,2,3],["Trapecio", "Simpson", "Cuadratura"]):
        power_law = (np.log(data[2,i]) - np.log(data[0,i]))/(np.log(data[2,0]) - np.log(data[0,0]))
        decimal_places = -np.log10(data[-1,i])
        print("Metodo {}".format(m))    
        print("\t Power Law: {:.1f}".format(power_law))
        print("\t Decimal Places: {:d}".format(int(decimal_places)))

