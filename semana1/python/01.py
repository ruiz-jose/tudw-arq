
'''
    Ejemplo 01.py: Muestra el rango maximo de elementos que pueden tener 
    las estructuras de datos (listas, diccionarios, conjuntos, etc.) en python
    esta dato por el valor entero máximo en Python 3 Max Int arquitectura x86-64 bits
    - valor maximo entero 2**63 -1 = 9223372036854775807
    - valor minimo entero -2**63 =-9223372036854775808
    - tipo de datos <class 'int'>

    En otros lenguajes de programación, los int tenían un valor máximo que pueden representar.
    Con 64 bits, el rango es de -9.223.372.036.854.775.808 hasta 9.223.372.036.854.775.807.
    En Python no tenemos que preocupar de esto, ya que el interprete de python 
    asigna memoria dinamicamente al numero y podemos representar prácticamente cualquier número.

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

x = 250**250
print(x)
print(type(x))
