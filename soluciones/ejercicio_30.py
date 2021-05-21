import numpy as np
import matplotlib.pyplot as plt

def grafica_proyeccion_pca(datos_entrada):
    # estandarizacion
    n_cols = len(datos_entrada[0,:])
    for i in range(n_cols):
        datos_entrada[:,i] = (datos_entrada[:,i] - np.mean(datos_entrada[:,i]))/np.std(datos_entrada[:,i])
    
    cov = np.cov(datos_entrada.T) # covarianza

    valores, vectores = np.linalg.eig(cov) # autovalores

    orden_valores = np.argsort(valores)[::-1] # indices de los autovalores de mayor a menor
    
    new_data = datos_entrada @ vectores # esto hace el cambio de base al nuevo sistema de los autovectores

    plt.scatter(new_data[:,orden_valores[0]], new_data[:,orden_valores[1]]) # scatter plot

    plt.xlabel("Primera Componente Principal")
    plt.ylabel("Segunda Componente Principal")
    plt.savefig("proyeccion.png")


#datos = np.loadtxt("datos.dat")
#grafica_proyeccion_pca(datos)
