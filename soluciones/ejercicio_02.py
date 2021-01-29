#Escriba un programa de python que:

#1. Lea un archivo llamado "texto.txt" usando readlines()

#2. Escriba en un archivo llamado "texto_invertido.txt" el contenido de "texto.txt" pero invertido. 

#Por ejemplo, si "texto.txt" contiene la dos líneas siguientes:

#Hola 

#Mundo

#El archivo "texto_invertido.txt" debe tener las dos líneas siguientes:

#odnuM

#aloH

#Solamente son permitidas las operaciones en python que aparezcan en los videos vistos hasta ahora en el curso. 

#El programa lo probaremos dejando el archivo "texto.txt" dentro de la misma carpeta en la que se encuentra su programa. Es decir, su programa debe abrir el archivo usando f=open("texto.txt", "r").

#El programa debe estar en un archivo llamado "ApellidoNombre_Ejercicio02.py" donde Apellido y Nombre debe reemplazarlos con su apellido y nombre. Suba ese archivo como respuesta a esta actividad.

f = open("texto.txt", "r")
lineas = f.readlines()
f.close()


f = open("texto_invertido.txt", "w")
n_lineas = len(lineas)

for i in range(n_lineas):
    linea = lineas[-(i+1)]

    linea_invertida = ""
    
    for j in range(len(linea)-1):
        linea_invertida = linea_invertida + linea[-(j+1)-1]

    f.write("{}\n".format(linea_invertida))

f.close()
