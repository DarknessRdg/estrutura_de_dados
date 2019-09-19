/**
 * Lista com cabeçeca
 * NULL -> 1 -> 2 -> 3 -> 4 -> NULL
 * 
 * O primeiro NULL da lista serve somente para guarda a referencia
 * do inicio da lista, e nao contem nenhum conteudo no seu interior
 * 
 */
#include <stdio.h>
#include <stdlib.h>


struct cell{
	int valor;
	struct cell* prox;
};
typedef struct cell Cell;


/**
 * Funcao que cria uma nova Celula, e retorna seu ponteiro
 */
Cell* criaCelula(int i) {
	Cell* nova = (Cell*) malloc(sizeof(Cell));
	nova->valor = i;
	nova->prox = NULL;
	
	return nova;
}


/**
 * Funcao que cria a cabeca de uma lista;
 */
Cell* criaListaComCabeca() {
	Cell* nova = (Cell*) malloc(sizeof(Cell));
	nova->prox = NULL;
	
	return nova;
}


/**
 * Funcao que receber a cabeca da lista e adicona uma nova celular ao final
 */
void addValor(Cell* listaComCabeca, int valor) {
	Cell* aux = listaComCabeca;
	while(aux->prox) 
		aux = aux->prox;
	
	aux->prox = criaCelula(valor);
}


Cell* buscar(Cell* listaComCabeca, int valor) {
	Cell* aux = listaComCabeca->prox;
	
	while (aux->valor != valor && aux)
		aux = aux->prox;
	
	return aux;
	
}


void imprime(Cell* listaComCabeca) {
	Cell* aux = listaComCabeca->prox;
	
	while (aux) {
		printf("%d, ", aux->valor);
		aux = aux->prox;
	}
	printf("\n");
}


void insereNaFrente(Cell* posicao, int valor) {
	Cell* proximo = proximo = posicao->prox;
	Cell* nova = criaCelula(valor);
	
	posicao->prox = nova;
	nova->prox = proximo;
}


void removeCelulaSeguinte(Cell* posicao) {
	Cell* lixo = posicao->prox;
	posicao->prox = lixo->prox;
	
	free(lixo);
}



int main() {
	Cell* cabeca = criaListaComCabeca();
	addValor(cabeca, 1);
	addValor(cabeca, 2);
	addValor(cabeca, 3);
	
	Cell* c = cabeca->prox;  // primeira posicao
	
	insereNaFrente(c, 10);
	imprime(cabeca);
	
	removeCelulaSeguinte(c);
	imprime(cabeca);
	return 0;
}