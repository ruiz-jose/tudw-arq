
'''
    Ejemplo 01.py: Muestra el rango maximo de elementos que pueden tener 
    las estructuras de datos (listas, diccionarios, conjuntos, etc.) en python
    esta dato por el valor entero máximo en Python 3 Max Int arquitectura x86-64 bits
    - valor maximo entero 2**63 -1 = 9223372036854775807
    - valor minimo entero -2**63 =-9223372036854775808
    - tipo de datos <class 'int'>

    https://www.onlinegdb.com/online_python_compiler
    https://www.online-python.com/
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