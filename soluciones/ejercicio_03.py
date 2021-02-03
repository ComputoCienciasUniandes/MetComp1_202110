#Escriba una función llamada juega_dados que toma como entrada un primer argumento llamado n_lanzamientos (entero), un segundo argumento llamado n_dados (entero) y un tercer argumento llamado n_caras (entero). 

#La función debe repetir n_lanzamientos veces las siguientes operaciones:

#A) Generar n_dados números aleatorios. Cada número aleatorio debe ser un entero elegido entre 1 y n_caras (inclusive).

#B) De los n_dados números aleatorios generados tomar los primeros n_dados-1 y sumarlos. Luego multiplicar el resultado de la suma por el número aleatorio que no fue incluido en la suma.

#C) Guardar el número resultante de las operaciones de B) dentro de una lista.

#Luego de terminar estas iteraciones la función debe devolver la lista de enteros resultantes en el item C). Los procedimientos anteriores deben funcionar para valores de los parámetros de entrada que sean mayores o iguales a 2.

#Solamente son permitidas las funciones y métodos que aparezcan en los videos vistos hasta ahora en el curso. 

#El programa debe estar en un archivo llamado "ApellidoNombre_Ejercicio03.py" donde Apellido y Nombre debe reemplazarlos con su apellido y nombre. El archivo solamente debe incluir los imports necesarios y la función pedida. Suba ese archivo como respuesta a esta actividad.

#Al ejecutar "python ApellidoNombre_Ejercicio03.py" no se debe producir ningún error, nada se debe imprimir en pantalla y ningún archivo debe ser creado por el programa.

import random

def juega_dados(n_lanzamientos, n_dados, n_caras):
    a = [0]*n_lanzamientos
    for i in range(n_lanzamientos):

        dados = [0]*n_dados
        for j in range(n_dados):
            dados[j] = int(random.random()*n_caras + 1)
        
        for j in range(n_dados-1):
           a[i] = a[i] + dados[j]
        a[i] = a[i]*dados[-1]

    return a

#import numpy as np
#l = juega_dados(100000,2,6)
#print(np.mean(l), np.std(l))

