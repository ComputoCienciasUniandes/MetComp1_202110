import numpy as np
import matplotlib.pyplot as plt

def histograma_compara(n_personas):
    n_gripas_normal = np.random.poisson(3.0, size=n_personas)        
    n_gripas_medicamento = np.random.poisson(2.0, size=n_personas)

    n_sin_resultados = int(n_personas*0.25)
    n_gripas_medicamento[:n_sin_resultados] = n_gripas_normal[:n_sin_resultados]
    
    plt.figure()
    plt.hist(n_gripas_normal+0.25, bins=np.arange(0,np.max(n_gripas_normal)+1, 0.25),
    rwidth=0.75, label='Sin medicamento')
    plt.hist(n_gripas_medicamento, bins=np.arange(0,np.max(n_gripas_normal)+1, 0.25),
    rwidth=0.75, label='Con medicamento')
    plt.xlabel("N gripas")
    plt.ylabel("N personas ")
    plt.legend()
    plt.savefig("gripas.png")

#histograma_compara(10000000)

