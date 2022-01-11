flag= -std=c++11 -c -Wall -g -fno-inline 
#flag= -static -c -Wall -O3
#flag= -static -std=c++11 -c -Wall -O3


main :  Main.o BPGraph.o Permutation.o Random.o InversionModel.o InOut.o
	g++ Main.o BPGraph.o Permutation.o Random.o InversionModel.o InOut.o -o main


Main.o: Main.cc
	g++ $(flag) Main.cc

BPGraph.o: BPGraph.cc BPGraph.h
	g++ $(flag) BPGraph.cc

Permutation.o: Permutation.cc Permutation.h
	g++ $(flag) Permutation.cc

Random.o: Random.cc Random.h
	g++ $(flag) Random.cc

InversionModel.o: InversionModel.cc InversionModel.h
	g++ $(flag) InversionModel.cc

InOut.o: InOut.cc InOut.h
	g++ $(flag) InOut.cc

clean: 
	rm -rf *.o *~ core.* vgcore.*