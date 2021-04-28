import numpy as np
import matplotlib.pyplot as plt

# Ejercicio 1

def FD(f, x, h):
    return (f(x+h)-f(x))/h

def CD(f, x, h):
    return (f(x+h/2)-f(x-h/2))/h

def ED(f, x, h):
    return (4*CD(f, x, h/2)-CD(f, x, h))/3.0


def get_error(f, deriva_f_analitica, deriva_f_numerica, x):
    h_range = np.logspace(-15,-1, 200)
    analitica = deriva_f_analitica(x)
    error_range = np.abs((deriva_f_numerica(f, x, h_range) - analitica)/analitica)
    return h_range, error_range


def minus_sin(x):
    return -np.sin(x)

plt.figure(figsize=(15,10))

i = 1
ff = [np.exp, np.cos]
gg = [np.exp, minus_sin]
names = ["exp(x)", "cos(x)"]
xx = [0.1, 1.0, 100.0]

for f, g, n, in zip(ff, gg, names):
    for x in xx:
        plt.subplot(2,3,i)

        h, e = get_error(f, g, FD, x); plt.plot(h, e, label="FD", alpha=1.0)
        h, e = get_error(f, g, CD, x); plt.plot(h, e, label="CD", alpha=1.0)
        h, e = get_error(f, g, ED, x); plt.plot(h, e, label="ED", alpha=1.0)

        plt.title("f(x)={}, x={:.1f}".format(n,x))
        plt.xlim([1E-15,1E-1])
        plt.ylim([1E-15,1E-1])
        plt.loglog()
        plt.legend()
        plt.grid()
        plt.xlabel("h")
        plt.ylabel("|error primera derivada|")
        i += 1

plt.tight_layout()
plt.savefig("primera_derivada.png", bbox_inches='tight')

