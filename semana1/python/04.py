'''
    Ejemplo 05.py:
    Multiplicacion: el operador << desplaza todos los bit n unidades a la izquierda. 
    division: el operador >> desplaza todos los bit n unidades a la derecha.
   
 '''

# Compilar y correr en python: python3 04.py

# mover cada bit 3 unidades a la izquierda 
x=0b1 # x= 1 = binario 0b1
print(x)
print(bin(x<<3)) # 1*2**3=8
print(x<<3)

# mover cada bit 2 unidades a la derecha  
x=0b1000 # x= 8 = binario 0b10
print(x)
print(bin(x>>2)) # 8/2**2=2
print(x>>2)




