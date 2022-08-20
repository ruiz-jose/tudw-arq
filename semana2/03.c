/******************************************************************************
 ejemplo 03: programa para ingresar caracter
    Esperar algunos segundos para ingresar caracter y presionar enter
    Este ejemplo ayuda a dstinguir entre tiempo vinculados a CPU y E/S
*******************************************************************************/


// compilar  gcc ubuntu: gcc 03.c -o 03
// correr programa:  time ./03


#include <stdio.h>
#include <unistd.h> 	// for sleep()


int main()
{
    int valorPeso;
    // programa espera que el usuario ingrese un carácter y presione enter
    printf("Introduzca su peso en kg como valor numerico: ");
    scanf("%d", &valorPeso);
    printf("Gracias");
    return 0;
}