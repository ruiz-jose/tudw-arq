<div align="center">
	<a href="https://github.com/ruiz-jose/tudw-arq/header.svg">
		<img src="header.svg" width="800" height="400" alt="TUDW-ARQ">
	</a>	
</div>

# Clases de arquitectura de computadoras - Tecnicatura Universitaria en Desarrollo Web - 2022

Puedes descargar la maquina virtual de la asignatura "tudw-arq-clave=2022.ova" [linux tudw-arq](https://drive.google.com/file/d/1BaPOo7rljAaHxAZYd7Eibd7w6VuXDTI2/view?usp=sharing) e importarla en virtual-box para correr los ejemplos en lenguaje c a traves de una maquina linux con gcc instalado y visual studio code.


# Semana 1: ¿Por qué estudiar arquitectura?

### - 1. Realidad #1: Aritmética en la computadora
  En la computadora los numeros se representan mediante atracciones y de manera finita, por lo tanto es necesario conocer sus limites y sus propiedades. 

### - 2. Realidad #2: Conocer ensamblador
  Es necesario conocer ensamblador para conocer que codigo es mas eficiente

### - 3. Realidad #3:  El acceso a la memoria importa
  La memoria es finita y conocer sus como funciona permite mejorar el código.


# Semana 2: Medidas de rendimiento

### - 1. Aceleración: comparación de dos maquinas

### - 2. CPI: promedio de ciclos por instrucción

### - 3. IPS: instrucciones por segundo
	  3.1 Frecuencia y ciclo de reloj
### - 4.Tiempo CPU
	  4.1 Ejemplo de time en linux (bash)

		El tiempo de ejecucion de un programa en una computadora se descompone en:
		- 'real' el tiempo desde el principio hasta el final de la llamada, como si lo hubiera medido un ser humano con un cronómetro o reloj de pared. Tambien se define como  tiempo total transcurrido o tiempo de respuesta del programa, incluye los intervalos de tiempo
		utilizados por otros procesos y el tiempo que el proceso pasa bloqueado (por ejemplo, si está esperando que se complete la E/S).
		- 'user' es el tiempo del CPU dedicado al código en modo usuario (fuera del kernel) dentro del proceso.
		Este es solo el tiempo de CPU real utilizado para ejecutar el proceso. Otros procesos y el tiempo que el proceso pasa bloqueado no cuentan para esta cifra.
		- 'sys' es el tiempo de CPU invertido en el kernel dentro del proceso. Esto significa que el tiempo de CPU dedicado a las llamadas al sistema dentro del kernel.
		Al igual que 'user', este es solo el tiempo de CPU utilizado por el proceso. 
		
		user + sys  dirá cuánto tiempo de CPU real usó su proceso.

Por que?
real≠ user+ sys.

Que pasa si el programa (proceso) tiene múltiples subprocesos y se ejecuta en un procesador multinucleo?
user + sys > real
real representa el tiempo transcurrido real, mientras que los valores user y sys representan el tiempo de ejecución de la CPU. Como resultado, en un sistema multinúcleo el tiempo user y/o sys (así como su suma) podría exceder el tiempo Real o de respuesta, ya que diferentes subprocesos o procesos pueden ejecutarse en paralelo.



