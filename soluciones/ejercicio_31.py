import numpy as np
import matplotlib.pyplot as plt


# 42. Ten pregnant women were given an injection of pitocin to induce labor. Their
# systolic blood pressures immediately before and after the injection were:

before = [134, 122, 132, 130, 128, 140, 118, 127, 125, 142]
after = [140, 130, 135, 126, 134, 138, 124, 126, 132, 144]

# vamos a implementar un metodo de shuffling. para hacer esto la hipotesis nula
# es que ambas series de datos vienen de la misma distribucion. 
# la estadistica que vamos a calcular es el promedio de las diferencias.

n_mc = 10000
n = len(before)
mu_mc = np.zeros(n_mc)
datos = np.array(before+after)
for i in range(n_mc):
    np.random.shuffle(datos)
    new_before = datos[:n]
    new_after = datos[n:]
    mu_mc[i] = np.mean(new_before - new_after)

mu = np.mean(np.array(before) - np.array(after))
p_value = np.count_nonzero(np.abs(mu_mc)>np.abs(mu))/n_mc
if p_value<0.05:
    H = 'SI'
else:
    H = 'NO'
print('Problema 42. p-value: {:.2f}. La droga {} tiene un efecto en la presion'.format(p_value, H))

plt.figure()
plt.hist(mu_mc, bins=20)
plt.axvline(mu, color='red')
plt.savefig("tmp_42.png")

# 43. A question of medical importance is whether jogging leads to a
#reduction in one’s pulse rate. To test this hypothesis, 8 nonjogging
#volunteers agreed to begin a 1-month jogging program. After the month
#their pulse rates were determined and compared with their earlier
#values. If the data are as follows, can we conclude that jogging has
#had an effect on the pulse rates?  


before = [74,86,98,102,78,84,79,70] 
after = [70,85,90,110,71,80,69,74]

# vamos a implementar un metodo de shuffling. para hacer esto la hipotesis nula
# es que ambas series de datos vienen de la misma distribucion. 
# la estadistica que vamos a calcular es el promedio de las diferencias

n_mc = 10000
n = len(before)
mu_mc = np.zeros(n_mc)
datos = np.array(before+after)
for i in range(n_mc):
    np.random.shuffle(datos)
    new_before = datos[:n]
    new_after = datos[n:]
    mu_mc[i] = np.mean(new_before - new_after)

mu = np.mean(np.array(before) - np.array(after))
p_value = np.count_nonzero(np.abs(mu_mc)>np.abs(mu))/n_mc
if p_value<0.05:
    H = 'SI'
else:
    H = 'NO'
print('Problema 43. p-value: {:.2f}. Correr {} tiene un efecto en el pulso'.format(p_value, H))

plt.figure()
plt.hist(mu_mc, bins=20)
plt.axvline(mu, color='red')
plt.savefig("tmp_43.png")

#67. In the
#nineteenseventies,theU.S.VeteransAdministration(Murphy,1977)con-
#ducted an experiment comparing coronary artery bypass surgery with
#medical drug therapy as treatments for coronary artery disease. The
#experiment involved 596 patients, of whom 286 were randomly assigned
#to receive surgery, with the remaining 310 assigned to drug
#therapy. A total of 252 of those receiving surgery, and a total of
#270 of those receiving drug therapy were still alive three years
#after  Use these data to test the hypothesis that the survival
#probabilities are equal.


N_cirugia = 286
N_droga = 310
N_sobrevive_cirugia = 252
N_sobrevive_droga = 270

# Vamos a tomar como la probabilidad de supervivencia global
# p_sobre = (N_sobrevive_cirugia+N_sobreviev_droga)/(N_cirugia+N_droga). 
# Si las probabilidades de supervivencia son iguales, entonce la
# p_sobrevive para cualquiera de los casos (cirugia, droga) debe ser 
# consistente con p_sobre.
# Vamos a generar entonces numeros aleatorios con la probabilidad
# p_sobre y compararlo con el N_sobrevive_cirugia observado.


n_mc  = 10000
p_sobre = (N_sobrevive_cirugia + N_sobrevive_droga)/(N_cirugia + N_droga)

n_sobre_mc = np.zeros(n_mc)
for i in range(n_mc):
    r = np.random.random(N_cirugia) 
    n_sobre_mc[i] = np.count_nonzero(r<p_sobre)

delta = np.abs(np.mean(n_sobre_mc) - N_sobrevive_cirugia)
p_value = np.count_nonzero(np.abs(n_sobre_mc - np.mean(n_sobre_mc))>delta)/n_mc

if p_value<0.05:
    H = 'NO'
else:
    H = 'SI'
print('Problema 67. p-value: {:.2f}. Las probabilidades de supervivencia {} son iguales.'.format(p_value, H))

plt.figure()
plt.hist(n_sobre_mc, bins=20)
plt.axvline(N_sobrevive_cirugia, color='red')
plt.savefig("tmp_67.png")


#69 The following table gives the number
#of fatal accidents o fU.S.commercialairline carriers in the 16 years from
#1980 to 1995. Do these data disprove, at the 5 percent level of
#significance, the hypothesis that the mean number of accidents in a
#year is greater than or equal to 4.5? What is the p-value? (Hint:
#First formulate a model for the number of accidents.) 

accidentes = [0, 4, 4, 4, 1, 4, 2, 4, 3, 11, 6, 4, 4, 1, 4, 2]

# Se espera que el numero de accidentes anuales siga una distribucion 
# possoniana de parametro lambda. Dado que par esta distribucion el 
# valor medio es lambda, entonces vamos a comparar la suma total del 
# numero de accidentes observados con el numero total de accidentes
# esperados si lambda fuera 4.5. 

n_mc = 10000
n_acc = len(accidentes)
n_tot_acc_mc = np.zeros(n_mc)

for i in range(n_mc):
    n_tot_acc_mc[i] = np.sum(np.random.poisson(lam=4.5, size=n_acc))


p_1 = np.count_nonzero(n_tot_acc_mc<np.sum(accidentes))/n_mc
p_2 = np.count_nonzero(n_tot_acc_mc>np.sum(accidentes))/n_mc
p_value = 2.0*np.min([p_1, p_2])
                           

if p_value<0.05:
    H = 'NO'
else:
    H = 'SI'
print('Problema 69. p-value: {:.2f}. El numero promedio de accidentes {} es mayor o igual que 4.5.'.format(p_value, H))

plt.figure()
plt.hist(n_tot_acc_mc, bins=20)
plt.axvline(np.sum(accidentes), color='red')
plt.savefig("tmp_69.png")


