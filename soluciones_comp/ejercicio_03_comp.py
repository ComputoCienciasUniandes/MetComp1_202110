import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

world_data = pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/MetComp1_202110/main/ejemplos/world.csv")


options = ['LATIN AMER. & CARIB    ']
columns = ['Region', 'Population']  
# selecting rows based on condition 
population_ds = world_data[world_data['Region'].isin(options)].loc[:, columns]

fig, ax = plt.subplots()
population_ds.hist(bins=20, ax=ax)
plt.xlabel("Population in millions")
plt.ylabel("Country Counts")
plt.title("Distribution of countries by population in LA")
fig.savefig('ejercicio3_imagen.png')