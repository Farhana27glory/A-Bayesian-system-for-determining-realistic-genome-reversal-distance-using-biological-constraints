#ifndef RANDOM_H
#define RANDOM_H

#include <stdlib.h>
#include <math.h>

//
//Finite discrete
//
int finiteDiscrete(int range, double* probArr);


//
//Uniform finite discrete
//
int uniformFiniteDiscrete(int range);


//
//Uniform between [0,1[
//
double uniform();

#endif
