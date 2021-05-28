import numpy as np
import matplotlib.pyplot as plt

cigarette = np.array([2618, 2212, 2184, 2344, 2692, 
                      2206, 2914, 3034, 4240, 1400, 
                      2257])

bladder = np.array([4.09, 4.23, 2.91, 2.86, 4.69, 
                    3.72, 5.30, 3.46, 6.54, 3.31,
                    3.21])

lung = np.array([20.30, 16.59, 16.84, 17.71, 22.04,
                 14.20, 25.02, 25.88, 23.03, 12.01, 
                 20.74])

kidney = np.array([2.81, 2.90, 2.88, 2.13, 3.03,
                    3.54, 3.10, 4.32, 2.85, 2.20,
                    2.69])

leukemia = np.array([7.00, 7.69, 7.42, 6.41, 6.89, 
                     8.28, 7.23, 4.90, 6.67, 6.71, 
                     7.02])

def fit_and_plot(x, y, 
                 x_predict=0, 
                 x_name='X', 
                 y_name='Y', 
                 fig_name='so.png', 
                 plot_predict=True, 
                 p_value_slope=False):


    n_iterations = 1000
    n_intervalo = int(n_iterations/20)
    intercepto = np.ones(n_iterations)
    pendiente = np.ones(n_iterations)
    y_predict = np.ones(n_iterations)
    # bootstrapping the fit
    for i in range(n_iterations):
        ids = np.random.choice(np.arange(len(x)), len(x))
        p = np.polyfit(x[ids], y[ids], deg=1)
        pendiente[i] = p[0]
        intercepto[i] = p[1]
        y_predict[i] = p[0]*x_predict + p[1]
        
    # prediction and error bar
    y_mean = y_predict.mean()
    y_sigma = 1.645 * y_predict.std()


    # p-value for the slope being zero
    p_1 = np.count_nonzero(pendiente>0)
    p_2 = np.count_nonzero(pendiente<0)
    p_slope = 2.0*np.min([p_1, p_2])/n_iterations


    plt.figure()
    x_line = np.linspace(0.9*x.min(), 1.1*x.max(), 1000)
    y_line = intercepto.mean() + pendiente.mean()*x_line


    plt.scatter(x, y)
    plt.plot(x_line, y_line)

    if plot_predict:
        plt.errorbar(x_predict, y_mean, y_sigma, capsize=5.0, color='red')
        plt.scatter(x_predict, y_mean)


    if p_value_slope:
        plt.title('p_value={:.3f}'.format(p_slope))


    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.xlim(x_line.min(), x_line.max())
    plt.ylim(0.9*y.min(), 1.1*y.max())
    plt.savefig(fig_name)

fit_and_plot(cigarette, bladder, 2500, 
             x_name='Cigarretes per person', 
             y_name='bladder cancer deaths per 100k people', 
             fig_name="sol_19.png", 
             plot_predict=True)


fit_and_plot(cigarette, lung, 2500, 
             x_name='Cigarretes per person', 
             y_name='lung cancer deaths per 100k people', 
             fig_name="sol_20.png", 
             plot_predict=False,
             p_value_slope=True)

fit_and_plot(cigarette, kidney, 3400, 
             x_name='Cigarretes per person', 
             y_name='kidney cancer deaths per 100k people', 
             fig_name="sol_21.png", 
             plot_predict=True, 
             p_value_slope=True)

fit_and_plot(cigarette, leukemia, 2500, 
             x_name='Cigarretes per person', 
             y_name='leukemia deaths per 100k people', 
             fig_name="sol_22.png", 
             plot_predict=True, 
             p_value_slope=True)
