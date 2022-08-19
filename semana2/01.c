/******************************************************************************
 ejemplo 01: programa que muestra como calcular el tiempo de ejecucion de un programa
*******************************************************************************/

// compilar gcc ubuntu: gcc 01.c -o 01 && ./01

#include <stdio.h>
#include <time.h>   	// for time()
#include <unistd.h> 	// for sleep()


int main()
{
	time_t begin = time(NULL);

	// duerme 3 segundos el programa
	sleep(3);

	time_t end = time(NULL);

	// calcular el tiempo de ejecucion del programa: diferenca entre (end - begin)
	printf("El tiempo de ejecución es %ld segundos", (end - begin));

	return 0;
}