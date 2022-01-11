#include "Permutation.h"
#include "Random.h"
#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>

// for debugging

////////////////
//Constructors//
////////////////

Permutation::Permutation(int* permut, int* inte_regions, int permutLength)
{
  permutation = permut;
  inteRegions = inte_regions;
  permutationLength = permutLength;
  inteRegionsLength = permutLength+1;
  minus1DeltaCycles = new vector<tuple<int*, int, int>>();
  zeroDeltaCycles = new vector<tuple<int*, int, int>>();
  plus1DeltaCycles = new vector<tuple<int*, int, int>>();

  nbReachablePermutations = permutationLength * (permutationLength + 1) / 2;
}

//
//To make a copy of a Permutation
//
Permutation::Permutation(Permutation* p)
{
  permutationLength = p->getPermutationLength();
  permutation = new int[permutationLength];
  for(int i = 0; i < permutationLength; i++)
  {
    permutation[i] = p->getPermutation()[i];
  }
  inteRegionsLength = p->getInteRegionsLength();
  inteRegions = new int[inteRegionsLength];
  for(int i = 0; i < inteRegionsLength; i++){
    inteRegions[i] = p->getInteRegions()[i];
  }

  minus1DeltaCycles = new vector<tuple<int*, int, int>>();
  zeroDeltaCycles = new vector<tuple<int*, int, int>>();
  plus1DeltaCycles = new vector<tuple<int*, int, int>>();

  nbReachablePermutations = p->getNbReachablePermutations();
}


//////////////
//Destructor//
//////////////

Permutation::~Permutation()
{
  //cerr<<"deleting permutation : "<<permutation<<endl;
  delete[] permutation;
  delete[] inteRegions;
  
  while(!minus1DeltaCycles->empty())
  {
    //cerr<<"deleting array : "<<minus1DeltaCycles->back()<<endl;
    int* tmpPermut = std::get<0>(minus1DeltaCycles->back());
    delete[] tmpPermut;
    minus1DeltaCycles->pop_back();
  }
  delete minus1DeltaCycles;
  
  while(!zeroDeltaCycles->empty())
  {
    //cerr<<"deleting array : "<<zeroDeltaCycles->back()<<endl;
    int* tmpPermut = std::get<0>(zeroDeltaCycles->back());
    delete[] tmpPermut;
    zeroDeltaCycles->pop_back();
  }
  delete zeroDeltaCycles;
  
  while(!plus1DeltaCycles->empty())
  {
    //cerr<<"deleting array : "<<plus1DeltaCycles->back()<<endl;
    int* tmpPermut = std::get<0>(plus1DeltaCycles->back());
    delete[] tmpPermut;
    plus1DeltaCycles->pop_back();
  }
  delete plus1DeltaCycles;
}


/////////////////
//Const methods//
/////////////////
 
//
//To check if a Permutation object is equal to another
//
bool Permutation::equals(Permutation* p)const
{
  int* otherPermut = p->getPermutation();
  
  if(permutationLength != p->getPermutationLength())
    return false;
  
  for(int i = 0; i < permutationLength; i++)
  {
    if(permutation[i] != otherPermut[i])
      return false;
  }
  return true;
}


//
//To print the permutation
//
void Permutation::printPermutation()const
{
  //cout<<"\""<<"->";
  for(int i = 0; i< inteRegionsLength; i++)
  {
    cout<<"*"<<inteRegions[i]<<",";
    if(i < permutationLength)
    {
      cout<<permutation[i]<<",";
      //cout<<"("<<permutation[i]<<")";
    }
  }
  //cout<<"\""<<",";
 
}



////////////
//Mutators//
////////////



