'''
    Ejemplo 02.py muestra error al superar el rango de los valores enteros
    probado para una arquitectura de 64 bits con python 3
    valor entero máximo en Python 3 Max Int
    - valor maximo entero 2**63 -1 = 9223372036854775807
    - valor minimo entero   -2**63 =-9223372036854775808
    - tipo de datos <class 'int'> 
    
    error: python int too large to convert to C ssize_t

	El valor sys.maxsize informa el tamaño del puntero de las estructuras de datos de Python, como listas.
 '''

import sys
	
max_val = sys.maxsize

try:

	# agregar un elemento 
	#list = range(max_val)

	# agregar otro elemento 
	max_val = max_val + 1
	list = range(max_val)
	
	# Mostrar el tamaño de list
	print(len(list))
	
	print("Exitoso se agrego un elemento")
	
except Exception as e:

	# displaying the exception
	print(e)
	print("NO Exitoso")
