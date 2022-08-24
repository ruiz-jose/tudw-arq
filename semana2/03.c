/******************************************************************************
 ejemplo 03: programa para ingresar caracter
    Esperar algunos segundos para ingresar caracter y presionar enter
    Este ejemplo ayuda a dstinguir entre tiempo vinculados a CPU y E/S
*******************************************************************************/


// compilar  gcc ubuntu: gcc 03.c -o 03
// correr programa:  time ./03


#include <stdio.h>
#include <unistd.h> 	// for sleep()
/*
corrida en la maquina virtual de clases
arq@arq-tudw:~/temp/tudw-arq/semana2$ time ./03
Introduzca su peso en kg como valor numerico: 4
Gracias
real	0m6,772s
user	0m0,001s
sys	0m0,000s
*/

int main()
{
    int valorPeso;
    // programa espera que el usuario ingrese un carácter y presione enter
    printf("Introduzca su peso en kg como valor numerico: ");
    scanf("%d", &valorPeso);
    printf("Gracias");
    return 0;
}