//
//To get the inversionLogProb from this to nextPermut, with target as the black edges in the BPGraph
//
double Permutation::getInversionLogProb(Permutation* nextPermut, Permutation* target)
{
  //The current nb of cycles
  BPGraph* bpg = new BPGraph(target->getPermutation(), permutationLength);
  bpg->initEdges(permutation, _CURVED);
  int currentNbCycles = bpg->getNbCycles();

  //To compute the nb of every type of inversion (+1, 0, -1 deltaNbCycles)
  int inverSize = 1;
  int i = 0;
  int* nbInversionType = new int[3];
  for(int k = 0; k < 3; k++)
    nbInversionType[k] = 0;

  while(i < nbReachablePermutations)
  {
    for(int begin = 0; (begin+inverSize-1) < permutationLength; begin++)
    {
      int* newPermut = new int[permutationLength];
      invert(begin, inverSize, newPermut);

      //Computing the difference in the number of cycles after making this inversion
      bpg->eraseCurvedEdges();
      bpg->initEdges(newPermut, _CURVED);
      int deltaNbCycles = bpg->getNbCycles() - currentNbCycles;
      
      //Incrementing nbInversionType
      if(deltaNbCycles == 1)
	nbInversionType[_N1]++;
      else if(deltaNbCycles == 0)
	nbInversionType[_N0]++;
      else if(deltaNbCycles == -1)
	nbInversionType[_N_1]++;
      else
	cerr<<"Big problem : deltaNbCycles != +1, 0 or 1"<<endl;
      
      i++;
      delete[] newPermut;
    }
    inverSize++;
  }

  //Checking in which category nextPermut falls into
  bpg->eraseCurvedEdges();
  bpg->initEdges(nextPermut->getPermutation(), _CURVED);
  int deltaNbCycles = bpg->getNbCycles() - currentNbCycles;

  delete bpg;
  
  double theProb = 0;
  double* probs = new double[3];

  if(nbInversionType[_N1] == 0)
    probs[_N1] = 0;
  else
    probs[_N1] = 1;

  if(nbInversionType[_N0] == 0)
    probs[_N0] = 0;
  else
    probs[_N0] = _E1;

  if(nbInversionType[_N_1] == 0)
    probs[_N_1] = 0;
  else
    probs[_N_1] = _E2;

  if(deltaNbCycles == 1)
    theProb = probs[_N1] / (probs[_N1] + probs[_N0] + probs[_N_1]) / nbInversionType[_N1];
  else if(deltaNbCycles == 0)
    theProb = probs[_N0] / (probs[_N1] + probs[_N0] + probs[_N_1]) / nbInversionType[_N0];
  else if(deltaNbCycles == -1)
    theProb = probs[_N_1] / (probs[_N1] + probs[_N0] + probs[_N_1]) / nbInversionType[_N_1];

  //Cleaning
  delete[] nbInversionType;
  delete[] probs;

  //Checking if we must add E3 to theProb
  if(equals(target))
    theProb *= _E3;
  
  //cerr<<"The Prob is: "<< theProb<<endl;

  return (theProb);
}



