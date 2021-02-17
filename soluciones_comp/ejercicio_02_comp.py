import numpy as np 
import matplotlib.pyplot as plt

lanzamientos = np.random.randint(1, 7, 300)

plt.hist(lanzamientos, bins = np.linspace(0.5, 6.5 , 7), histtype='bar', ec='black')
plt.xlabel("Result of the dice")
plt.ylabel("counts")
plt.savefig('histograma.png')

print(f"average = {lanzamientos.mean()}, std = {lanzamientos.std()}")