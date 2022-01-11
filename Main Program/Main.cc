#include "BPGraph.h"
#include "InversionModel.h"
#include "InOut.h"
#include <ctime>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{

  if(argc < 3)
  {
    cerr<<"USAGE : ./main  filename  K  [burnin]"<<endl;
    exit(0);
  }


  //Reading the input file
  int permutLength = 0;
  int indexPermut = 0;
  int indexInteR = 0;
  int* permut1;
  int* permut2;
  int* inteRegions1;
  int* inteRegions2;


  // different types of input files

  //ifstream* in = new ifstream(argv[1]);
  //ifstream* in = new ifstream("testaaa.txt");
  //ifstream* in = new ifstream("testbbb.txt");
  //ifstream* in = new ifstream("testccc.txt");
  //ifstream* in = new ifstream("testddd.txt");
  //ifstream* in = new ifstream("testeee.txt");
  //ifstream* in = new ifstream("testfff.txt");
  //ifstream* in = new ifstream("testggg.txt");
  //ifstream* in = new ifstream("testhhh.txt");
  //ifstream* in = new ifstream("testiii.txt");
  //ifstream* in = new ifstream("testuuu.txt");
  ifstream* in = new ifstream("testvvv.txt");
  //ifstream in("testaaa.txt");
  
  char* c = new char();
  string* s = new string();

  //reading the permutation length
  eatSpace(in, c);
  do
  {
    s->append(1, (*c));
    in->read(c, 1);
  }
  while((*c) != ' ' && (*c) != '\n' && (*c) != '\t' && (*c) != '\r' && !in->eof());
  
  permutLength = stoi(s);
  s->clear();
  permut1 = new int[permutLength];
  inteRegions1 = new int[permutLength+1];
  permut2 = new int[permutLength];
  inteRegions2 = new int[permutLength+1];
  
  //reading the first permutation
  for(int i = 0; i < (2*permutLength)+1; i++)
  {
    eatSpace(in, c);
    //cout << "permut1, ";
    if((*c) == '*'){
      in->read(c, 1);
      while((*c) != ' ' && (*c) != '\n' && (*c) != '\t' && (*c) != '\r' && !in->eof()){
        s->append(1, (*c));
        in->read(c, 1);
      }
      inteRegions1[indexInteR] = stoi(s);
      //cout << "I: "+(*s) << endl;
      s->clear();
      indexInteR++;
    }else{
      while((*c) != ' ' && (*c) != '\n' && (*c) != '\t' && (*c) != '\r' && !in->eof()){
        s->append(1, (*c));
        in->read(c, 1);
      }
      permut1[indexPermut] = stoi(s);
      //cout << "G: "+(*s) << endl;
      s->clear();
      indexPermut++;
    }
  }

  //reading the second permutation
  indexPermut = 0;
  indexInteR = 0;
  for(int i = 0; i < (2*permutLength)+1; i++)
  {
    eatSpace(in, c);
    //cout << "permut2, ";
    if((*c) == '*'){
      in->read(c, 1);
      while((*c) != ' ' && (*c) != '\n' && (*c) != '\t' && (*c) != '\r' && !in->eof()){
        s->append(1, (*c));
        in->read(c, 1);
      }
      inteRegions2[indexInteR] = stoi(s);
      //cout << "I: "+(*s) << endl;
      s->clear();
      indexInteR++;
    }else{
      while((*c) != ' ' && (*c) != '\n' && (*c) != '\t' && (*c) != '\r' && !in->eof()){
        s->append(1, (*c));
        in->read(c, 1);
      }
      permut2[indexPermut] = stoi(s);
      //cout << "G: "+(*s) << endl;
      s->clear();
      indexPermut++;
    }
  }

  delete s;
  delete c;
  in->close();
  delete in;

  int K = atoi(argv[2]);
  int burnin = 0;

  if(argc > 3)
    burnin = atoi(argv[3]);

  InversionModel* invmod = new InversionModel(permut1, inteRegions1, permut2, inteRegions2, permutLength);
  
  //Burnin
  for(int b = 0; b < burnin; b++)
  {
    invmod->resample();
  }

  //Repetitions
  double mean = 0;
  ofstream MyFile;
  ofstream ofs("nature.txt");
  streambuf* oldrdbuf = cerr.rdbuf(ofs.rdbuf());
  MyFile.open("result.txt");
  MyFile<<"Start time: "<<(float)clock()/(float)CLOCKS_PER_SEC<<" sec.\n";
  ofstream out("outputtest.txt");
  auto *coutbuf = cout.rdbuf();
  cout.rdbuf(out.rdbuf());
  float start_t = (float)clock()/(float)CLOCKS_PER_SEC;
  for(int nRep = 0; nRep < K; nRep++)
  {
    
    invmod->resample(); 
    MyFile<<invmod->getL()<<endl;
    mean += invmod->getL();
    //cout<<endl;
    
    //cout << invmod->getL() << endl;
  }
  cerr.rdbuf(oldrdbuf);
  MyFile<<"End time: "<<(float)clock()/(float)CLOCKS_PER_SEC<<" sec.\n";
  MyFile<<"Time: "<<((float)clock()/(float)CLOCKS_PER_SEC)-start_t<<" sec.\n";
  cout<<"Time: "<<((float)clock()/(float)CLOCKS_PER_SEC)-start_t<<" sec.\n";
  //Printing the mean
  mean = mean/K;
  MyFile<<"Mean of L = "<<mean<<endl;

  delete invmod;
  MyFile.close();
  
}