//
//To perform an inversion on this permutation; returns the result (Permutation) of the chosen inversion 
//
Permutation* Permutation::performInversion(Permutation* target)
{
  //If the permutations are equal, we might stop (and return NULL) or we might perform another inversion
  if(equals(target))
  {
    if(uniform() > _E3)
      return NULL;
    //cerr<<"Continuing after reaching target!!!"<<endl;
  }
  
  findPermutations(target->getPermutation());

  double* probArray = new double[3];
  double e0, e1, e2;  //e0 is the prob of choosing deltaCycles = +1, e1 -> 0, e2 -> -1
  
  int *numArray;
  int *numArray2;
  numArray = new int[2*permutationLength +1];
  numArray2 = new int[permutationLength -1];
  //Not pretty...
  if(plus1DeltaCycles->empty())
    e0 = 0;
  else
    e0 = 1;

  if(zeroDeltaCycles->empty())
    e1 = 0;
  else
    e1 = _E1;

  if(minus1DeltaCycles->empty())
    e2 = 0;
  else
    e2 = _E2;

  probArray[0] = e0/(e0 + e1 + e2);
  probArray[1] = e1/(e0 + e1 + e2);
  probArray[2] = e2/(e0 + e1 + e2);
  
  int chosen = finiteDiscrete(3, probArray);

  Permutation* p = NULL;

  if(chosen == 0)  //deltaCycles = + 1 has been chosen
  {
    int size = plus1DeltaCycles->size();
    int chosenIndex = uniformFiniteDiscrete(size);
    int bg = std::get<1>((*plus1DeltaCycles)[chosenIndex]);
    int ed = std::get<2>((*plus1DeltaCycles)[chosenIndex]);
    int* inteRegions_n = invertSpacing(inteRegions,inteRegionsLength,bg,ed);
    p = new Permutation(std::get<0>((*plus1DeltaCycles)[chosenIndex]), inteRegions_n, permutationLength);
    plus1DeltaCycles->erase(plus1DeltaCycles->begin()+chosenIndex);  //removing the chosen permutation from the vector (because ~Permutation() will delete it)
    
 

  }
  else if(chosen == 1)  //deltaCycles = 0 has been chosen
  {
    int size = zeroDeltaCycles->size();
    int chosenIndex = uniformFiniteDiscrete(size);
    int bg = std::get<1>((*zeroDeltaCycles)[chosenIndex]);
    int ed = std::get<2>((*zeroDeltaCycles)[chosenIndex]);
    int* inteRegions_n = invertSpacing(inteRegions,inteRegionsLength,bg,ed);
    p = new Permutation(std::get<0>((*zeroDeltaCycles)[chosenIndex]), inteRegions_n, permutationLength);
    zeroDeltaCycles->erase(zeroDeltaCycles->begin()+chosenIndex);  //removing the chosen permutation from the vector (because ~Permutation() will delete it)
  
    
    
  }
  else if(chosen == 2)  //deltaCycles = - 1 has been chosen
  {
    int size = minus1DeltaCycles->size();
    int chosenIndex = uniformFiniteDiscrete(size);
    int bg = std::get<1>((*minus1DeltaCycles)[chosenIndex]);
    int ed = std::get<2>((*minus1DeltaCycles)[chosenIndex]);
    int* inteRegions_n = invertSpacing(inteRegions,inteRegionsLength,bg,ed);
    p = new Permutation(std::get<0>((*minus1DeltaCycles)[chosenIndex]), inteRegions_n, permutationLength);
    minus1DeltaCycles->erase(minus1DeltaCycles->begin()+chosenIndex);  //removing the chosen permutation from the vector (because ~Permutation() will delete it)
    
    
  }
  else
    cerr<<"-----Big problem with finiteDiscrete(3, probArray)"<<endl;
  
  
  delete[] probArray;
  return p;

  
}

