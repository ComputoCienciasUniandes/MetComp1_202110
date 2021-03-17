#El promedio histórico del salario de los egresados de una universidad
#es salario_historico, la desviación estándar es
#de std_salario_historico. 

#Calcule con un método Monte Carlo el salario promedio
#salario_promedio que una muestra aleatoria de  n_egresados debe tener
#para considerar que cualquier otro grupo de n_egresados tiene una
#probabilidad p_excede de tener un salario promedio que excede
#salario_promedio. 

#Esta probabilidad se debe calcular con una función llamada
#probabilidad_excede. Las variables de entrada de las función son (en ese orden):
#salario_historico, std_salario_historico, n_egresados, p_excede, donde
#todas las variables de entrada son de tipo entero, excepto p_excede
#que es de tipo float. Suponga que el valor de p_excede es un múltiplo
#entero de 0.001. La función solamente debe devolver el valor pedido
#del salario (un número de tipo entero). 

#La solución debe estar en un archivo llamado
#"ApellidoNombre_Ejercicio14.py" donde Apellido y Nombre debe
#reemplazarlos con su apellido y nombre.  Suba ese archivo como
#respuesta a esta actividad. Al ejecutar "python
#ApellidoNombre_Ejercicio14.py" o al llamar la función no se debe
#producir ningún error ni escribir nada en la terminal.  Calificaremos
#la función con valores de n_egresados hasta 10000. Se considera que la
#función no corre si cada llamada de la función se demora más de 10
#segundos en correr. 

#Solamente puede utilizar las funciones y métodos vistos en clase
#(videos o clases sincrónicas, o que ya se encuentren en el
# repositorio).  

import numpy as np

def probabilidad_excede(salario_historico, std_salario_historico, n_egresados, p_excede):
    n_sample = 10000000
    x = np.random.normal(loc=salario_historico, 
                         scale=std_salario_historico/np.sqrt(n_egresados), 
                         size=n_sample)
    x = np.sort(x)
    salario_promedio = int(x[n_sample - int(p_excede*n_sample)])
    return salario_promedio

#a = probabilidad_excede(50000, 1000, 4, 0.158)

