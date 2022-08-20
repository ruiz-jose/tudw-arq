/******************************************************************************
 ejemplo 02: programa para utilizar con el comando time linux (bash)
El tiempo de ejecucion de un programa en una computadora se descompone en:
- 'real'es el tiempo del reloj de pared: el tiempo desde el principio hasta el final de la llamada.
  Es el tiempo total transcurrido o tiempo de respuesta del programa, incluidos los intervalos de tiempo
   utilizados por otros procesos y el tiempo que el proceso pasa bloqueado (por ejemplo, si está esperando que se complete la E/S).
- 'user' es el tiempo del CPU dedicado al código en modo usuario (fuera del kernel) dentro del proceso.
   Este es solo el tiempo de CPU real utilizado para ejecutar el proceso. Otros procesos y el tiempo que el proceso pasa bloqueado no cuentan para esta cifra.
- 'sys' es el tiempo de CPU invertido en el kernel dentro del proceso. Esto significa que el tiempo de CPU dedicado a las llamadas al sistema dentro del kernel.
   Al igual que 'user', este es solo el tiempo de CPU utilizado por el proceso. 
*******************************************************************************/


// compilar  gcc ubuntu: gcc 02.c -o 02
// correr programa:  time ./02


#include <stdio.h>
#include <unistd.h> 	// for sleep()


int main()
{
	// duerme 3 segundos el programa
	sleep(3);
	return 0;
}