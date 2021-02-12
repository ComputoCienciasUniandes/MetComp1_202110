import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv("Cars93.csv")

columnas = ['Price', 'RPM', 'Fuel.tank.capacity', 'Width', 'Length']

plt.figure(figsize=(12,18))

i = 0 
for columna in columnas:
    data = datos[columna]

    plt.subplot(len(columnas), 2, 2*i+1)
    plt.plot(np.sort(data), np.linspace(1/len(data),1,len(data)))
    plt.xlabel(columna)
    plt.ylabel('Distribición Acumulada')

    plt.subplot(len(columnas), 2, 2*i+2)
    plt.hist(data, label="{:.2f} +/- {:.2f}".format(data.mean(), data.std()))
    i = i+1
    plt.legend()
    plt.xlabel(columna)
    plt.ylabel('Histograma')
    
plt.savefig("resumen.png")
