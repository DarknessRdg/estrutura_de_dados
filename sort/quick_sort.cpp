#include <iostream>
using namespace std;


/**
 * int v[p..r]
 * int p: inicio
 * int r: fim
 *
 * return posicao do pivo
 */
int separa(int v[], int p, int r) {
	int pivo = v[p];
    int i = p + 1; int j = r;
    while (i <= j) {
        if (v[i] <= pivo)
            i ++;
        else {
            if (pivo < v[j])
                j --;
            else {
                int aux = v[i];
                v[i] = v[j];
                v[j] = aux;
            }
        }
    }

    int aux = v[p];
    v[p] = v[j];
    v[j] = aux;
    cout << "j = " << p << endl;
    return j;
}


void quick_sort_rustico(int v[], int ini, int fim) {
    if (ini < fim) {
        int j = separa(v, ini, fim);
        quick_sort_rustico(v, ini, j-1);
        quick_sort_rustico(v, j+1, fim);
    }
}


void quick_sort_com_uma_recursao(int v[], int ini, int fim) {
    while (ini < fim) {
        int j = separa(v, ini, fim);
        quick_sort_com_uma_recursao(v, ini, j-1);
        ini = j + 1;
    }
}


void quick_sort_melhor_versao(int v[], int ini, int fim) {
    while (ini < fim) {
        int j = separa(v, ini, fim);
        if (j - ini < fim - j) {  // lado esquerdo menor
            quick_sort_melhor_versao(v, ini, j-1);
            ini = j + 1;
        }
        else {
            quick_sort_melhor_versao(v, j+1, fim);
            fim = j - 1;
        }
    }
}

int main() {
	int v[] = {5, 3, 2, 1, 12, 7, 8};
	int tam = 6;

    int esperado_j = 3;

    for (int i = 0; i < tam; i ++)
		cout << v[i] << " ";
	cout << endl;

    quick_sort_melhor_versao(v, 0, tam);
	
	for (int i = 0; i < tam; i ++)
		cout << v[i] << " ";
	cout << endl;
	
	
	return 0;
}