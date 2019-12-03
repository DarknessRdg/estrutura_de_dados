/**
 * Metodo de ordenaçao bolha
 */



/**
 *  Ordenacao iterativa
 *  @param int v[]: vetor de inteiros
 *  @param int tam: tamanho do vetor
 */
void bubble_sort(int v[], int tam) {
	int aux; bool houve_troca = true;
	
	for (int j = 0; j < tam - 1 && houve_troca; j++) {
		houve_troca = false;
		
		for(int i = 0; i < tam - 1 - j; i++) {
			if (v[i] > v[i + 1]) {
				aux = v[i];
				v[i] = v[i + 1];
				v[i + 1] = aux;
				houve_troca = true;
			}
		}
	}
}


/**
 *  Ordenacao recursiva
 *  @param int v[]: vetor de inteiros
 *  @param int tam: tamanho do vetor
 */
void bubble_sort_rercursivo(int v[], int tam) {
	if (tam < 1)
		return;
	
	int aux;
	for(int i = 0; i < tam - 1; i++) {
		if (v[i] > v[i + 1]) {
			aux = v[i];
			v[i] = v[i + 1];
			v[i + 1] = aux;
		}
		
		bubble_sort_rercursivo(v, tam - 1);
	}
}
