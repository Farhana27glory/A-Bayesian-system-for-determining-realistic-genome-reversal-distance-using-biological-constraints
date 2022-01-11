#ifndef BPGRAPH_H
#define BPGRAPH_H

#include <iostream>
#include <fstream>

enum EdgeType {_STRAIGHT, _CURVED};

using namespace std;
using std::cerr;
using std::cout;

class BPGraph{
 public:
  BPGraph(int* order, int length);
  void initEdges(int* order, EdgeType et);
  ~BPGraph();

  //To get the nb of cycles
  int getNbCycles()const{return nbCycles;}

  //int addRelation(int min,int max); //return nb cycle
  //void removeRelation(int min,int max);
  //void getOptimalOrder(int* theOrder);
  void printBPGraph();
  void eraseCurvedEdges();
  

 private:
  int** graph;
  //int* optimalOrder;
  int nbNodes;
  //int nbEdges;
  int nbCycles;
  int nbGenes;
  //int* nameTable;
  bool isConnex(int min, int max);
  //int map(int node)
};
#endif

