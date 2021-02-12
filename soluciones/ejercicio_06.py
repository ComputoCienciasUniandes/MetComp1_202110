import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv("world.csv")


# Desigualdad de Chebyshev
x = np.log10(datos['Population'])
k = 1.5
s = x.std()
m = x.mean()

# valores alrededor de la media
ii = np.abs(x-m) < k*s
n_in = len(x[ii])

# valores en la cola de la derecha
ii = x-m > k*s
n_one_side = len(x[ii])
n = len(x)

#Cotas de la desigualdad
f_che = 1.0 - 1/(k*k)
f_che_one_side = 1/(1+k**2)

titulo = "m = {:.2f}, s={:.2f}, k={:.2f}\n".format(m, s, k) 
titulo += "N(m+/-ks)/n = {:.2f} ".format(n_in/n)
titulo += "vs. Chebyshev: N(m+/-ks)/n > {:.2f}\n".format(f_che)
titulo += "N(k)/n = {:.2f}, ".format(n_one_side/n)
titulo += "vs. One Side Chebyshev: N(k)/n < {:.2f}".format(f_che_one_side)


plt.figure(figsize=(8,6))
plt.hist(x, bins=20)
plt.title(titulo)
plt.xlabel('Log10 Population')
plt.ylabel('Histograma')
plt.savefig("distribucion.png")

# Correlaciones

def coef_corr(x, y):
    n = len(x)
    r = np.sum((x-x.mean())*(y-y.mean()))/((n-1) * x.std() * y.std())
    return r

plt.figure(figsize=(5,5))

r = coef_corr(np.log10(datos['Population']), np.log10(datos['Area (sq. mi.)']))
plt.scatter(np.log10(datos['Population']), np.log10(datos['Area (sq. mi.)']), label="r={:.2f}".format(r))
plt.legend()
plt.xlabel("log10 Population")
plt.ylabel("log10 Area")

plt.savefig("correlaciones.png", bbox_inches='tight')
