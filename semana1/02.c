/******************************************************************************
 ejemplo 02: overflow int signed: muestra overflow en un entero signado,  
 al multiplicar la variable x * x producen un desbordamiento.
 En C los enteros signado (signed int)
 ocupan 4 bytes y tienen un rango de {-2.147.483.648 ; 2.147.483.647}
*******************************************************************************/

// compilar gcc ubuntu: gcc 02.c -o 02 && ./02  

#include <stdio.h>

int main()
{
    int x;
    //x*x >= 0 ?
    x=40000;
    printf ("valor de x = 40000 * 40000=: %i \n", x*x);
    x=50000;
    printf ("valor de x = 50000 * 50000=: %i \n", x*x);
    return 0;
}