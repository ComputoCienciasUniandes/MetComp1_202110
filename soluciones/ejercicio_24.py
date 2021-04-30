import numpy as np
import matplotlib.pyplot as plt

def func(v0, d, h, theta):
    g = 10.0
    x = np.tan(theta)*d - 0.5*g*(d/(v0*np.cos(theta)))**2 - h
    return x

def deriva_func(v0, d, h, theta):
    delta_theta = 1E-4
    d = (func(v0, d, h, theta+delta_theta/2) - 
         func(v0, d, h, theta-delta_theta/2))/delta_theta
    return d

def encuentra_theta(v0,d,h, theta):
    N = 0
    N_iter_max = 100
    epsilon =1E-10
    while (np.abs(func(v0,d,h,theta))>epsilon) and N<N_iter_max:
        theta = theta - func(v0,d,h,theta)/deriva_func(v0,d,h,theta)
        N = N+1
    if N==N_iter_max:
        theta = -1.0
    return theta

def plot_solucion(v0,d,h, theta):
    g =10.0
    t_max = d/(v0*np.cos(theta))
    t = np.linspace(0,t_max, 100)
    x = v0*np.cos(theta)*t
    y = v0*np.sin(theta)*t - 0.5*g*t**2
    plt.plot(x, y, label='theta={:.2f} grados'.format((theta*180.0/np.pi)%180.0))
    plt.scatter(d, h, color='black')
    plt.xlim([0,d*1.1])
    plt.ylim([0,y.max()*1.1])
    plt.title("v0 = {:.2f}m/s, d = {:.2f}m, h={:.2f}m".format(
            v0, d, h))
    plt.xlabel("x [metros]")
    plt.ylabel("y [metros]")
    plt.legend()

def encuentra_angulo(v0, d, h):
    theta_1 = encuentra_theta(v0,d,h, 1E-5)
    theta_2 = encuentra_theta(v0,d,h, np.pi/2.0-1E-5)

    plt.figure()    
    if theta_1>0 and theta_2>0:
        plot_solucion(v0,d,h,theta_1)
        plot_solucion(v0,d,h,theta_2)
    else:
        plt.scatter(d,h)
        plt.title("no hay solucion")
    plt.savefig("parabola.png")


#encuentra_angulo(100,50,120)
