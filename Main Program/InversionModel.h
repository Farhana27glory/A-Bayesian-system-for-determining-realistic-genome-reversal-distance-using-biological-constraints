#ifndef INVERSION_MODEL_H
#define INVERSION_MODEL_H

#include "Permutation.h"
#include <iostream> 
#include <unistd.h> 
using namespace std; 

class InversionModel{
  
  
  //////////
  //Fields//
  //////////
  
private:

  vector<Permutation*>* inversionPath;
  int permutationLength;
	
public:
 
  ////////////////
  //Constructors//
  ////////////////
  
  InversionModel(int* ancestorOrder, int* ancestorRegions, int* currentOrder, int* currentRegions, int permutLength);
  
  
  //////////////
  //Destructor//
  //////////////
  
  ~InversionModel();
  
  
  /////////////////
  //Const methods//
  /////////////////
 
  
  //
  //To get L, the length of the inversion path
  //
  int getL()const;


  //
  //To print the inversionPath (the permutations)
  //
  void printInversionPath()const;
  
  
  ////////////
  //Mutators//
  ////////////
  
 
  //
  //Resample
  //
  
  void resample();
  
 
};
#endif

