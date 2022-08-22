
'''
    Ejemplo 01.py: 

    Tiempo de respuesta (Wall time: reloj de pared): Es la diferencia entre el momento en que un programa terminó  su ejecución
    y el momento en que se inició el programa. Es como medir el tiempo con un cronómetro.
    IMPORTANTE: También incluye el tiempo de espera de los recursos .

    https://www.onlinegdb.com/online_python_compiler

    Ejemplo tomado de:
    https://pynative.com/python-get-execution-time-of-program/#wall-time-vs-cpu-time
'''


import time

# Obtiene tiempo de inicio (start time)
st = time.time()

# main program
# Calcular la suma del primer millon de numeros (0-999999)
sum_x = 0
for i in range(1000000):
    sum_x += i

# Espera por 3 segundos
time.sleep(3)

print('La suma del primer millon de números es:', sum_x)

# Obtiene tiempo de finalizacion (end time)
et = time.time()

# Calcular el tiempo transcurrido: diferencia Finalizacion - Inicio (elapsed time)
elapsed_time = et - st
print('Tiempo de respuesta:', elapsed_time, 'segundos')

# El tiempo de respuesta dependera de cada arquitectura