double Permutation::performInversion2(Permutation* target)
{
  //If the permutations are equal, we might stop (and return NULL) or we might perform another inversion
  if(equals(target))
  {
    if(uniform() > _E3)
      return NULL;
    //cerr<<"Continuing after reaching target!!!"<<endl;
  }
  
  findPermutations(target->getPermutation());

  double* probArray = new double[3];
  double e0, e1, e2;  //e0 is the prob of choosing deltaCycles = +1, e1 -> 0, e2 -> -1
  
  int *numArray;
  int *numArray2;
  numArray = new int[2*permutationLength +1];
  numArray2 = new int[permutationLength -1];
  //Not pretty...
  if(plus1DeltaCycles->empty())
    e0 = 0;
  else
    e0 = 1;

  if(zeroDeltaCycles->empty())
    e1 = 0;
  else
    e1 = _E1;

  if(minus1DeltaCycles->empty())
    e2 = 0;
  else
    e2 = _E2;

  probArray[0] = e0/(e0 + e1 + e2);
  probArray[1] = e1/(e0 + e1 + e2);
  probArray[2] = e2/(e0 + e1 + e2);
  
  int chosen = finiteDiscrete(3, probArray);

  Permutation* p = NULL;
  double total = 0.0;
  double e,f =0.0;
  double m = 0.0;
  int gene_adjacency_number = 2*(permutationLength - 1);
  int* A = new int[gene_adjacency_number * 3];
  ifstream fp("adjvvv.txt");
  if (! fp) {
    cout << "Error, file couldn't be opened" << endl; 
    return 1; 
  } 
    // this is for reading and opening existing file sudoku.txt
  for(int row = 0; row < gene_adjacency_number; row++){
      for(int column = 0; column < 3; column++){
            fp >> *(A + row*3 + column);
            // from fp we read the characters
        }
  }
  
  fp.close();

  if(chosen == 0)  //deltaCycles = + 1 has been chosen
  {
    int size = plus1DeltaCycles->size();
    int chosenIndex = uniformFiniteDiscrete(size);
    int bg = std::get<1>((*plus1DeltaCycles)[chosenIndex]);
    int ed = std::get<2>((*plus1DeltaCycles)[chosenIndex]);
    int* inteRegions_n = invertSpacing(inteRegions,inteRegionsLength,bg,ed);
    p = new Permutation(std::get<0>((*plus1DeltaCycles)[chosenIndex]), inteRegions_n, permutationLength);
    plus1DeltaCycles->erase(plus1DeltaCycles->begin()+chosenIndex);  //removing the chosen permutation from the vector (because ~Permutation() will delete it)
    //inversionLogProb = log(probArray[0]/size);
    int* array2 = p->getPermutation();
    //cout<<endl;
    
    //int *numArray;
    //int *numArray2;

    for (int f=0; f < permutationLength; f++) 
    {       
      //cout <<array2[f] << " ";    
    }
    //cout<<endl;

    for (int f=0; f < permutationLength+1; f++) 
    {       
      //cout <<inteRegions_n[f] << " ";    
    }
    //cout<<endl;

    //numArray = new int[2*permutationLength +1];
    //numArray2 = new int[permutationLength -1];
    int i = 0, j = 0, k = 0; 
    // Traverse both array 
    while (i<permutationLength+1 && j <permutationLength) 
    { 
        numArray[k++] = inteRegions_n[i++]; 
        numArray[k++] = array2[j++]; 
    } 
  
    // Store remaining elements of first array 
    while (i < permutationLength+1) 
        numArray[k++] = inteRegions_n[i++]; 
  
    // Store remaining elements of second array 
    while (j < permutationLength) 
        numArray[k++] = array2[j++]; 
    
  
    //cout << "The total path with intergenic regions" <<endl; 
    for (i=0; i < permutationLength+1+permutationLength; i++) 
    {       
            //cout <<numArray[i] << " ";    
    }
    //cout<<endl;

    //p = numArray[permutationLength+1+permutationLength];

    for (int n=0; n<permutationLength -1; n++)
    {
      numArray2[n]= inteRegions_n[n+1];
    }

    
    //cout << "without marginal intergenics:" <<endl; 
    for (i=0; i < (permutationLength -1); i++) 
    {       
            //cout <<numArray2[i] << " ";    
    }
    //cout<<endl;
    // for testaaa.txt M, N = 10, 3
    // for testbbb.txt M,N = 4, 3
    // for testccc.txt M,N =
    // for testddd.txt M,N =
    // for testfff.txt M,N =
    // for testhhh.txt M,N =
    // for testiii.txt M,N =
    

    int genes[permutationLength];
    int intergenes[permutationLength-1];
  
    for(int q=0; q<permutationLength; q++)
    {
          genes[q]=array2[q];
          //cout<<genes[q]<<" ";
          
    }
    //cout<<endl;
    for(int s=0; s<permutationLength-1; s++)
    {
          intergenes[s]=inteRegions_n[s+1];
          //cout<<intergenes[s]<<" ";
          
    }

    
    

    for(int k=0; k<permutationLength; k++)
      {
          for (int j=0; j< gene_adjacency_number; j++)
          {
              if (genes[k] == *(A + j*3 + 0))
              {
                  
                  if (genes[k+1] == *(A + j*3 + 1))
                  {
                      f = *(A + j*3 + 2);
                      e = intergenes[k];
                      //cout<<e<<endl;
                      //cout<<f<<endl;
                      if (f==0)
                      {
                         f = 1;
                         e = 0;
                        
                      }
                      else if (e==0 && f==0)
                      {
                        f = 1;
                      }
                      else
                      {
                        /* code */
                      }
                      m = m + double (min(e,f)/max(e,f));
                      //cout<<"\nsum: "<<m<<endl;
                      f=0;
                      e=0;
                  }
                  
                  else
                  {
                    //cout<<"do nothing"<<endl; 
                  }
              }          
              else
              {
                // cout<<"do nothing"<<endl; 
              }          
          }         
      }
      
      //total = double((m/(permutationLength-1))*((permutationLength-1)/2 - 0.005));
      total = double(m/(2*permutationLength-1));
      //cout<<"prob:"<<total<<endl;
      m = 0;
      delete[] A;
    
      //cout<<"Size:"<<array2.size()<<endl;
      //cout<<"Total probability of the conservation of intergenics is: "<<total<<endl;
      //delete[] numArray;
      //delete[] numArray2;

  }
  else if(chosen == 1)  //deltaCycles = 0 has been chosen
  {
    int size = zeroDeltaCycles->size();
    int chosenIndex = uniformFiniteDiscrete(size);
    int bg = std::get<1>((*zeroDeltaCycles)[chosenIndex]);
    int ed = std::get<2>((*zeroDeltaCycles)[chosenIndex]);
    int* inteRegions_n = invertSpacing(inteRegions,inteRegionsLength,bg,ed);
    p = new Permutation(std::get<0>((*zeroDeltaCycles)[chosenIndex]), inteRegions_n, permutationLength);
    zeroDeltaCycles->erase(zeroDeltaCycles->begin()+chosenIndex);  //removing the chosen permutation from the vector (because ~Permutation() will delete it)
    //inversionLogProb = log(probArray[1]/size);
    //cout<<endl;
    int* array2 = p->getPermutation();
    //cout<<endl;
    
    //int *numArray;
    //int *numArray2;

    for (int f=0; f < permutationLength; f++) 
    {       
      //cout <<array2[f] << " ";    
    }
    //cout<<endl;

    for (int f=0; f < permutationLength+1; f++) 
    {       
      //cout <<inteRegions_n[f] << " ";    
    }
    //cout<<endl;
    //numArray = new int[2*permutationLength +1];
    //numArray2 = new int[permutationLength -1];
    int i = 0, j = 0, k = 0; 
    // Traverse both array 
    while (i<permutationLength+1 && j <permutationLength) 
    { 
        numArray[k++] = inteRegions_n[i++]; 
        numArray[k++] = array2[j++]; 
    } 
  
    // Store remaining elements of first array 
    while (i < permutationLength+1) 
        numArray[k++] = inteRegions_n[i++]; 
  
    // Store remaining elements of second array 
    while (j < permutationLength) 
        numArray[k++] = array2[j++]; 
    
  
    //cout << "The total path with intergenic regions" <<endl; 
    for (i=0; i < permutationLength+1+permutationLength; i++) 
    {       
            //cout <<numArray[i] << " ";    
    }
    //cout<<endl;

    for (int n=0; n<permutationLength -1; n++)
    {
      numArray2[n]= inteRegions_n[n+1];
    }

    
    //cout << "without marginal intergenics:" <<endl; 
    for (i=0; i < (permutationLength -1); i++) 
    {       
            //cout <<numArray2[i] << " ";    
    }
    //cout<<endl;
    

    int genes[permutationLength];
    int intergenes[permutationLength-1];
  
    for(int q=0; q<permutationLength; q++)
    {
          genes[q]=array2[q];
          //cout<<genes[q]<<" ";
          
    }
    //cout<<endl;
    for(int s=0; s<permutationLength-1; s++)
    {
          intergenes[s]=inteRegions_n[s+1];
          //cout<<intergenes[s]<<" ";
          
    }

    
    

    for(int k=0; k<permutationLength; k++)
      {
          for (int j=0; j< gene_adjacency_number; j++)
          {
              if (genes[k] == *(A + j*3 + 0))
              {
                  //if (genes[k+1] == A[j][1])
                  if (genes[k+1] == *(A + j*3 + 1))
                  {
                      f = *(A + j*3 + 2);
                      e = intergenes[k];
                      //cout<<e<<endl;
                      //cout<<f<<endl;
                      if (f==0)
                      {
                         f = 1;
                      }
                      else if (e==0 && f==0)
                      {
                        f =1;
                      }
                      else
                      {
                        /* code */
                      }
                      m = m + double (min(e,f)/max(e,f));
                      //cout<<"\nsum: "<<m<<endl;
                      f=0;
                      e=0;
                  }
                  
                  else
                  {
                    //cout<<"do nothing"<<endl; 
                  }
              }          
              else
              {
                // cout<<"do nothing"<<endl; 
              }          
          }         
      }
      
      //total = double((m/(permutationLength-1))*((permutationLength-1)/2 - 0.005));
      total = double(m/(2*permutationLength-1));
      //cout<<"prob:"<<total<<endl;
      m = 0;
      delete[] A;
      
    
    
    
      //cout<<"Size:"<<array2.size()<<endl;
      //cout<<"Total probability of the conservation of intergenics is: "<<total<<endl;
      //delete[] numArray;
      //delete[] numArray2;
    
  }
  else if(chosen == 2)  //deltaCycles = - 1 has been chosen
  {
    int size = minus1DeltaCycles->size();
    int chosenIndex = uniformFiniteDiscrete(size);
    int bg = std::get<1>((*minus1DeltaCycles)[chosenIndex]);
    int ed = std::get<2>((*minus1DeltaCycles)[chosenIndex]);
    int* inteRegions_n = invertSpacing(inteRegions,inteRegionsLength,bg,ed);
    p = new Permutation(std::get<0>((*minus1DeltaCycles)[chosenIndex]), inteRegions_n, permutationLength);
    minus1DeltaCycles->erase(minus1DeltaCycles->begin()+chosenIndex);  //removing the chosen permutation from the vector (because ~Permutation() will delete it)
    //inversionLogProb = log(probArray[2]/size);
    //cout<<endl;
    int* array2 = p->getPermutation();
    //cout<<endl;
    
    //int *numArray;
    //int *numArray2;

    for (int f=0; f < permutationLength; f++) 
    {       
            //cout <<array2[f] << " ";    
    }
    //cout<<endl;

    for (int f=0; f < permutationLength+1; f++) 
    {       
            //cout <<inteRegions_n[f] << " ";    
    }
    //cout<<endl;
    //numArray = new int[2*permutationLength +1];
    //numArray2 = new int[permutationLength -1];
    int i = 0, j = 0, k = 0; 
    // Traverse both array 
    while (i<permutationLength+1 && j <permutationLength) 
    { 
        numArray[k++] = inteRegions_n[i++]; 
        numArray[k++] = array2[j++]; 
    } 
  
    // Store remaining elements of first array 
    while (i < permutationLength+1) 
        numArray[k++] = inteRegions_n[i++]; 
  
    // Store remaining elements of second array 
    while (j < permutationLength) 
        numArray[k++] = array2[j++]; 
    
  
    //cout << "The total path with intergenic regions" <<endl; 
    for (i=0; i < permutationLength+1+permutationLength; i++) 
    {       
            //cout <<numArray[i] << " ";    
    }
    //cout<<endl;

    for (int n=0; n<permutationLength -1; n++)
    {
      numArray2[n]= inteRegions_n[n+1];
    }

    
    //cout << "without marginal intergenics:" <<endl; 
    for (i=0; i < (permutationLength -1); i++) 
    {       
            //cout <<numArray2[i] << " ";    
    }
    //cout<<endl;
    

    int genes[permutationLength];
    int intergenes[permutationLength-1];
  
    for(int q=0; q<permutationLength; q++)
    {
          genes[q]=array2[q];
          //cout<<genes[q]<<" ";
          
    }
    //cout<<endl;
    for(int s=0; s<permutationLength-1; s++)
    {
          intergenes[s]=inteRegions_n[s+1];
          //cout<<intergenes[s]<<" ";
          
    }

    

    for(int k=0; k<permutationLength; k++)
      {
          for (int j=0; j< gene_adjacency_number; j++)
          {
              if (genes[k] == *(A + j*3 + 0))
              {
                  //if (genes[k+1] == A[j][1])
                  if (genes[k+1] == *(A + j*3 + 1))
                  {
                      f = *(A + j*3 + 2);
                      e = intergenes[k];
                      //cout<<e<<endl;
                      //cout<<f<<endl;
                      if (f==0)
                      {
                         f = 1;
                      }
                      else if (e==0 && f==0)
                      {
                        f =1;
                      }
                      else
                      {
                        /* code */
                      }
                      m = m + double (min(e,f)/max(e,f));
                      //cout<<"\nsum: "<<m<<endl;
                      f=0;
                      e=0;
                  }
                  
                  else
                  {
                    //cout<<"do nothing"<<endl; 
                  }
              }          
              else
              {
                // cout<<"do nothing"<<endl; 
              }          
          }         
      }
      
      //total = double((m/(permutationLength-1))*((permutationLength-1)/2 - 0.005));
      total = double(m/(2*permutationLength-1));
      //cout << "prob: "<<total<<endl;
      m = 0;
      delete[] A;
    
    
    
    
      //cout<<"Size:"<<array2.size()<<endl;
      //cout<<"Total probability of the conservation of intergenics is: "<<total<<endl;
      //delete[] numArray;
      //delete[] numArray2;

    
  }
  else
    cerr<<"-----Big problem with finiteDiscrete(3, probArray)"<<endl;
  
  
  delete[] probArray;
  delete[] numArray;
  delete[] numArray2;
  
  //cerr<<endl;
  //cerr << "Intergenic prob: "<<total<<endl;
  //cout<<"Intergenic prob: "<<log(total)<<endl;
  /*
  if (total == 0)
  {
    //total = 0.999999;
    total = 0.0000011;
  }

  else
  {
        //cout<<"do nothing"<<endl;
  }
  */
  return (total);

  
}

