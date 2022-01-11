#include "InOut.h"

//
//Eats white space and puts in buffer the first non-white space character
//
void eatSpace(ifstream* input, char* c)
{
  do
  {
    input->read(c, 1);
    //cerr<<"c = "<<*c<<","<<endl;
  }
  while((!input->eof()) && ((*c) == ' ' || (*c) == '\t' || (*c) == '\n' || (*c) == '\r'));
}


//
//Transforms a string into a double
//
double stringToDouble(string* number)
{
  double res;
  istringstream is( *number );
  is >> res;
  return res;
}


//
//Transforms a string into an int
//
int stoi(string* number)
{
  return (int) stringToDouble(number);
}


