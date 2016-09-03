#include <iostream>
#include <iomanip>      /*setprecision*/
#include <stdlib.h>       /*atof*/

/*
 * either takes inputs from stdin or from cmdline:
 * argv[1]=x_i
 * argv[2]=R
 * argv[3]=n->number of iterations
 */
int main(int argc, char* argv[]){
    long n,i;
    double r,xi,xj;
    if (argc==1){
        std::cout<<"I will calculate the logistic map for nth iteration"<<std::endl;
        std::cout<<"What is n?";
        std::cin>>n;
        std::cout<<"What is R?"<<std::endl;
        std::cin>>r;
        std::cout<<"What is x0?"<<std::endl;
        std::cin>>xi;
    }
    else{
        xi=atof(argv[1]);
        r=atof(argv[2]);
        n=atof(argv[3]);
    }
    i=0;
    while (i<n){
      xi=r*xi*(1.0-xi);

      i+=1;
    }
    std::cout<<std::setprecision(12);
    std::cout<<xi<<std::endl;

    return 0;}

