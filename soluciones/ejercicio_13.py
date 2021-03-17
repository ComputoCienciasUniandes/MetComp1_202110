#Una profesora sabe por experiencias anteriores que las notas
#definitivas de los estudiantes de su curso tienen un valor medio de
#nota_media y una desviación estándar de std_media.

#Calcule la probabilidad con un método Monte Carlo de que la nota
#promedio de un curso de n_estudiantes se encuentre entre min_nota y
#max_nota.


#Esta probabilidad se debe calcular con una función llamada
#probabilidad_nota. Las variables de entrada de las función son (en ese orden):
#nota_media, std_media, n_estudiantes, min_nota y max_nota, donde todas
#las variables de entrada son de tipo entero. La función solamente debe
#devolver la probabilidad pedida (un número de tipo float).


#La solución debe estar en un archivo llamado
#"ApellidoNombre_Ejercicio13.py" donde Apellido y Nombre debe
#reemplazarlos con su apellido y nombre.  Suba ese archivo como
#respuesta a esta actividad. Al ejecutar "python
#ApellidoNombre_Ejercicio13.py" o al llamar la función no se debe
#producir ningún error ni escribir nada en la terminal.  Calificaremos
#la función con valores de n_estudiantes hasta 10000. Se considera que
#la función no corre si cada llamada de la función se demora más de 10
#segundos en correr.


#Solamente puede utilizar las funciones y métodos vistos en clase
#(videos o clases sincrónicas, o que ya se encuentren en el
# repositorio).


import numpy as np

def probabilidad_nota(nota_media, std_media, n_estudiantes, min_nota, max_nota):
    n_sample = 100000
    x = np.random.normal(loc=nota_media, scale=std_media/np.sqrt(n_estudiantes), size=n_sample)
    n_in = np.count_nonzero((x>min_nota) & (x<max_nota))
    return n_in/n_sample

