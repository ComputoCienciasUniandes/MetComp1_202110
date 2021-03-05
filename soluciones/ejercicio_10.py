import numpy as np

def realization(p_1, p_2, n_trials):
    p_3 = 1.0 - p_1 - p_2

    outcomes = np.random.random(n_trials)

    ii_1 = outcomes<=p_1
    ii_2 = (outcomes>p_1) & (outcomes<=(p_1+p_2))
    ii_3 = (~ii_1) & (~ii_2)

    outcomes[ii_1] = 1
    outcomes[ii_2] = 2
    outcomes[ii_3] = 3

    N_1 = len(outcomes[outcomes==1])
    N_2 = len(outcomes[outcomes==2])

    return N_1, N_2

def joint_probability(p_1, p_2, n_trials, n_iteraciones):
    proba = np.zeros([n_trials+1, n_trials+1])
    for i in range(n_iteraciones):
        N_1, N_2 = realization(p_1, p_2, n_trials)
        proba[N_1, N_2] += 1
    proba /= n_iteraciones
    return proba

def covarianza(p_1, p_2, n_total):
    p = joint_probability(p_1, p_2, n_total, 100000)

    #valor esperado de N1*N2
    E_N1_N2 = 0.0
    for i in range(n_total+1):
        for j in range(n_total+1):
            E_N1_N2 += p[i,j] * i * j

    # valor esperado de N1
    E_N1 = 0.0
    for i in range(n_total+1):
        p_i = 0.0 
        for j in range(n_total+1):
            p_i += p[i,j]

        E_N1 += p_i * i

    # valor esperado de N2
    E_N2 = 0.0
    for j in range(n_total+1):
        p_j = 0.0 
        for i in range(n_total+1):
            p_j += p[i,j]

        E_N2 += p_j * j

    return E_N1_N2  - E_N1 * E_N2 

