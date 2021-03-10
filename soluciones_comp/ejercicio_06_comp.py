import numpy as np 

X = np.random.poisson(6, 50000)

counts_seven = np.count_nonzero(X == 7)
prob_montecarlo = counts_seven / 50000
prob_poisson = np.exp(-6)*(6**7)/np.math.factorial(7)

print(f"Prob MC = {prob_montecarlo}, Prob Poisson = {prob_poisson}")