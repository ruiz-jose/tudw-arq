/*************************************************************************************
 ejemplo 05: si un programa se realizan divisiones por un numero multiplo 2 exp n 
 se pueden utilizar instrucciones de desplazamientos a la derecha, debido a que 
 son más rapida que la instruccion de dividir.
 Pagina con ejemplos: https://bitwisecmd.com/
**************************************************************************************/

// compilar gcc ubuntu: gcc 05.c -o 05 && ./05

#include <stdio.h>
int main()
{
    
    int x =20; 	/* 20 =  0001 0100 */

    printf("Desplazar 1 bit a la derecha x= %i \n", x >> 1); /* 10 = 0000 1010 */
    printf("Desplazar 2 bit a la derecha x= %i \n", x >> 2); /* 5  = 0000 0101 */
    return 0;
}
