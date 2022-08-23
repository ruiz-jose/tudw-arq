/******************************************************************************
 ejemplo 02: programa para utilizar con el comando time linux (bash)
El tiempo de ejecucion de un programa en una computadora se descompone en:
**real** es el tiempo desde el principio hasta el final de ejecucion del programa, 
   como si se hubiera medido con un cronómetro o reloj de pared. 
   Tambien se denomina tiempo transcurrido o tiempo de respuesta del programa,
   incluye los intervalos de tiempo utilizados por otros procesos y 
   el tiempo que el proceso pasa bloqueado (por ejemplo, si está esperando que se complete la E/S).
- **user** es el tiempo del CPU dedicado al código en modo usuario (fuera del kernel).
    Es el tiempo de CPU realmente utilizado para ejecutar el proceso. 
	 Otros procesos y el tiempo que el proceso pasa bloqueado no cuentan para esta cifra.
- **sys** es el tiempo de CPU invertido en el kernel. 
    Esto significa que el tiempo de CPU dedicado a las llamadas al sistema dentro del kernel.
*******************************************************************************/


// compilar  gcc ubuntu: gcc 02.c -o 02
// correr programa:  time ./02


#include <stdio.h>
#include <unistd.h> 	// for sleep()


int main()
{
	
   // Calcular la suma del primer millon de numeros (0-999999)
   long suma=0;
   for(long i=0;i<1000000;i++){
      suma += i;
   }
   printf("La suma del primer millon de números es: %ld \n",suma);
   
   // duerme 3 segundos el programa
	sleep(3);
	return 0;
}