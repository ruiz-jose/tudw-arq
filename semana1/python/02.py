'''
    Ejemplo 02.py:
	Muestra el rango maximo de elementos que pueden tener 
    las estructuras de datos (listas, diccionarios, conjuntos, etc.) en python
    esta dato por el valor entero máximo.
	 Probado para una arquitectura de 64 bits con python 3,
    valor entero máximo en Python 3 Max Int
    - valor maximo entero 2**63 -1 = 9223372036854775807
    - valor minimo entero -2**63 =-9223372036854775808
    - tipo de datos <class 'int'> 

	Si se genera una estructura (Lista) con un rango superior
	y se intenta acceder a la cantidad de elementos de la lista (len)
	genera una excepcion que es atrapada.
       
    error: python int too large to convert to C ssize_t

	El valor sys.maxsize informa el tamaño maximo de una estructura de datos en Python.
 '''



# importar libreria de python sys y su atributo maxsize
import sys

# valor maximo entero 2**63 -1
max_val = sys.maxsize
print(max_val)


# valor minimo entero -2**63
min_val = - sys.maxsize - 1
print(min_val)

# tipo de datos de max_val
print(type(max_val))


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

	# Se atrapa el error
	print(e)
	print("NO Exitoso supero tamaño de la lista")