// reverse function, only applies to the list containing intergenic regions;
void Permutation::reverseInner(int* permut, int start_pt, int end_pt){
    while (start_pt < end_pt)
    {
        int temp = permut[start_pt];
        permut[start_pt] = permut[end_pt];
        permut[end_pt] = temp;
        start_pt++;
        end_pt--;
    }
}

// only applies to the list containing intergenic regions;
int* Permutation::invertSpacing(int* intergenicPermut, int intergenicArraySize, int start_pt, int end_pt){
    int sum = 0;
    int* intergenicPermut_n = new int[intergenicArraySize];
    // srand((unsigned) time(0));

    for(int i = 0; i < intergenicArraySize; i++){
        intergenicPermut_n[i] = intergenicPermut[i];
    }

    if(start_pt<=end_pt && end_pt<intergenicArraySize){
        sum = intergenicPermut_n[start_pt] + intergenicPermut_n[end_pt+1];
    }
    //cout<<"second index: "<<end_pt<<endl;
    //sum += 1;
    if(sum>0){
      intergenicPermut_n[start_pt] = rand()%sum;
      intergenicPermut_n[end_pt+1] = sum - intergenicPermut_n[start_pt];
    }else{
      intergenicPermut_n[start_pt] = 0;
      intergenicPermut_n[end_pt+1] = 0;
    }

    reverseInner(intergenicPermut_n, start_pt+1, end_pt);
    return intergenicPermut_n;
}

