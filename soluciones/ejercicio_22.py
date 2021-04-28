import numpy as np
import matplotlib.pyplot as plt


# Soluciones a los ejercicios de la seccion 6.6.3 (Implementation:
# 10-D Monte Carlo Integration)  
# del libro A Survey of Computational Physics Introductory Computational Science
# de Landau, Paez, Bordeianu (Python Multimodal eTextBook Beta4.0)

# Use a built-in random-number generator to perform the 10-D Monte
# Carlo integration in (6.50). 
def integral(dim=10, n_points=100):
    x = np.random.random((dim, n_points))
    x_sum = np.sum(x, axis=0)
    x_sum = np.average(x_sum**2)
    return x_sum

# 1. Conduct 16 trials and take the average as your answer.
def mean_integral(n_trial=16, dim=10, n_points=100):
    x = 0
    for i in range(n_trial):
        x +=  integral(dim=dim, n_points=n_points)
    x = x/n_trial
    return x

# 2. Try sample sizes of N = 2,4,8,...,8192.
def integra_montecarlo():
    N = 2**np.arange(1,14)
    analitico = 155.0/6.0
    error = []
    for n in N:
        error.append(np.abs(analitico-mean_integral(n_points=n))/analitico)

#3. Plot the error versus 1/sqrt(N) and see if linear behavior occurs.
    plt.figure()
    plt.plot(1/np.sqrt(N), error)
    plt.loglog()
    plt.title("$\int_0^{1} dx_1 \ldots \int_0^1 dx_{10} (x_1+\cdots x_{10})^2 $")
    plt.ylabel("|error|")
    plt.xlabel("1/$\sqrt{N}$")
    plt.savefig("error_integral_10D.png")

