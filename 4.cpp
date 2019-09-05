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
#include <sstream>
using namespace std;

boolean polindrom(int chisl){
    stringstream ss;
    ss << chisl;
	string chi_s = ss.str();
	string per;
	for(int i = chi_s.size()-1; i != -1; i--){
		per.push_back(chi_s[i]);
	}
	if (per == chi_s){
		return true;
	}
	return false;
	
}


void main(){
	int max = 0;
	for(int i = 1; i != 1000; i++){
		for(int j = i; j != 1000; j++){
			if(polindrom(i*j)){
				if(max < i*j){
					max = i*j;
				}
			}
		}
	}
	cout << max;
	Sleep(10000000);
}

