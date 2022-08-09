/*************************************************************************************
 ejemplo 04: si un programa se realizan multiplicaciones en la computadora se traducen 
 por desplazamientos, debido a que la instruccion de desplazamiento es más rapida que 
 la instruccion de multiplicar.
 Pagina con ejemplos: https://bitwisecmd.com/
**************************************************************************************/

// compilar gcc ubuntu: gcc 04.c -o 04 && ./04  

#include <stdio.h>
int main()
{
    
    int x =5; 	/* 5 =  0000 0101 */

    printf("Desplazar 1 bit a la izquierda x= %i \n", x << 1); /* 10 = 0000 1010 */
    printf("Desplazar 2 bit a la izquierda x= %i \n", x << 2); /* 20 = 0001 0100 */
    return 0;
}
