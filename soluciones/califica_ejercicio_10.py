import ejercicio_10 as e
import numpy as np

c = e.covarianza(0.5, 0.1, 10)
t = -0.5*0.1*10

if np.allclose(c, t, atol=0.1):
    print('bien')

c = e.covarianza(0.1, 0.8, 20)
t=-0.1*0.8*20

if np.allclose(c, t, atol=0.1):
    print('bien')

c = e.covarianza(0.3, 0.3, 50)
t = -0.3*0.3*50

if np.allclose(c, t, atol=0.1):
    print('bien')
