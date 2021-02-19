#Siguiendo las definiciones del ejercicio 34 del texto guía, utilice un método montecarlo para estimar la fracción de individuos de una población que tienen cancer dado que la medición da un PSA alto, donde las variables p_alto_PSA_dado_no_cancer=0.2, p_alto_PSA_dado_cancer=0.4 y p_cancer=0.6.

#Suponga además que la población tiene solamente N=10 individuos para los cuales se hace la medición de PSA alto. La estimación de P(cancer|PSA alto) se hace entonces sobre esa pequeña población. 

#Con un N tan pequeño, el valor de P(cancer|PSA alto) va a ser diferente para cada llamada del método montecarlo. Haga M=100000 llamadas del método montecarlo y grafique el histograma de P(cancer|PSA_alto) en un esquema como el que muestra la figura, donde m es el valor medio de los valores de P(cancer|PSA alto) y s es la desviación estándar de los valores de P(cancer|PSA alto) (los valores de m y s en la figura son ilustrativos).



#El programa debe estar en un archivo llamado "ApellidoNombre_Ejercicio08.py" donde Apellido y Nombre debe reemplazarlos con su apellido y nombre.  Suba ese archivo como respuesta a esta actividad.

#Al ejecutar "python ApellidoNombre_Ejercicio08.py" no se debe producir ningún error ni imprimir nada en pantalla. Solamente debe producir la gráfica solicitada con el nombre "proba_montecarlo.png". Se considera que el programa no corre si se demora más de 30 segundos en producir la gráfica. 

#Solamente puede utilizar las funciones y métodos vistos en clase (videos o clases sincrónicas, o que ya se encuentren en el repositorio) . En este caso no se puede usar while. 




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
