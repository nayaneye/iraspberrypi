#include <stdio.h>
#include <wiringPi.h>

#define LED     7

int main (void)
{
  printf ("Raspberry Pi  blink\n") ;

  wiringPiSetup () ;
  pinMode (LED, OUTPUT) ;

  for (;;)
  {
      printf("LED ON");
      digitalWrite (LED, HIGH) ;  // On
    delay (500) ;               // mS
       printf("LED OFF");
    digitalWrite (LED, LOW) ;   // Off
    delay (500) ;
  }
  return 0;
} 

