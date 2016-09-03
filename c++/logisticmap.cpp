#include <iostream>
#include <iomanip>

int main(){
    long n,i;
    double r,xi,xj;
    std::cout<<"I will calculate the logistic map for nth iteration"<<std::endl;
    std::cout<<"What is n?";
    std::cin>>n;
    std::cout<<"What is R?"<<std::endl;
    std::cin>>r;
    std::cout<<"What is x0?"<<std::endl;
    std::cin>>xi;
    i=0;
    while (i<n){
      xi=r*xi*(1.0-xi);

      i+=1;
    }
    std::cout<<std::setprecision(12);
    std::cout<<xi<<std::endl;

    return 0;}

