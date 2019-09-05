#include <iostream>
#include <windows.h>
#include <complex>
#include <iostream>
#include <string>
int rtiugo(int p){
	int sk = 0;
	int i,j,m;
	for (i = 2; i < p/2; i++){
		for (j = i; j < p/2; j++){
			int m = p - (i+j);
			if (p == (i + j + m)){
				if ((i*i) + (j*j) == (m*m)){
					sk ++; 
				}	
			}
			
		}
	}
	return (sk);
}
main ()
{
	int max = 0;
	int mm = 1;
	while (mm < 10000){
		int a = rtiugo(mm);
		if (max < a){
			max = a;
			printf("%d\t %d\n", max/2, mm);
		}
		mm ++;
	}
}