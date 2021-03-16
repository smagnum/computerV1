#include <stdio.h>


 
double Sqrt(double X) {
  double A,B,C,D;
  if(X==0.0) {
     return 0.0;
  } 
   else {
     C=1.0;
     D=X;
     while(D>=2.0) {
        D=0.25*D;
        C=2.0*C;
     }
     while(D<0.5) {
        D=4.0*D;
        C=0.5*C;
     }
     A=D;
     B=1.0-D;
     do {
        A=A*(1.0+0.5*B);
        B=0.25*(3.0+B)*B*B;
     } while(B>=1.0E-15); /pow(10, -15/
     return A*C;
  }
}
 
 void main() {
    double NB=49.0;
    
     printf("Sqrt(%f)=%f\n",NB,Sqrt(NB));
}