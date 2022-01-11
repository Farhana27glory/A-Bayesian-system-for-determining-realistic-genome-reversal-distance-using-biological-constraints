#include "BPGraph.h"


//
//order is the order of the straight edges
//
BPGraph::BPGraph(int* order, int length){  
  
  nbCycles = 0;
  nbGenes = length;
  /////////////////////nameTable=new int[nbGenes+2];

  nbNodes = nbGenes*2+2;
  graph = new int*[nbNodes];
    

  //allocate break point graph
  for(int i=0;i<nbNodes;i++){
    graph[i]=new int[2];
  }

  /*
  cerr<<"Permutation pi:\n";
  for(int i=0;i<length;i++){
    cerr<<order[i]<<" ";
  }
  cerr<<"\n\n";
  */

  //Initializes the curved edges with -1
  eraseCurvedEdges();
 
  //Initializing straight edges
  initEdges(order, _STRAIGHT);
  
}

//
//Initialization of the straight or curved edges
//
void BPGraph::initEdges(int* order, EdgeType et)
{
  //the first rightNode is connected to the left chromosome end (index 0)
  int leftNode = 0;
  int rightNode;
  
  for(int i = 0; i < nbGenes; i++)
  {
    if(order[i] < 0)
      rightNode = -2 * order[i];
    else
      rightNode = (2 * order[i]) - 1;

    //checking the nb of cycles
    if(et == _CURVED)
    {
      if(isConnex(leftNode, rightNode))
	nbCycles++;
    }
    
    //Creating the straight edges
    graph[leftNode][et] = rightNode;
    graph[rightNode][et] = leftNode;

    //Next nodes
    if(order[i] < 0)
      leftNode = rightNode - 1;
    else
      leftNode = rightNode + 1;
  }

  //the last leftNode is connected to the right chromosome end (index nbNodes-1)
  rightNode = nbNodes-1;

  //checking the nb of cycles
  if(et == _CURVED)
  {
    if(isConnex(leftNode, rightNode))
      nbCycles++;
  }

  //Creating the straight edges
  graph[leftNode][et] = rightNode;
  graph[rightNode][et] = leftNode;
}



BPGraph::~BPGraph(){
  for(int i=0;i<nbNodes;i++){
    delete[] graph[i];
  }
  delete[] graph;
  //delete[] nameTable;
}



/*
int BPGraph::addRelation(int min,int max){
  cout<<"addRelation "<<max<<" "<<min<<endl;
  //int min, max;
  //min=nameTable[theMin];
  //max=nameTable[theMax];
  //cout<<"addRelation theMin "<<theMin<<" "<<min<<" theMax "<<theMax<<" "<<max<<endl;
  nbEdges++;
  if(isConnex(2*min,2*max-1)){
    nbCycles++;
  }
  graph[2*min][1]=2*max-1;
  graph[2*max-1][1]=2*min;
  return nbEdges-nbCycles;
  //return (nbGenes+nbCycles+1-nbEdges);
}

void BPGraph::removeRelation(int min,int max){
  cout<<"removeRelation "<<max<<" "<<min<<endl;
  //cout<<"removeRelation ";cin.get();
  //int min, max;
  //min=nameTable[theMin];
  //max=nameTable[theMax];
  nbEdges--;
  if(isConnex(2*min,2*max-1)){
    nbCycles--;
  }
  graph[2*min][1]=-1;
  graph[2*max-1][1]=-1;
}
*/

//
//Erases curved edges
//
void BPGraph::eraseCurvedEdges(){
  nbCycles=0;
  for(int i=0;i<nbNodes;i++)
    graph[i][1]=-1;
}
/*

void BPGraph::getOptimalOrder(int* theOrder){
  
  int currNode = graph[0][1]+1;//curved edge

  theOrder[0]=currNode/2;
  int i=1;
  while(graph[currNode][1]>=0 && graph[currNode][1]<nbNodes-1){    
    currNode = graph[currNode][1]+1; //curved edge   
    theOrder[i]=currNode/2;
    i++;
  }
}
*/

bool BPGraph::isConnex(int nodeA, int nodeB){

  int currNode=graph[nodeA][_STRAIGHT];//straight edge
  int lastNode=nodeB;

  if(currNode==lastNode){
    return true;
  }

  while(graph[currNode][1]>=0){
    //cout<<"et merde"<<endl;
    currNode = graph[currNode][_CURVED];//curved edge
    currNode = graph[currNode][_STRAIGHT];//straight edge
    if(currNode==lastNode){
      return true;
    }
  }
  return false;

}

void BPGraph::printBPGraph(){

 //Print break point graph
  cerr<<"Break point graph:\n";
  for(int i=0;i<nbNodes;i++){
    cerr<<i<<" | "<<graph[i][0]<<" | "<<graph[i][1] <<"\n";
  }
  cerr<<"\n";
}
