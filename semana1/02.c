/******************************************************************************
 ejemplo 02: overflow int signed: muestra overflow en un entero signado,  
 al multiplicar la variable x * x producce un desbordamiento.
 En C los enteros signado (signed int)
 ocupan 4 bytes y tienen un rango de {-2.147.483.648 ; 2.147.483.647}
*******************************************************************************/

// compilar gcc ubuntu: gcc 02.c -o 02 && ./02  

#include <stdio.h>

int main()
{
    int i, x;
    for (i = 1; i <= 5; i++)
    {
        x = i*10000;
        printf("x = %d * %d = %d\n", x, x, x*x);
    
    }
    return 0;
}