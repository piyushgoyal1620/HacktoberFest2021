#include <iostream>
using namespace std;

int min(int a[],int n,int k){

	int min=a[k],loc=k;
	for(int i=k+1;i<n;i++){
		if(min>a[i]){
			min=a[i];
			loc=i;
		}
	}
	return loc;
}

int main() {
	int a[] = { 33,3,6,1,67,89,34,56,30,91,76,43,134,99 };

	for (int k=0;k<=12;k++){
		int loc=min(a,14,k);
		int t;
		t=a[k];
		a[k]=a[loc];
		a[loc]=t;
	}


	for (int i = 0; i < 14; i++) {
		cout << a[i] << endl;
	}
	return 0;
}
