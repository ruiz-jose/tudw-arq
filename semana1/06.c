/******************************************************************************
06.c: Referencia a elementos de un arreglo fuera de rango
probarlo en https://www.onlinegdb.com/
*******************************************************************************/
#include<stdio.h>
// compilar gcc ubuntu: gcc 06.c -o 06 && ./06

int main ( ) {
    
    int  arreglo[2];  // arreglo de un elemento  
    
    arreglo[0] = 5;
    printf("Arreglo accedido dentro de los limites.");

    arreglo[1] = 6;
    printf("Arreglo accedido dentro de los limites.");

    arreglo[2] = 7;
    printf("Arreglo No accedido fuera de los limites.");
    
    return 0;
}
