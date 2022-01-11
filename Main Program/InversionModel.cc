#include "InversionModel.h"
#include "Random.h"
#include <array>
#include <iostream>
#include <fstream>
#include <cmath>

////////////////
//Constructors//
////////////////

InversionModel::InversionModel(int* ancestorOrder, int* ancestorRegions, int* currentOrder, int* currentRegions, int permutLength)
{
  //Initializing the seed
  int seed;
  seed  = time(NULL) + getpid();
  //cerr<<"Seed = "<<seed<<endl;
  srand(seed);
  //

  permutationLength = permutLength;

  //Creating the first inversion path
  inversionPath = new vector<Permutation*>();

  Permutation* p = new Permutation(ancestorOrder, ancestorRegions, permutationLength);
  Permutation* target = new Permutation(currentOrder, currentRegions, permutationLength);
  // Permutation* p = new Permutation(ancestorOrder, permutationLength);
  // Permutation* target = new Permutation(currentOrder, permutationLength);


  do
  {
    inversionPath->push_back(p);
    p = p->performInversion(target);
  }
  while(p != NULL);

  
  //printInversionPath();
  

  delete target;
}


//////////////
//Destructor//
//////////////
 
InversionModel::~InversionModel()
{
  while(!inversionPath->empty())
  {
    delete inversionPath->back();
    inversionPath->pop_back();
  }
  delete inversionPath;
}



/////////////////
//Const methods//
/////////////////
 

//
//To get L, the length of the inversion path
//
int InversionModel::getL()const
{
  return inversionPath->size() - 1;
}


//
//To print the inversionPath (the permutations)

void InversionModel::printInversionPath()const
{
  int size = inversionPath->size();
  //cout<<"\"";
  for(int i = 0; i < size; i++)
  {
    //return (*inversionPath)[i]->printPermutation();
    
    (*inversionPath)[i]->printPermutation();
    cout<<"->";
  }
  //cout<<"\""<<","<<endl;
  cout<<"\t";
}
/*
void InversionModel::printInversionPath()const
{
  int size = inversionPath->size();
  for(int i = size-1; i > size-2; i--)
  {
    //return (*inversionPath)[i]->printPermutation();
    (*inversionPath)[i]->printPermutation();
    cout<<endl;
  }
}
*/

////////////
//Mutators//
////////////

