import numpy as np
import matplotlib.pyplot as plt

def probabilidad_operacion(vida_media, vida_std, n_componentes, vida_total):
    n_pasa = 0
    n_iteraciones = 10000
    for i in range(n_iteraciones):
        comps = np.random.normal(loc=vida_media, scale=vida_std,
                                 size=n_componentes)
        comps[comps<0] = 0
        vida = np.sum(comps)
        if vida > vida_total:
            n_pasa += 1

    return n_pasa/n_iteraciones

