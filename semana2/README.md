##  Semana 2: Medidas de rendimiento

### 1. Aceleración: 
    - Comparación de dos maquinas
    - Mejorar una parte del sistema
	
### 2. CPI: promedio de ciclos por instrucción

### 3. IPS: instrucciones por segundo
    - Frecuencia y ciclo de reloj
    - Millones de instrucciones por segundo (MIPS)
	
### 4.Tiempo de respuesta y tiempo CPU

El tiempo de ejecucion de un programa en una computadora se descompone en linux con el comando ```time``` (bash):

-**Tiempo de respuesta o transcurrido (real)** : es el tiempo desde el principio hasta el final de ejecucion del programa, 
	  como si se hubiera medido con un cronómetro o reloj de pared. 
         incluye los intervalos de tiempo utilizados por otros procesos y 
	  el tiempo que el proceso pasa bloqueado (por ejemplo, si está esperando que se complete la E/S).
	  El tiempo real incluye el tiempo de E/S, intervalos de tiempo utilizados por otros programa (multitarea) 
	  y todos los demás tipos de espera en los que incurre el programa (sleep).
	
-**Tiempo de CPU**: tiempo que utilizo el CPU para ejecutar las instrucciones de un programa, se descompone en:

- **user** es el tiempo del CPU dedicado al código en modo usuario (fuera del kernel).
	  Es el tiempo de CPU realmente utilizado para ejecutar el proceso. 
	  Otros procesos y el tiempo que el proceso pasa bloqueado no cuentan para esta cifra.
- **sys** es el tiempo de CPU invertido en el kernel. 
	  Esto significa que el tiempo de CPU dedicado a las llamadas al sistema dentro del kernel.
			

**Consideraciones tiempo de respuesta y tiempo CPU**

    El tiempo de CPU (user + sys) nos dirá cuánto tiempo utilizó el CPU para procesar 
    instrucciones de un programa (user) o sistema operativo (sys).
            
    Ejemplo del comando ```df``` (Disk Filesystem se usa para chequear el espacio en el disco) 

    ```time df```

    real    0m0.243s

    user    0m0.000s

    sys     0m0.063s

    Se puede observar el tiempo de CPU consumido por el sistema operativo (sys)

- ¿Qué pasa cuando el sistema operativo es multitarea?
    Las computadoras solo pueden hacer una tarea (o proceso ) a la vez. Pero una computadora puede cambiar tareas muy rápidamente y engañar a seres humanos lentos haciéndoles creer que está haciendo varias cosas a la vez. Esto se llama tiempo compartido.
    Uno de los trabajos del kernel es administrar el tiempo compartido. Cada 1/60 de segundo, el scheduler detiene cualquier proceso que se esté ejecutando actualmente, lo suspende en su lugar y le pasa el control a otro proceso.
    El procesador comparte su tiempo entre los procesos, entonces si el proceso se ejecuta con otros procesos debe esperar su turno para utilizar el CPU.

- ¿Por qué real ≠ user+ sys?
   Consultar el sitio web (https://www.fcad.uner.edu.ar/), en este escenario el proceso espera la respuesta del sitio
   se puede observar como el programa espera la repuesta del sitio, el tiempo del CPU (sys=0.016s ) representa el tiempo
   que el sistema operativo realiza la invocación al sitio.
   
   ```time host www.fcad.uner.edu.ar```
   
   real    0m0.903s
   
   user    0m0.000s
   
   sys     0m0.016s
   

- ¿Por qué real > user + sys? ¿Qué pasa si un programa (proceso) tiene múltiples subprocesos y se ejecuta en un procesador multinucleo?
    En un procesador multinucleo un programa puede usar dos o más CPU para el procesamiento mediante la programación de procesamiento en paralelo.
    En tales situaciones, el tiempo de CPU total es la suma del tiempo de CPU consumido por todas las CPU utilizadas por el programa.
    En un sistema multinúcleo el tiempo user y/o sys (así como su suma) podría exceder el tiempo Real o de respuesta,ya que diferentes subprocesos o procesos pueden ejecutarse en paralelo.
    p.ej.

    real    0m5.815s

    user    0m8.213s

    sys     0m0.473s








