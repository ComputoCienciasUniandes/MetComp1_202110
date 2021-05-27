import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/MetComp1_202110/main/ejemplos/world_pop.csv")

df = df.loc[df['Entity'] == 'Our World In Data']
data = df[df['Year'].between(700, 1900)]
year = data['Year'].to_numpy()
population = data['World Population'].to_numpy()

def poly_fit(x, y, grado):
  x = np.asarray(x).reshape(-1,1)
  y = np.asarray(y).reshape(-1,1)
  pts = len(x)
  P = np.concatenate([np.ones([pts,1]),x], axis=1)
  for i in range(1,grado):
    P = np.concatenate([P, (P[:,-1]*P[:,1]).reshape(-1,1)], axis=1)
  v = ((np.linalg.inv(P.T @ P) @ P.T) @ y).flatten()
  return v[::-1]

def graficar_ajuste_pol(years,population,coeficientes):
  x = np.linspace(years[0]-40, years[-1]+10,num=200)
  p = np.poly1d(coeficientes)
  plt.figure(figsize=(9,5))
  plt.plot(years, population, 'o')
  plt.plot(x, p(x), 'r', linewidth=2)
  plt.xlabel('Year')
  plt.ylabel('World population')
  plt.show()
    
coefs = poly_fit(year, population, 4)

x = np.linspace(year[0]-40, year[-1]+10,num=200)
p = np.poly1d(coefs)
plt.figure(figsize=(9,5))
plt.plot(year, population, 'o')
plt.plot(x, p(x), 'r', linewidth=2)
plt.xlabel('Year')
plt.ylabel('World population')
plt.savefig("UsecheDiego_diagram.png")
print(f"coefs = {coefs}")