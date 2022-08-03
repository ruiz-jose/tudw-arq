/******************************************************************************
 ejemplo 01: overflow short signed: muestra overflow en un entero corto signado,  
 al incrementar la variable x producce un desbordamiento.
 En C los enteros corto signado (signed short int)
 ocupan 2 bytes y tienen un rango de {-32768; 32767}
*******************************************************************************/

// compilar gcc ubuntu: gcc 01.c -o 01 && ./01

#include <stdio.h>


int main()
{
    signed short int x = 32767;
    
    printf("x=%i \n", x);
    x++;
    printf("x+1=%i \n", x);
    return 0;
}