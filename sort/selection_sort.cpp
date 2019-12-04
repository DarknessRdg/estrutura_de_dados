/**
 * Selection sort: sort onde procura o menor e
 * coloca ele na primeira posicao, e assim sucessivamente
 */

/**
 * Selection sort iterativo
 * 
 * @param: int v[], vetor de inteiros
 * @param: int tam, tamanho do vetor
 * 
 */
void selection_sort(int v[], int tam) {
	int aux, menor;
	for (int i = 0; i < tam - 1; i++) {
		
		menor = i;
		for (int j = i; j < tam; j++) {
			if (v[j] < v[menor]) {
				menor = j;
			}
		}
		
		aux = v[i];
		v[i] = v[menor];
	 	v[menor] = aux;
	}
}



/**
 * Selection sort recursivo
 * 
 * @param: int v[], vetor de inteiros
 * @param: int tam, tamanho do vetor
 * 
 */
void selection_sort_recursivo(int v[], int tam) {
	if (tam == -1) 
		return;
	
	int menor = 0;
	for (int i = 0; i < tam; i++) {
		if (v[i] < v[menor])
			menor = i;
	}
	
	int aux = v[0];
	v[0] = v[menor];
	v[menor] = aux;
	
	selection_sort(&v[1], tam - 1);
}