'''
    Ejemplo 03.py:
    Errores de aproximación en reales (float) o punto flotante
    Debido a que la representación interna de los valores en coma flotante
    sigue el estándar IEEE 754 y estamos trabajando con aritmética finita.

    A diferencia de los enteros, los números flotantes sí que tienen un límite en Python. 
      
 '''

# Compilar y correr en python: python3 03.py

# ejemplo 03.c en python 
x=1e20
y=-1e20
z=3.14

# 1e+20 = 1 × 10exp20 = 100.000.000.000.000.000.000
# "mEn" significa m × 10n
# x y z son numeros grandes y al sumarles un numero z
# no impacta en el resultado -1e20 + 3.14 = -1e20
   
# No se cumple la propiedad asociativa matematica
#(x+y)+z) distinto que x+(y+z))        
print ("valor de (x+y)+z= ", (x+y)+z);
print ("valor de x+(y+z)= ", x+(y+z));

# x debería dar 1.0
x = (19 / 155) * (155 / 19)
print(x)

# Debería dar 1.0  http://geocar.sdf1.org/numbers.html
print(9999999999999999.0 - 9999999999999998.0)

# importar libreria de python sys 
import sys

print(sys.float_info.min)
print(sys.float_info.max)