//
//Resample
//
void InversionModel::resample()
{
  //Choosing uniformly at random the length of the path to be resampled
  //int length = uniformFiniteDiscrete(getL()) + 1;  // + 1 so that length = 0 is never chosen

  // cerr<<"In resample, chosen length = "<<length<<endl;

  //Choosing uniformly at random the starting permutation in the inversion path
  //int startIndex = uniformFiniteDiscrete(getL()-length+1);
  
  //int pivotpoint = getL();
  
  // we are compelling our system to start from a random index and end to the end point of the path
  int startIndex = rand() % getL();   
  int length = getL() - startIndex; 
  if(length == 0)
  {
    startIndex = getL() - 1; 
    length = 1;
    //cout<<"Path length = "<<pivotpoint<<endl;
    //cout<<"In resample, chosen start point = "<<startIndex<<endl;
    //cerr<<"In resample, chosen length = "<<length<<endl;
  }
  else
  { 
    //cout<<"Path length = "<<pivotpoint<<endl;
    //cout<<"In resample, chosen start point = "<<startIndex<<endl;
    //cout<<"In resample, chosen length = "<<length<<endl;
  }

  // cerr<<"and startIndex = "<<startIndex<<endl;
  //printInversionPath();
  vector<Permutation*>* newPath = new vector<Permutation*>();
  Permutation* p = new Permutation((*inversionPath)[startIndex]);
  Permutation* target = (*inversionPath)[startIndex+length];
  
  do
  {
    newPath->push_back(p);
    /*
    int lengthPmt = p->getPermutationLength();
    int* tmpPmt = p->getPermutation();
    cout<<"P: "<<endl;
    for(int i=0;i<lengthPmt;i++){
       cout<<" "<<tmpPmt[i];
    }
    cout<<endl;
    */
    p = p->performInversion(target);
    
    //printInversionPath();
    
  }
  while(p != NULL);

  
  //printInversionPath();

  
  //Computing acceptance probability//
  int newLength = newPath->size()-1;

  //cout<<endl;
  //cout << "new length is: " << newLength << endl;
 //cout << "Permutation length " << permutationLength << endl;
  
  //Computing qOld and qNew
  //Computing qOld and qNew
  double qOld = 0; double qNew = 0;
  double problty1= 0;
  double problty2= 0;
  int i = 0;
  while((i < newLength) || ((startIndex+i) < (startIndex + length)))
  {  
    
    if(i < newLength)
      problty1 = ((*newPath)[i]->getInversionLogProb((*newPath)[i+1], (*newPath)[newLength])) *(0.9999*(i+0.9999)/(length)) *((*newPath)[i]->performInversion2((*newPath)[newLength]));
      qNew += (log(problty1));
      //problty1 = ((*newPath)[i]->getInversionLogProb((*newPath)[i+1], (*newPath)[newLength])) *(0.9999*(i+0.9999)/(getL()+newLength-length)) *((*newPath)[i]->performInversion2((*newPath)[newLength]));
      //qNew += (log(problty1));
      //qNew += ((*newPath)[i]->getInversionLogProb((*newPath)[i+1], (*newPath)[newLength])) +((*newPath)[i]->performInversion2((*newPath)[newLength]));
      //cerr<<i<<endl;
      //test = (*newPath)[i]->getLogProbIntergenics((*newPath)[i+1], (*newPath)[newLength]);
      //cerr<<problty1<<endl;
      //cerr<<"qNew = "<<qNew<<endl;
    if((startIndex+i) < (startIndex + length))
      problty2 += ((*inversionPath)[startIndex+i]->getInversionLogProb((*inversionPath)[startIndex+i+1], 
      (*inversionPath)[startIndex+length])) * (0.9999*(i+0.9999)/(length))*
      ((*inversionPath)[startIndex+i]->performInversion2((*inversionPath)[startIndex+length]));
      qOld += (log(problty2));
      /*
      problty2 += ((*inversionPath)[startIndex+i]->getInversionLogProb((*inversionPath)[startIndex+i+1], 
      (*inversionPath)[startIndex+length])) * (0.9999*(i+0.9999)/(getL()+newLength-length))*
      ((*inversionPath)[startIndex+i]->performInversion2((*inversionPath)[startIndex+length]));
      qOld += (log(problty2));
      */   
      //qOld += ((*inversionPath)[startIndex+i]->getInversionLogProb((*inversionPath)[startIndex+i+1], (*inversionPath)[startIndex+length]))+
      //((*inversionPath)[startIndex+i]->performInversion2((*inversionPath)[startIndex+length]))+log(1*(i+1)/(length));
      //cerr<<problty2<<endl;
    i++;
  }
  
  
  double acceptanceProb = 0;
  //Upper bound for the length of the inversion path
  if((getL() + newLength - length) <= 100)
    //acceptanceProb = ((double)getL()/(getL()+newLength-length)) * exp(qOld - qNew) * exp(log(getL()) - log(getL() + newLength - length));
    //acceptanceProb = ((double)getL()/(getL()+newLength-length)) * exp(qOld - qNew) * exp(log(getL()) - log(getL() + newLength - length) * (log(permutationLength) + log(permutationLength+1) - log(2)));
    acceptanceProb = ((double)getL()/(getL()+newLength-length)) * exp(qOld - qNew) * exp(log(getL()) - log(getL() + newLength - length) + (length-newLength) * (log(permutationLength) + log(permutationLength+1) - log(2)));
  
  
  //cerr<<"qNew = "<<qNew<<endl;
  //cerr<<"exp(qOld - qNew) = "<<exp(qOld - qNew)<<endl;
  //cerr<<"newLength = "<<newLength<<" and length = "<<length<<endl;
  //cerr<<"((double)getL()/(getL()+newLength-length)) = "<<((double)getL()/(getL()+newLength-length))<<endl;
  //cerr<<"exp(log(getL()) - log(getL() + newLength - length) + (length-newLength) * (log(permutationLength) + log(permutationLength+1) - log(2))) = ";
  //cerr<<exp(log(getL()) - log(getL() + newLength - length) + (length-newLength) * (log(permutationLength) + log(permutationLength+1) - log(2)))<<endl;
  //cout<<"Acceptance probability = "<<acceptanceProb<<endl;
  //double qq =0;
  if(uniform() < acceptanceProb)  //If we accept, we change the old path in inversionPath for the newPath; else, nothing changes
  { 
    //Removing the old part of inversionPath --> I don't need to replace the first permutation anymore (because inversionLogProb isn't a field anymore), but I didn't change it
     for(int j = startIndex; j < startIndex+length+1; j++)
     {
       delete (*inversionPath)[j];
     }
     vector<Permutation*>::iterator iter = inversionPath->erase(inversionPath->begin() + startIndex, inversionPath->begin() + startIndex + length+1);  //second position is excluded
     inversionPath->insert(iter, newPath->begin(), newPath->begin() + newLength+1);  //the last permutation isn't inserted, the old one is kept
     //nature_print(qNew);
     //MyFile1<<qNew<<endl;
     //cerr<<endl;
     //cerr<<qNew*((double)getL()/(getL()+newLength-length))<<endl;
     //cerr<<qNew<<endl;
     //cerr<<"Qold = "<<qNew/(log(getL() - newLength + length))<<endl;
     //cerr<<-(qNew - qOld) <<endl;
     //cerr<<"Acceptance probability = "<<acceptanceProb<<endl;
     //cerr<<"length = "<<getL()<<endl;
     //nature(qq);
    //Deleting only the last permutation of newPath
     //delete newPath->back();
     //delete newPath;
    
  
  }


  else  //the permutations of newPath must be deleted
  {
    while(!newPath->empty())
    {
      delete newPath->back();
      newPath->pop_back();
    }
    delete newPath;
    //cerr<<endl;
    //cerr<<qOld*((double)getL()/(getL()+newLength-length))<<endl;
    //cerr<<qOld<<endl;
    //cerr<<"Qold = "<<qOld /(log(getL() - newLength +length))<<endl;
    //cerr<<-(qOld-qNew)<<endl;
    //cerr<<"Acceptance probability = "<<acceptanceProb<<endl;
    //cerr<<"length = "<<getL()<<endl;
    //MyFile1<<qOld<<endl;
    
  }
  
  //cout<<endl;
  
  printInversionPath();
  
}


