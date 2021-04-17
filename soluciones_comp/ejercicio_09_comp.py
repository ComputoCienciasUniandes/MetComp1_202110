import numpy as np
from scipy.stats import norm

miu = 8.2
sigma = 0.02
sample = [8.18, 8.17, 8.16, 8.15, 8.17, 8.21, 8.22, 8.16, 8.19, 8.18]
n_sample = len(sample)
miu_sample = sum(sample)/n_sample

p_value = round(2* norm.cdf(miu_sample, loc=miu, scale=sigma/np.sqrt(n_sample)), 3)
conclusion = "Dado que el p_value es menor que el nivel de significancia de 0.5, el promedio de la muestra no corresponde a la distribucion."

print(f"p value = {p_value}, la conclusion es:  {conclusion}")