##  Semana 4: Aprender Arquitectura programando!! (Idea: Christiam Gregorio Rey Pacheco)

** Objetivo: comprender como funciona la arquitectura acumulador**

### 1. Arquitectura Acumulador 
Hagamos nuestra arquitectura acumulador en python

Repertorio de instrucciones 
load direccion
add direccion
store direccion

CPU 20 Hz 1/20 = 0.05 segundos
Memoria RAM 10 Hz = 0.1 
    - Tarda 2 ciclos en una read/write 0.2 segundos
    - El CPU queda en espera por 4 ciclos (0.05 * 4 =0.02 segundos)

load x fectch 3 ciclos + 4 