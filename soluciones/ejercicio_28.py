#Escriba una función en python que toma como entrada dos listas
#(valores_x, valores_y) y el grado de un polinomio (p_poli, un entero
#                                                   positivo) y ajusta
#por mínimos cuadrados el polinomio de orden p_poli que mejor ajusta
#los datos en valores_x y valores_y. La función debe implementar el
#ajuste en términos de operaciones de álgebra lineal trabajados en el
#"Ejercicio 28 - primera parte".  

#La función de debe llamar ajuste_matricial.

#La función debe tomar como entrada, en ese orden, las variables
#valores_x, valores_y y p_poli. 

#La función debe hacer el ajuste y hacer una gráfica donde se muestran
#los valores de entrada (valores_x, valores_y) y el polinomio de
#ajuste. La gráfica producida se debe guardar como "ajuste.png"
#(siguiendo el estilo de la Figura 1.4 del texto guía). 

#La solución debe estar en un archivo llamado
#"ApellidoNombre_Ejercicio28.py" donde Apellido y Nombre debe
#reemplazarlos con su apellido y nombre.  Suba ese archivo como
#respuesta a esta actividad. 
 
#Al ejecutar "python ApellidoNombre_Ejercicio28.py" no se debe producir
#ningún error. Al llamar la función con el nombre solicitado no se debe
#producir ningún error. 
import numpy as np
import matplotlib.pyplot as plt

def ajuste_matricial(valores_x, valores_y, p_poli):
    N = len(valores_x)
    S = np.ones((N,p_poli+1))
    for i in range(N):
        for j in range(p_poli+1):
            S[i,j] = (valores_x[i])**j

    S_inv = np.linalg.pinv(S)
    Y = np.array(valores_y)
    C = S_inv @ Y
    
    x = np.linspace(np.min(valores_x), np.max(valores_x), 100)
    y = np.zeros(100)
    for i in range(p_poli+1):
        y += C[i]*(x**i)

    plt.figure()
    plt.scatter(valores_x, valores_y)
    plt.plot(x, y)
    plt.savefig("ajuste.png")
    

#ajuste_matricial([1,2,4,6],[4,8,7,1],3)
#ajuste_matricial([-2.0, -2.0, 0.0, 3.0, 4.0], [5.0, 1.0, -3.0, -2.0, -5.5],1)
