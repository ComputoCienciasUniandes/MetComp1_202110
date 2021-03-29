#Contamos con dos series diferentes de mediciones de la resistencia de
#dos tipos diferentes de concreto, serie_A y serie_B. Calcule con un
#método montecarlo de reordenamiento (shuffling) el intervalo de
#confianza bilateral (two-sided) del p_confianza por ciento para la
#diferencia de los promedios de serie_A y serie_B.  

#Esta probabilidad se debe calcular con una función llamada
#calcula_intervalo_reordenando. Las variables de entrada de las función
#son (en ese orden):  serie_A, serie_B y p_confianza, donde todas las
#variables de entrada son de tipo float (serie_A y serie_B son listas
#de floats), excepto 
#p_confianza que es un entero que se encuentra entre 1 y 100. La
#función solamente debe devolver una lista con dos elementos que
#describen el intervalo de confianza pedido, donde el primer elemento
#es el valor inferior del y el segundo elemento es el valor superior.  

#La solución debe estar en un archivo llamado
#"ApellidoNombre_Ejercicio16.py" donde Apellido y Nombre debe
#reemplazarlos con su apellido y nombre.  Suba ese archivo como
#respuesta a esta actividad. Al ejecutar "python
#ApellidoNombre_Ejercicio16.py" o al llamar la función no se debe
#producir ningún error ni escribir nada en la terminal.  Se considera
#que la función no corre si cada llamada de la función se demora más de
#30 segundos en correr. 

#Solamente puede utilizar las funciones y métodos vistos en clase
#(videos o clases sincrónicas, o que ya se encuentren en el
# repositorio).  

import numpy as np

def calcula_intervalo_reordenando(serie_A, serie_B, p_confianza):
    n_A = len(serie_A)
    n_B = len(serie_B)
    
    n_iteraciones = 100000
    delta = np.zeros(n_iteraciones)    
    serie = np.array(serie_A + serie_B)

    for i in range(n_iteraciones):
        np.random.shuffle(serie)
        A = serie[:n_A]
        B = serie[n_A:]
        delta[i] = A.mean() - B.mean()
    
    delta = np.sort(delta)

    i_confianza = int((n_iteraciones/100) * ((100 - p_confianza)/2))
    return [delta[i_confianza],delta[-i_confianza]]

#serie_A = [84,72,57,46,63,76,99,91]
#serie_B = [81,69,74,61,56,87,69,65,66,44,62,69]

#a=calcula_intervalo_reordenando(serie_A, serie_B, 80)
#np.testing.assert_allclose(a[1], abs(a[0]), atol=0.2)
#np.testing.assert_allclose(a[1], 8.4, atol=0.2)

#a=calcula_intervalo_reordenando(serie_A, serie_B, 70)
#np.testing.assert_allclose(a[1], abs(a[0]), atol=0.2)
#np.testing.assert_allclose(a[1], 6.8, atol=0.2)

#a=calcula_intervalo_reordenando(serie_A, serie_B, 60) 
#np.testing.assert_allclose(a[1], abs(a[0]), atol=0.2)
#np.testing.assert_allclose(a[1], 5.5, atol=0.2)

