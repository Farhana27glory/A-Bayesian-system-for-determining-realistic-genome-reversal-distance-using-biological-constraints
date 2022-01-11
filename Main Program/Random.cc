#include "Random.h"


//
//Finite discrete
//
int finiteDiscrete(int range, double* probArr)
{
  double random = uniform();

  double sum = 0;
  int i = -1;
  while ((i<range) && (sum<random))
  {
    i++;
    sum += probArr[i];
  }

  return i;
}


//
//Uniform finite discrete
//
int uniformFiniteDiscrete(int range)
{
  return (int)(uniform() * range);
}


//
//Uniform between [0,1[
//
double uniform()
{
  return (double)rand()/((double)RAND_MAX + 1);
}
