#include <list>
#include <iostream>
#include <fstream>

using namespace std;

struct SingleStep
{
    char* fullPermut;
};

class PathRC{
    
    public:
        PathRC(int pID, char* permut);
        ~PathRC();
        void addStep(char* permut);
        void recordPath();

        int pathID;

};