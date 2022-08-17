'''
    Ejemplo 02.py muestra error al superar el rango de los valores de una lista
    probado para una arquitectura de 64 bits con python 3
    valor entero máximo en Python 3 Max Int
    - valor maximo entero 2**63 -1 = 9223372036854775807
    - valor minimo entero   -2**63 =-9223372036854775808
    - tipo de datos <class 'int'> 
    
    error: python int too large to convert to C ssize_t

	El valor sys.maxsize informa el tamaño maximo de una estructura de datos en Python.
 '''

import sys
	
max_val = sys.maxsize

try:

	# Se define una lista con un rango max_val elementos 
	#list = range(max_val)

	# se incrementa en uno max_val y se genera nueva lista 
	max_val = max_val + 1
	list = range(max_val)
	
	# Arroja error al intentar acceder a la lista porque tiene un rango superior
	print(len(list))
	
	print("Exitoso tamaño de lista correcta")
	
except Exception as e:

	# Se atraba el error
	print(e)
	print("NO Exitoso supero tamaño de la lista")
