import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://raw.githubusercontent.com/ComputoCienciasUniandes/MetComp1_202110/main/ejemplos/linear.csv")
x = np.array(df["x"])
y = np.array(df["y"])
mc_counts = 10000
x_prueba = 5

def error(x, y, x_prueba, mc_counts):

    n = len(x)
    bs = np.zeros(mc_counts)
    ms = np.zeros(mc_counts)
    ys = np.zeros(mc_counts)

    for i in range(mc_counts):
        indices_sr = np.random.randint(0, n,  n)
        x_sr = x[indices_sr].reshape(-1, 1)
        y_sr = y[indices_sr].reshape(-1, 1)
        reg = LinearRegression().fit(x_sr, y_sr)
        bs[i] = reg.intercept_
        ms[i] = reg.coef_
        ys[i] = reg.predict(np.array([[x_prueba]]))

    return bs.mean(), bs.std(), ms.mean(), ms.std(),  ys.mean(), ys.std()


a, b, c, d, e, f = np.round(error(x, y, x_prueba, mc_counts), 4)
print(f"intercept = {a} pm {b}, slope = {c} pm {d}, y = {e} pm {f}")