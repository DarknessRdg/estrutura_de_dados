#include <iostream>
using namespace std;



void insertion_sort(int v[], int tam) {
	int eleito;
	for (int i = 1; i < tam; i ++) {
		eleito = v[i];
		
		int j;
		for (j = i - 1; j >= 0 && v[j] > eleito; j--)
			v[j + 1] = v[j];
		
		v[j + 1] = eleito;
	}
}

void insertion_sort_rec(int v[], int tam) {
	if (tam <= 1)
		return;
	
	insertion_sort_rec(v, tam - 1);
	int x = v[tam - 1];
	
	int i;
	for (i = tam - 2; i >= 0 && v[i] > x; i--)
		v[i + 1] = v[i];
	
	v[i + 1] = x;
}





int main() {
	int v[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
	int tam = 9;
	
	insertion_sort_rec(v, tam);
	
	for (int i = 0; i < tam; i ++)
		cout << v[i] << " ";
	cout << endl;
	
	
	return 0;
}