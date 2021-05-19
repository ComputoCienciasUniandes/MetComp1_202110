import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def grafica_direcciones_pca(datos_x, datos_y):
    data = np.array([datos_x, datos_y])
    data[0,:] = data[0,:]-np.mean(data[0,:])
    data[1,:] = data[1,:]-np.mean(data[1,:])
    cov = np.cov(data)
    values, vectors = np.linalg.eig(cov)
    

    plt.figure()
    fig, ax = plt.subplots()
    for i in range(2):
        x = np.linspace(np.min(data[0,:]), np.max(data[0,:]), 100)
        y = -vectors[0,i]/(vectors[1,i])*x
        plt.plot(x,y)

    plt.scatter(data[0,:], data[1,:])
    plt.xlim(np.min(data[0,:]), np.max(data[0,:]))
    plt.ylim(np.min(data[1,:]), np.max(data[1,:]))
    plt.xlabel('X-avg(X)')
    plt.ylabel('Y-avg(Y)')
    ax.set_aspect('equal')
    plt.savefig("direcciones.png", bbox_inches='tight')


#datos_x =[ 0.49416816,  0.46465438, -1.73694346, -0.12428063,  2.06799947,
#        2.0545997 ,  2.48939343, -0.81445802, -1.53473612, -1.75149721,
#       -3.88090413, -0.98148244,  0.266375  , -1.48104676, -0.28795435,
#        0.15063483,  0.55152368,  1.53011185, -1.46317706,  0.1278654 ]
#datos_y = [ 1.82086909e+00, -1.66252722e+00, -1.01376736e-03,  1.21411624e+00,
#       -1.22597662e+00, -7.48611751e-01, -9.38910856e-01,  8.23553713e-02,
#        5.61304037e-01,  1.41525966e+00, -2.53389854e-01, -2.19081552e-01,
#       -1.47090740e-01,  3.45632163e-01, -9.88379478e-02,  1.43713407e+00,
#       -4.64200400e-01, -9.67044402e-01,  1.01327199e+00,  5.21229231e-01]

#grafica_direcciones_pca(datos_x, datos_y)
