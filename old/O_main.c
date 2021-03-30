#include <stdio.h>
#include <math.h>
 
int main() 
{ 
int a, b,c,delt;
printf("a*x²+b*x+c "); 
printf("donnes al val de a");
scanf("%d", &a);
printf("donnes al val de b");
scanf("%d", &b);
printf("donnes al val de c");
scanf("%d", &c);

delt = pow(b,2) - 4.0*a*c;
 
  if (delt>0) /* b^2-4ac > 0 */  
     {  
       printf("Les solutions réelles de cette équation sont :"); 
       printf(" x1 = %f", (-b+sqrt(delt))/(2*a)); 
       printf(" x2 = %f",(-b-sqrt(delt))/(2*a)); 
     } 
 else if (delt==0) /* b^2-4ac = 0 */  
     { 
       printf("Cette équation a une seule solution réelle :"); 
       printf(" x =  %d", ((-b)/(2*a))); 
     } 
 
 
 
 /* b^2-4ac < 0 */
else if (delt<0)   
 {
printf("Les solutions   :\n"); 
  printf("%f", ((-b) + (sqrt(-delt)/(2*a)))) ;
  printf("%f", ((-b)+(-sqrt(-delt)/(2*a))) ); 
 } 

/* 0x = 0 */ 
if (a==0 && b==0 && c==0) {
     printf("Tout réel est une solution de cette équation ");

}
 
   
/* Contradiction: c # 0 et c = 0 */ 
else if (a==0 && b==0)    {
    printf("Cette équation ne possède pas de solutions");
}
    
/* bx + c = 0 */
else if (a==0)   {
    printf("La solution de cette équation du premier degré est :");  
    printf(" x = %d", -c/b);
}
     
}
       