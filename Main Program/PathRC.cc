#include "PathRC.h"

list<SingleStep> path;

// Constructor, pID->pathID created outside;
// permut->the original/first permutation in the path.
PathRC::PathRC(int pID, char* permut){
    pathID = pID;
    SingleStep tmpPermut = {
        permut
    };
    path.push_back(tmpPermut);
}

// Destructor
PathRC::~PathRC(){
    for(int i=0; i<path.size(); i++){
        path.pop_back();
    }
    while(!path.empty()){
        delete &path.back();
        path.pop_back();
    }
    delete &path;
}

// adding steps(intermediate/final permutation) on the path.
void PathRC::addStep(char* permut){
    SingleStep tmpPermut = {
        permut
    };
    path.push_back(tmpPermut);
}

// Recording the path to a new created file;
// File name is based on the pathID;
void PathRC::recordPath(){
    std::ofstream ofs;
    ofs.open (pathID+".txt", std::ofstream::out | std::ofstream::app);

    ofs << ""+pathID;
    for(int i=0; i<path.size(); i++){
        ofs << path.begin()->fullPermut;
        path.pop_front();
    }

    ofs.close();
}
