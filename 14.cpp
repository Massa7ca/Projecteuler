#include <iostream>
#include <windows.h>
#include <complex>
#include <iostream>
#include <string>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <string>
using namespace std;

int pos(int chisl){
	__int64 chislo;
	chislo = chisl;
	int kol = 0;
	while (chislo != 1){
		if (chislo % 2 == 0){
			chislo /= 2;
			kol ++;
		}
		else{
			chislo = 3*chislo+1;
			kol ++;
		}
	}
	return kol;
}


void main(){
	int ot, max = 0, chis; 
	for(int i = 1; i != 1000000; i ++){
		ot = pos(i);
		if (ot > max){
			max = ot;
			chis = i;
		}
	}
	cout << chis;
	Sleep(10000000);
}

