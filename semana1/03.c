/*************************************************************************************
 ejemplo 03: donde {x,y,z] son reales (float) en formato de dato en punto flotante,  
 En C los reales (float) ocupan 4 bytes y tienen un rango de {1.18e-38; 3.40e38}
 Mas sobre tipo de datos float https://www.h-schmidt.net/FloatConverter/IEEE754.html
**************************************************************************************/

// compilar gcc ubuntu: gcc 03.c -o 03 && ./03  

#include <stdio.h>
int main()
{
  float x=1e20, y=-1e20, z=3.14;

  /* 1e+20 = 1 × 10exp20 = 100.000.000.000.000.000.000
   "mEn" significa m × 10n
   x y z son numeros grandes y al sumarles un numero z
   no impacta en el resultado -1e20 + 3.14 = -1e20*/
   
   /* No se cumple la propiedad asociativa matematica
   (x+y)+z) distinto que x+(y+z))          */
  printf ("valor de (x+y)+z= %f \n", (x+y)+z);
  printf ("valor de x+(y+z)= %f \n", x+(y+z));

  // otro ejemplo
  float a = 12335545621232154;
  printf ("valor de (a) antes de a = a + 1; = %f \n",a);
  a = a + 1;
  printf ("valor de (a) despues de a = a + 1; = %f \n", a);
 
 /* otros ejemplos:
  - http://geocar.sdf1.org/numbers.html
  - https://float.exposed/0x3fc00000
  */ 

  return 0;
}
