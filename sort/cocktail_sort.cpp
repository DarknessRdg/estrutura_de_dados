
void troca(int* a, int* b) {
	int aux = *a;
	*a = *b;
	*b = aux;
}


void cocktail_sort(int v[], int tam) {
	int esq = 0; int dir = tam - 1;
	
	while (esq < dir) {
		
		/**
		 * Da esquerda para a direita, portanto o 
		 * maior vai ficar na posicao final
		 */
		for (int i = esq; i < dir; i++) {
			if (v[i] > v[i + 1])
				troca(&v[i], &v[i + 1]);
		}
		
		dir --;  // decrementa a direita, ja que o maior esta no final
		
		/**
		 * Da direita para a esquerda, portanto o
		 * menor vai para o inicio
		 */
		for (int i = dir; i > esq; i--) {
			if (v[i] < v[i - 1])
				troca(&v[i], &v[i - 1]);
		}
		esq ++;  // decrementa a esquerda ja que o menor esta na posicao inicial
	}
	
}