#Suponga que tiene dos enteros A y B que representan fechas, y un tercer entero C que representa un número de meses.

#La fecha 7 de enero del 2020 se representaría de la forma 20200107. Es decir, los cuatro primeros dígitos de la izquierda corresponden al año, los siguientes dos al mes (con un cero por delante si el mes es anterior a octubre) y los últimos dos dígitos al día del mes (con un cero por delante si el día es menor que 10).

#Escriba un programa de python que:

#1. Asigne al entero A la fecha de su nacimiento. (Simplemente A=19901010, por ejemplo)

#2. Asigne al entero C un numero entero diferente de cero.

#3. Calcule una nueva fecha B que corresponde a la fecha A luego de aumentarle el número de meses en C. Por ejemplo, si A=20101010 (10 de octubre del 2010) y C=-12 (12 meses hacia atrás), B debería ser el 20091010 (10 de octubre del 2009).

#4. Imprima A, B y C.

#Solamente son permitidas sumas, multiplicaciones, divisiones, restas y módulos. El programa debe funcionar correctamente si se cambia A a cualquier otra fecha entre el año 1 y el año 9999, y C se cambia a cualquier otro valor de tal manera que B también se encuentre entre el año 1 y el año 9999.

#El programa debe estar en un archivo llamado "ApellidoNombre_MagistralEjercicio01.py" donde Apellido y Nombre debe reemplazarlos con su apellido y nombre. Suba ese archivo como respuesta a esta actividad.

A = 20011230
C = -13

A_ano = A//10000
A_mes = (A//100)%100
A_dia = A%100

meses_totales_A = A_ano*12 + (A_mes-1) # meses completos que han pasado desde un 0 de referencia
meses_totales_B = meses_totales_A + C  # meses completos que han pasado desde un 0 de referencia

B_ano = meses_totales_B//12
B_mes = meses_totales_B%12 + 1 # el uno toma en cuenta el mes en curso, que no se ha completado

B = B_ano*10000 + B_mes*100 + A_dia

print(A, B, C)
