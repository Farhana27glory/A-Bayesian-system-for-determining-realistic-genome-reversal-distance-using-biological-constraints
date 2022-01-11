#include <cmath>
#include <iostream>
#include <fstream>
#include <string>


using namespace std;

const long MAX_NUM = 80000000;
string words[MAX_NUM];
int instances[MAX_NUM];
int number = 0;

void insert(string input) {
	//check first, add if not present
	for (int i = 0; i < number; i++)
        if (input == words[i]) {
            instances[i]++;
            return;
        }

	if (number < MAX_NUM) {
		words[number] = input;
		instances[number] = 1;
		number++;
	}
	else
		cerr << "Too many unquie words in the file";
}

int findTop(string &word) {
	//int topIndex = 0;
	int topCount = instances[0];
	int topIndex = 0;

	for (int i = 1; i< number; i++)
        if (instances[i] > topCount) {
            topCount = instances[i];
            topIndex = i;
        }

	instances[topIndex] = 0;
	word = words[topIndex];
	//topIndex = i;
	return topCount;
}

int main()
{
	string word;
	int myint4 = 0;
	ifstream data("outputtest.txt");
	while (data >> word)
		insert(word);

	int topCount = 0;
	ofstream myfile1;
	ofstream myfile2;
	ofstream myfile3;
	ofstream myfile4;
	ofstream myfile5;
	myfile4.open ("Top_25_results.txt");
	myfile5.open ("Top_40_results.txt");
	for (int i = 0; i < 26; i++)
	{
	    //if (instances[i]>0)
		   //cout << words[i] << " " << instances[i] << endl;
	         //cout << instances[i] << " times\n"<< words[i] <<endl;
		if (i < 25)
	    {
			myint4 = findTop(word);
			myfile4 << myint4 <<" times, "<< "Posterior Probability is: "<< double((myint4/50.0) * 100.0) << "%" << "\n" << word << endl;
			myfile5 << myint4 <<" times, "<< "Posterior Probability is: "<< double((myint4/50.0) * 100.0) << "%" << "\n" << word << endl;
			//myfile4 << findTop(word) <<"times \n"<< word << endl;
			//myfile5 << findTop(word) <<"times \n"<< word << endl;
		}	
	}	
		
	myfile4.close();
	myfile5.close();
	return 0;

}