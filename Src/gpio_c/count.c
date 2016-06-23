#include<stdio.h>
#include<wiringPi.h>

//GPIO to seven segment pins a,b,c,d,e,f,g,dp
//these are wiring Pi pin numbers
unsigned int gpio[8]={8,9,7,0,2,3,12,13};

unsigned int b[8]; // for bit values of one seven segment digit

//seven segment code for 0 to 9 digits
unsigned int ssc[10]={0xc0,0xF9,0xa4,0xb0,0x99,0x92,
0x82,0xf8,0x80,0x90}; 

void seg_count(int);
int main()
{
int i,b;
printf("counter\n");
if(wiringPiSetup () == -1)    //initialization
return 1 ;
	
for(i=0;i<=7;i++)
pinMode (gpio[i], OUTPUT) ;   // pin mode set to output


while(1)
{
for(i=0;i<=9;i++)
{
seg_count(i);
delay(1000);
}
	 }
return 0;
}
void seg_count (int x)
{
int i;
//separating bits from digit x 
for(i=0;i<=7;i++)
b[i]=(ssc[x]>>i)& 0x01;

printf ("Raspberry Pi seven segment display %d\n",x) ;

for (i=0;i<=7;i++)	// setting GPIO pins as per seven seg code
 		digitalWrite(gpio[i],b[i]) ;

}
