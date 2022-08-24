'''
    Ejemplo 02.py: 

    Tiempo CPU: se refiere al tiempo que la CPU estuvo ocupada procesando las instrucciones del programa.
    No incluye el tiempo que se pasa esperando que se complete otra tarea (como las operaciones de E/S)

    https://www.onlinegdb.com/online_python_compiler

    Ejemplo tomado de:
    https://pynative.com/python-get-execution-time-of-program/#wall-time-vs-cpu-time

'''
# Compilar y correr en python: python3 02.py

import time

# Obtiene tiempo de inicio (start time)
st = time.process_time()

# main program
# Calcular la suma del primer millon de numeros (0-999999)
sum_x = 0
for i in range(1000000):
    sum_x += i

# Espera por 3 segundos
time.sleep(3)

print('La suma del primer millon de números es:', sum_x)

# Obtiene tiempo de finalizacion (end time)
et = time.process_time()

# Calcular el tiempo CPU: diferencia Finalizacion - Inicio
res = et - st
print('Tiempo CPU:', res, 'segundos')

# Debido a que estamos calculando el tiempo CPU, el programa estuvo activo durante más de 3 segundos.
# Aún así, esos 3 segundos no se agregaron al tiempo CPU.