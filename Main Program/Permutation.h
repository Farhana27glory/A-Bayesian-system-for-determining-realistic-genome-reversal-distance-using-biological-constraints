#ifndef PERMUTATION_H
#define PERMUTATION_H

#include "BPGraph.h"
#include "vector"
#include "tuple"

using namespace std;

/////////////
//Constants//
/////////////

#define _E1 0.03
#define _E2 0.015
#define _E3 0.0009

//probabilities are 0.955,0.03 and 0.015

enum inversionType{_N1, _N0, _N_1};  //+1, 0, -1

// create a type for the tuple


class Permutation{
  
  
  //////////
  //Fields//
  //////////

private:

  int* permutation;
  int* inteRegions;
  int permutationLength;
  int inteRegionsLength;
 
  int nbReachablePermutations;
  vector<tuple<int*, int, int>>* minus1DeltaCycles;
  vector<tuple<int*, int, int>>* zeroDeltaCycles;
  vector<tuple<int*, int, int>>* plus1DeltaCycles;
  
  
public:
  
  ////////////////
  //Constructors//
  ////////////////
  
  Permutation(int* permut, int* inte_regions, int permutLength);
  
  //
  //To make a copy of a Permutation
  //
  Permutation(Permutation* p);
  
  
  //////////////
  //Destructor//
  //////////////
 
  ~Permutation();
  
  
  /////////////////
  //Const methods//
  /////////////////
 
  
  //
  //To get permutation
  //
  int* getPermutation()const{return permutation;}

  //
  //To get integenic regions
  //
  int* getInteRegions()const{return inteRegions;}
  
  //
  //To get permutationLength
  //
  int getPermutationLength()const{return permutationLength;}

  //
  //
  //
  int getInteRegionsLength()const{return inteRegionsLength;}

  //
  //To get nbReachablePermutations
  //
  int getNbReachablePermutations()const{return nbReachablePermutations;}
  
  //
  //To check if a Permutation object is equal to another
  //
  bool equals(Permutation* p)const;
  
  //
  //To print the permutation
  //
  void printPermutation()const;

  //here I have done my testings
  //void habijabi(Permutation* target);


  ////////////
  //Mutators//
  ////////////


  //
  //To get the inversionLogProb from this to nextPermut, with target as the black edges in the BPGraph
  //
  double getInversionLogProb(Permutation* nextPermut, Permutation* target);

  // function for getting probability for the conservation of intergenics
  //void getLogProbIntergenics()const;
 

  //
  //To perform an inversion on this permutation; returns the result (Permutation) of the chosen inversion 
  //
  Permutation* performInversion(Permutation* target);
  //double performInversion1(Permutation* target);
  double performInversion2(Permutation* target);

  //Permutation* performInversion2(Permutation* target);
  //
  //To fill the vector<tuple<int*, int, int>>s
  //
  void findPermutations(int* target);


  //
  //To fill with the permutation and make the proposed inversion beginning at position 'begin' of 'inverSize' size
  //
  void invert(int begin, int inverSize, int* permut);


  //
  //To put a permutation in the right vector<tuple<int*, int, int>>, based on deltaNbCycles
  //
  void addNewPermutation(int* permut,int begin,int inverSize, int deltaNbCycles);
  

  //
  //To simulate the random cutting on the spacings
  //
  int* invertSpacing(int* intergenicPermut, int intergenicArraySize, int start_pt, int end_pt);


  //
  //To reverse the middle part of the spacings
  //
  void reverseInner(int* permut, int start_pt, int end_pt);
  

};
#endif

