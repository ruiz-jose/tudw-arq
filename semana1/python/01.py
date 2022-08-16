#https://www.online-python.com/

# ejemplo para arquitectura de 64 bits

# valor entero máximo en Python 3 Max Int
   
#  valor maximo entero 2^63 -1 = 9223372036854775807
#  valor minimo entero   -2^63 =-9223372036854775808
#  tipo de datos <class 'int'>

import sys

# valor maximo entero 2^63 -1
max_val = sys.maxsize
print(max_val)


# valor minimo entero -2^63
min_val = - sys.maxsize - 1
print(min_val)

# tipo de datos de max_val
print(type(max_val))