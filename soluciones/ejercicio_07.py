
# Un grupo de m gatos y n perros se encuentran alieados en un orden aleatorio.
# Es decir, cualquiera de las 50! permutaciones es igual de probable.

#Escriba un programa de python que genere una lista que representa a
#los 50 perros y gatos, y la reordene aleatoriamente usando
#np.random.shuffle() para calcular las siguientes probabilidades: 

#¿Cual es la probabilidad de que un perro se encuentre en la primera
#posición? 

#¿Cuál es la probabilidad de que un gato se encuentre en la primera
#posición? 

#¿Cuál es la probabilidad de que un perro y un gato se encuentren al
#tiempo en la primera y última posición, respectivamente?  

# El programa debe estar en un archivo llamado
# "ApellidoNombre_MagistralEjercicio07.py" donde Apellido y Nombre
# debe reemplazarlos con su apellido y nombre.  Suba ese archivo como
# respuesta a esta actividad.  
#

# Al ejecutar "python ApellidoNombre_MagistralEjercicio07.py" no se
# debe producir ningún error y solamente debe imprimir las tres
# probabilidades con dos cifras decimales. 
# Se considera que el programa no corre si se demora más de un minuto
# en producir la respuesta.
# Al correr tres veces el programa la respuesta debe ser la misma.


# Solamente puede utilizar las funciones y métodos vistas en clase
# (videos o clases sincrónicas, o que ya se encuentren en el repositorio) 
# Un grupo de m gatos y n perros se encuentran alieados en un orden aleatorio.
# Es decir, cualquiera de las 50! permutaciones es igual de probable.

#Escriba un programa de python que genere una lista que representa a
#los 50 perros y gatos, y la reordene aleatoriamente usando
#np.random.shuffle() para calcular las siguientes probabilidades: 

#¿Cual es la probabilidad de que un perro se encuentre en la primera
#posición? 

#¿Cuál es la probabilidad de que un gato se encuentre en la primera
#posición? 

#¿Cuál es la probabilidad de que un perro y un gato se encuentren al
#tiempo en la primera y última posición, respectivamente?  

# El programa debe estar en un archivo llamado
# "ApellidoNombre_MagistralEjercicio07.py" donde Apellido y Nombre
# debe reemplazarlos con su apellido y nombre.  Suba ese archivo como
# respuesta a esta actividad.  
#

# Al ejecutar "python ApellidoNombre_MagistralEjercicio07.py" no se
# debe producir ningún error y solamente debe imprimir las tres
# probabilidades con dos cifras decimales. 
# Se considera que el programa no corre si se demora más de un minuto
# en producir la respuesta.
# Al correr tres veces el programa la respuesta debe ser la misma.


# Solamente puede utilizar las funciones y métodos vistas en clase
# (videos o clases sincrónicas, o que ya se encuentren en el repositorio) . 
 

import numpy as np

def gatos_y_perros(m, n):
    n_gatos = m
    n_perros = n

    gato = 0
    perro = 1
    animales = n_gatos*[gato] + n_perros*[perro]# 0 es para gatos, 1 para perros.

    N = 1000
    perro_en_primera = 0 
    gato_en_primera = 0
    perro_en_primera_gato_en_ultima = 0
    for i in range(N):
        np.random.shuffle(animales)

        if animales[0]==perro: # perro en primera posicion
            perro_en_primera += 1

        if animales[0]==gato: # gato en primera posicion
            gato_en_primera  += 1

        if animales[0]==perro and animales[-1]==gato: # perro en primera, gato en ultima
            perro_en_primera_gato_en_ultima += 1

    a = (perro_en_primera/N)
    b = (gato_en_primera/N)
    c = (perro_en_primera_gato_en_ultima/N)
    return a, b, c



#a = []
#b = []
#c = []
#for i in range(10):
#    x = gatos_y_perros(1000,15000)
#    a.append(x[0])
#    b.append(x[1])
#    c.append(x[2])
#print(np.mean(a), np.std(a))
#print(np.mean(b), np.std(b))
#print(np.mean(c), np.std(c))
         
                                      
