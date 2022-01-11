#ifndef INOUT_H
#define INOUT_H

#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

//
//Eats white space and puts in buffer the first non-white space character
//
void eatSpace(ifstream* input, char* c);


//
//Transforms a string into a double
//
double stringToDouble(string* number);


//
//Transforms a string into an int
//
int stoi(string* number);


#endif