//
//To fill the vector<int*>s
//
void Permutation::findPermutations(int* target)
{
  int inverSize = 1;
  int i = 0;

  /*
  cerr<<"....current permutation.....  ";
  ////////
  for(int m = 0; m < permutationLength; m++)
  {
    cerr<<permutation[m]<<"  ";
  }
  ///////
  cerr<<endl;
  cerr<<"....target permutation.....  ";
  ////////
  for(int m = 0; m < permutationLength; m++)
  {
    cerr<<target[m]<<"  ";
  }
  ///////
  cerr<<endl;
  */

  //Getting the current number of cycles
  BPGraph* bpg = new BPGraph(target, permutationLength);
  bpg->initEdges(permutation, _CURVED);
  int currentNbCycles = bpg->getNbCycles();

  //cerr<<"Current nb of cycles = "<<currentNbCycles<<endl;

  while(i < nbReachablePermutations)
  {
    for(int begin = 0; (begin+inverSize-1) < permutationLength; begin++)
    {
      int* newPermut = new int[permutationLength];
      invert(begin, inverSize, newPermut);
      
      //Computing the difference in the number of cycles after making this inversion
      bpg->eraseCurvedEdges();
      bpg->initEdges(newPermut, _CURVED);
      int deltaNbCycles = bpg->getNbCycles() - currentNbCycles;
      //Adding the new permutation in the right vector
      addNewPermutation(newPermut, begin, inverSize, deltaNbCycles);

      /*
      ////////
      for(int m = 0; m < permutationLength; m++)
      {
	cerr<<newPermut[m]<<"  ";
      }
      ///////
      cerr<<"    deltaNbCycles = "<<deltaNbCycles<<endl;
      */
      
      i++;
    }
    inverSize++;
  }

  delete bpg;
}


