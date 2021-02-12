# Tome como referencia los formatos del video del curso "Ejemplo - Gráfica de ciudades colombianas". 

#Escriba un programa de Python que:

#1. Tenga una función que se llama lee_datos que tiene como primer
#argumento la cadena de caracteres que representa el nombre del
#archivo con las coordenadas (con el mismo formato del video) y como
#segundo argumento la cadena de caracteres que representa el nombre
#del archivo con los nombres de las ciudades. La función debe devolver
#dos arrays de numpy, el primer array corresponde a las coordenadas y
#el segundo a los nombres de las ciudades.  

#2. Tenga una función que se llama genera_recorrido. Esta función
#tiene como argumento de entrada un array con nombres de ciudades. La
#función genera una lista aleatoria de n+1 enteros donde el primer y
#último elemento es el número 0. n es la longitud del array del nombre
#de ciudades. Los demás elementos de la lista deben incluir, en
#desorden, los números del 1 al n-1. En este lista el entero n va a
#representar a la ciudad n-esima en el array de entrada. Esta lista de
#enteros va a representar entonces un recorrido que empieza y termina
#en la primera ciudad de la lista y pasa por todas las ciudades. La
#función debe devolver la lista de n+1 enteros. 

#3. Tenga una función que se llama calcula_distancia. Esta función
#toma como primer argumento de entrada un array de coordenadas de
#ciudades, como segundo argumento un entero a, como tercer argumento
#un entero b. Los enteros representan las filas del array de
#coordenadas. La función deben calcular la distancia entre las dos
#ciudades representadas por los dos enteros a y b, dadas las
#coordenadas de entrada. La función debe devolver el valor de la
#distancia. Calcule esta distancia asumiendo que la Tierra es una
#esfera perfecta de radio 6400 km y que la medición se hace sobre el
#arco de longitud mínima sobre esa
#esfera https://www.johndcook.com/lat_long_details.html 

#4. Tenga una función que se llama calcula_distancia_total. Esta
#función toma como primer argumento de entrada un array de coordenadas
#de ciudades y como segundo argumento una lista con al menos dos
#enteros. Los enteros representan las filas del array de
#coordenadas. La función debe calcular la distancia total del
#recorrido representado por la lista de enteros de entrada. La función
#debe devolver la distancia total. 

#5. Tenga una función que se llama encuentra_recorrido. La
#función toma como primer argumento el nombre del archivo con
#coordenadas de ciudades y como segundo argumento el nombre del
#archivo con los nombres de las ciudades. La función utiliza las
#funciones de los cuatro puntos anteriores para generar 100 recorridos
#diferentes por las ciudades de los archivos de entrada. De esos 100
#recorridos encuentra el recorrido de menor longitud total y lo
#grafica en un plano Longitud-Latitud donde cada ciudad está
#representada por un punto y su nombre. Los pares de ciudades que
#están conectadas en el recorrido se representan por una línea recta
#en el plano Longitud-Latitud. La gráfica debe guardarse como
#"recorrido_mas_corto.png". La función devuelve None. 

#Pueden usar la función shuffle de numpy
#(https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.shuffle.html) 
#Solamente son permitidas las funciones y métodos que aparezcan en los
#videos vistos hasta ahora en el curso.  

#El programa debe estar en un archivo llamado
#"ApellidoNombre_Ejercicio04.py" donde Apellido y Nombre debe
#reemplazarlos con su apellido y nombre. El archivo solamente debe
#incluir los imports necesarios y las funciónes pedida. Suba ese
#archivo como respuesta a esta actividad. 

#Al ejecutar "python ApellidoNombre_Ejercicio04.py" no se
#debe producir ningún error, nada se debe imprimir en pantalla y
#ningún archivo debe ser creado por el programa. 

#Para calificar el ejercicios vamos a llamar la función
#encuentra_recorrido con dos nombres de archivos y contenidos
#diferentes a los del video. Esos archivos contienen los datos de al
#menos cuatro ciudades. 

import numpy as np
import matplotlib.pyplot as plt

def lee_datos(archivo_coordenadas, archivo_nombres):
    coordenadas = np.loadtxt(archivo_coordenadas, delimiter=",")
    nombres = np.loadtxt(archivo_nombres, dtype="str")
    return coordenadas, nombres

def genera_recorrido(nombres):
    n = len(nombres)
    r = np.arange(n-1)+1
    np.random.shuffle(r)
    r = [0] + list(r) + [0]
    return r

def calcula_distancia(coordenadas, a, b):
    latitud = coordenadas[:,0]
    longitud = coordenadas[:,1]

    phi = 90.0 - latitud
    theta = longitud
    theta[longitud<0] = 360.0 + longitud[longitud<0]

    phi = phi * np.pi/180.0
    theta = theta * np.pi/180.0

    psi = np.sin(phi[a])*np.sin(phi[b]) * np.cos(theta[a]-theta[b])
    psi = psi + np.cos(phi[a]) * np.cos(phi[b])
    psi = np.arccos(psi)
    rho = 6400.0
    return rho*psi

def calcula_distancia_total(coordenadas, recorrido):
    d = 0
    for i in range(len(recorrido)-1):
        d += calcula_distancia(coordenadas, recorrido[i], recorrido[i+1])
    return d

def encuentra_recorrido(archivo_coordenadas, archivo_nombres):
    coordenadas, nombres = lee_datos(archivo_coordenadas, archivo_nombres)

    d_min = 1E10
    r_min = []
    for i in range(100):
        r = genera_recorrido(nombres)
        d = calcula_distancia_total(coordenadas, r)
        if d < d_min:
            d_min = d
            r_min = r.copy()

    plt.figure()
    n_ciudades = len(nombres)
    for i in range(n_ciudades):
        plt.text(coordenadas[i,1], coordenadas[i,0], nombres[i])

    plt.scatter(coordenadas[r_min,1], coordenadas[r_min,0])
    plt.plot(coordenadas[r_min,1], coordenadas[r_min,0])

    plt.xlabel("Longitud [grados]")
    plt.ylabel("Latitud [grados]")
    plt.axis('equal')
    plt.savefig("recorrido_mas_corto.png")

    return None

