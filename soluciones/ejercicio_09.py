#Una caja contiene n_total transistores de los cuales n_funciona
#funcionan correctamente y n_no_funciona no funcionan
#correctamente. Los transistores se van probando uno a uno para ver si
#funcionan. Una vez se prueba un transistor se retira de la caja y no
#se devuelve. Sea N_1 el número de pruebas que se hicieron hasta
#encontrar el primer transistor dañado y N_2 el número de pruebas
#realizadas hasta encontrar el segundo transistor dañado. Escriba una
#función de Python que encuentre la probabilidad conjunta de N_1 y N_2
#usando un método Monte Carlo usando un número total de diez mil
#iteraciones.  

#La función debe llamarse probabilidad_conjunta.  La función toma como
#entrada dos variables enteras n_funciona y n_no_funciona (en ese
#orden). La función debe devolver un array bidimensional de numpy
#(i.e. con filas y columnas). En cada dirección el array tiene
#dimensión n_total+1. Al calificar la entrega vamos a llamar a la
#función de la siguiente manera: 

# p = probabilidad_conjunta(n_funciona, n_no_funciona)

# print(p[N_1, N_2])

#donde n_funciona, n_no_funciona, N_1, y N_2 son variables enteras que
#se inicializan al momento de calificar. 

# La función debe estar en un archivo llamado
# "ApellidoNombre_Ejercicio09.py" donde Apellido y Nombre
# debe reemplazarlos con su apellido y nombre.  Suba ese archivo como
# respuesta a esta actividad. 

#Al ejecutar "python ApellidoNombre_Ejercicio09.py" o al
#llamar la funci ón no se debe producir ningún error. 

# Solamente puede utilizar las funciones y métodos vistas en clase
# (videos o clases sincrónicas, o que ya se encuentren en el
# repositorio) . 

import numpy as np


def probabilidad_conjunta(n_funciona, n_no_funciona):
    funciona = 0
    no_funciona = 1

    transistores = np.array(n_funciona*[funciona] + n_no_funciona*[no_funciona])

    n_total = n_funciona + n_no_funciona
    probabilidad = np.zeros([n_total+1, n_total+1])
    n_realizaciones = 100000
    for i in range(n_realizaciones):
        np.random.shuffle(transistores)
    
        intentos = np.arange(len(transistores))+1

        intentos_sin_funcionar = intentos[transistores==no_funciona]

        N_1 = intentos_sin_funcionar[0]
        N_2 = intentos_sin_funcionar[1]
        
        probabilidad[N_1, N_2] += 1

    probabilidad /= n_realizaciones
    return probabilidad
