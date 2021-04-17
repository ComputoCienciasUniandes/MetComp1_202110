import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm 

montecarlo_counts = 50000

steps = np.zeros((montecarlo_counts, 100))
for i in range(montecarlo_counts):
    for j in range(100):
        random_num = np.random.rand()
        if (random_num<0.1):
            steps[i, j] = 2
        elif (random_num>0.8):
            steps[i, j] = -1
        else:
            steps[i, j] = 1

total_steps = steps.sum(axis=1)

ev_analitical = 0.7 * 1 + 0.2 * (-1) + 0.1 * 2
print("El valor esperado analiticamente es:", ev_analitical)

mean, std = norm.fit(total_steps)
x = np.linspace(0, 200, 201)
y = norm.pdf(x, mean, std)
plt.hist(total_steps, bins=np.linspace(0, 200, 201), density=True)
plt.xlabel("Total Steps")
plt.ylabel("Probability")
plt.plot(x, y)
plt.savefig("UsecheDiego_Ejercicio7.png")
