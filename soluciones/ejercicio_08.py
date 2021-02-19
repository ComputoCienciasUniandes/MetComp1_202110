
# El cancer de prostata es uno de los tipos mas comunes de cancer en hombres.
# Para saber si alguien tiene cancer de prostata los doctores hacen un
# examen que mide  los niveles de la proteina PSA (prostate specific
# antigen) que es producida unicamente por la prostata. 
# Niveles altos de PSA se correlacionan con la presencia de cancer.
# Sin embargo, la probabilidad de que una persona sin cancer tenga un
# nivel elevado de PSA es de 0.135, mientras que la probabilidad de
# que alguien con cancer tenga un nivel elevado de PSA es de 0.268.
# Si basado en otros factores se cree que una persona tiene
# probabilidad 0.7 de tener este cancer. Calcule:
# a) La probabilidad de tener cancer dado que hay niveles elevedos de
# PSA.
# b) La probabiidad de tener cancer dado que hay niveles bajos de PSA.

# Escriba una función de python llamada probabilidad_psa_cancer que
# soluciona el problema mencionado anteriormente a traves de un metodo montecarlo

# La solución se debe hacer para el caso general donde:

# - la probabilidad de tener PSA alto dado que no tiene cancer es la variable p_alto_PSA_dado_no_cancer, 

# - la probabilidad de tener PSA alto dado que tiene cancer es la variable p_alto_PSA_dado_cancer,

#- la probabilidad de tener cancer es la variable p_cancer.

#A la función probabilidad_psa_cancer deben entrar las tres variables
#anteriores en el orden p_alto_PSA_dado_no_cancer,
#p_alto_PSA_dado_cancer, p_cancer 

# La función debe devolver dos números: la probabilidad de cancer dado
# PSA alto y la probabilidad de cancer dado PSA bajo. 

#La función debe estar en un archivo llamado
#"ApellidoNombre_MagistralEjercicio08.py" donde Apellido y Nombre debe
#reemplazarlos con su apellido y nombre.  Suba ese archivo como
#respuesta a esta actividad. 

# Al ejecutar "python ApellidoNombre_MagistralEjercicio08.py" no se
# debe producir ningún error. Se considera que el programa no corre si
# se demora más de un minuto en producir la respuesta. Cuando
# califiquemos vamos a llamar tres veces la función y la respuesta
# debe ser la misma hasta la segunda cifra decimal. 

# Solamente puede utilizar las funciones y métodos vistas en clase
# (videos o clases sincrónicas, o que ya se encuentren en el
# repositorio) . 

import numpy as np

def probabilidad_psa_cancer(p_alto_PSA_dado_no_cancer, p_alto_PSA_dado_cancer, p_cancer, n_individuos=100):
    cancer_positivo = 0
    cancer_negativo = 1
    cancer = np.random.random(n_individuos)

    ii_cancer = cancer < p_cancer
    cancer[ii_cancer] = cancer_positivo
    cancer[~ii_cancer] = cancer_negativo


    PSA_alto = 0
    PSA_bajo = 1
    psa = np.random.random(n_individuos)

    ii_psa_alto_y_cancer = ii_cancer & (psa<p_alto_PSA_dado_cancer)
    ii_psa_bajo_y_cancer = ii_cancer & ~(psa<p_alto_PSA_dado_cancer)
    ii_psa_alto_y_no_cancer = ~ii_cancer & (psa<p_alto_PSA_dado_no_cancer)
    ii_psa_bajo_y_no_cancer = ~ii_cancer & ~(psa<p_alto_PSA_dado_no_cancer)

    psa[ii_psa_alto_y_cancer] = PSA_alto
    psa[ii_psa_bajo_y_cancer] = PSA_bajo
    psa[ii_psa_alto_y_no_cancer] = PSA_alto
    psa[ii_psa_bajo_y_no_cancer] = PSA_bajo


    # Probabilidad de tener cancer dado que el PSA es alto
    ii_cancer_y_PSA_alto = (cancer==cancer_positivo) & (psa==PSA_alto)

    if len(psa[psa==PSA_alto]):
        a =  len(cancer[ii_cancer_y_PSA_alto])/len(psa[psa==PSA_alto])
    else:
        a = 0

    # Probabilidad de tener cancer dado que el PSA es bajo
    ii_cancer_y_PSA_bajo = (cancer==cancer_positivo) & (psa==PSA_bajo)
    if len(psa[psa==PSA_bajo])>0:
        b =  len(cancer[ii_cancer_y_PSA_bajo])/len(psa[psa==PSA_bajo])
    else:
        b = 0

    return a, b


import matplotlib.pyplot as plt

lista_a = []
lista_b = []

for m in range(100000):
    a, b =  probabilidad_psa_cancer(0.2, 0.4, 0.6, n_individuos=10)
    lista_a.append(a)
    lista_b.append(b)

plt.figure()
plt.hist(lista_a, bins=9, alpha=1.0)
plt.title("N={}, M={}. m={:.2f} s={:.2f}".format(10,100000, np.mean(lista_a), np.std(lista_a)))
plt.xlabel("P(cancer | PSA alto)")
plt.ylabel("Histograma")
plt.xlim([0,1])
plt.savefig("proba_montecarlo.png")