//
//To fill with the permutation and make the proposed inversion beginning at position 'begin' of 'inverSize' size
//
void Permutation::invert(int begin, int inverSize, int* permut)
{
  for(int i = 0; i < permutationLength; i++)  //filling permut with the old permutation (permutation before the inversion)
  {
    permut[i] = permutation[i];
  }
  
  int end = begin+inverSize-1;
  
  while(begin < end)  //making the inversion in the array
  {
    int temp = permut[begin];
    permut[begin] = -1 * permut[end];
    permut[end] = -1 * temp;
    begin++;
    end--;
  }
  if(begin == end)
    permut[begin] = -1 * permut[begin];
}


//
//To put a permutation in the right vector<int*>, based on deltaNbCycles
//
void Permutation::addNewPermutation(int* permut,int begin,int inverSize, int deltaNbCycles)
{
  //cerr<<"DeltaNbCycles = "<<deltaNbCycles<<endl;
  //TupleO* tmpPermut = new TupleO(permut,begin,begin+inverSize-1);

  // cout<<"after pushing to vectors, delta: "<<deltaNbCycles<<endl;
  // int* tmpSeq = std::get<0>(tmpPermut);
  // for(int i=0;i<permutationLength;i++){
  //   cout<<tmpSeq[i]<<" ";
  // }
  // cout<<endl;

  if(deltaNbCycles == -1){
    minus1DeltaCycles->push_back(make_tuple(permut,begin,begin+inverSize-1));
    // TupleO* tmpTTT = (*minus1DeltaCycles)[minus1DeltaCycles->size()-1];
    // int* testSeq = std::get<0>(*tmpTTT);
    // for(int i=0;i<permutationLength;i++){
    //   cout<<testSeq[i]<<" ";
    // }
    // cout<<endl;
  }
  else if(deltaNbCycles == 0){
    zeroDeltaCycles->push_back(make_tuple(permut,begin,begin+inverSize-1));
  }
  else if(deltaNbCycles == 1){
    plus1DeltaCycles->push_back(make_tuple(permut,begin,begin+inverSize-1));
  }
  else
  {
    cerr<<"-----Big problem : deltaNbCycles is not -1, 0 or +1"<<endl; cin.get();
  }
}
