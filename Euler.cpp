#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

// variable constantes globales
const double K = 100;
const double M = 2;
const double LAMBDA = 1;
const double DeltaT = 0.01;

// declaracion de funciones
double f0(double t, double y0, double y1); // derivada de y0
double f1(double t, double y0, double y1); // derivada de y1
double Euler(double t, double y0, double y1);
double Euler2(double t, double y0, double y1);


int main(){
    
    double y0 = 1;
    double y1 = 0;
    double t =0;
    
    ofstream outfile;
    outfile.open("Euler.dat");
    
    for( int i = 0; i < 1000; i++){
        outfile << t << "\t" << y0 << "\t" << y1 << endl;
        t += DeltaT;
        y0 = Euler(t,y0,y1);
        y1 = Euler2(t,y0,y1);
    }
    outfile.close();
    return 0;
}


double f0(double t, double y0, double y1){
  return y1;
}

double f1(double t, double y0, double y1){
  return (-K/M)*pow(y0, LAMBDA);
}

double Euler(double t, double y0, double y1){
    return y0+DeltaT*f0(t,y0,y1);
}

double Euler2(double t, double y0, double y1){
    return y1+DeltaT*f1(t,y0,y1);
}



