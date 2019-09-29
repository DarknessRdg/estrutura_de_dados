#include <stdio.h>
#include <stdlib.h>
#define endl "\n"


struct cell{
	int valor;
	struct cell* prox;
};
typedef struct cell Cell;


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


/**
 * Funcao para mostrar elementos de uma lista COM CABECA
 */
void imprime(Cell* listaComCabeca) {
	Cell* aux = listaComCabeca->prox;
	
	while (aux) {
		printf("%d, ", aux->valor);
		aux = aux->prox;
	}
	printf(endl);
}


/**
 * Funcao para imprimir invetida uma lista SEM CABECA
 */
void printInvertida(Cell* cabeca) {
    if (cabeca->prox)
        printInvertida(cabeca->prox);
    
    printf("%d ", cabeca->valor);
}


/**
 * Funcao para imprimir uma lista invertida COM CABECA
 */
void printInvertidaComCabeca(Cell* cabeca) {
    Cell* proximo = cabeca->prox;

    if (proximo->prox)
        printInvertida(proximo->prox);
    
    printf("%d ", proximo->valor);
}


/**
 * Funcao que remove todos elementos Y de uma lista COM CABECA
 */
Cell* removeTodosY(Cell* cabeca, int valor) {
    Cell* anterior = cabeca;
    Cell* atual = cabeca->prox;

    while (atual) {
        if (atual->valor == valor) {

            Cell* lixo = atual;
            anterior->prox = atual->prox;
            free(lixo);
            
            atual = anterior->prox;
        } 
        else {
            anterior = atual;
            atual = atual->prox;
        }
    }
    return cabeca;
}


int somarDigitos(int num) {
    int resto = num % 10;
    if (resto == 0)
        return num;

    return resto + somarDigitos(num / 10); 
}


int main() {
    Cell* cabeca = criaListaComCabeca();

    /* 6, 2, 3, 4, 5, 6, 6, 6, 4, 6, 1, 6 */
    addValor(cabeca, 6); addValor(cabeca, 2); addValor(cabeca, 3);
    addValor(cabeca, 4); addValor(cabeca, 5); addValor(cabeca, 6); 
    addValor(cabeca, 6); addValor(cabeca, 6); addValor(cabeca, 4);
    addValor(cabeca, 6); addValor(cabeca, 1); addValor(cabeca, 6);
    
    imprime(cabeca);
    printf("Lista ivnertida: ");
    printInvertidaComCabeca(cabeca);
    printf(endl);
    printf(endl);

    printf("Remove todo os 6: ");
    removeTodosY(cabeca, 6);
    imprime(cabeca);
    printf(endl);

    
    printf("Somar digitos de um numero interio - ex 123: %d\n", somarDigitos(123));
    printf(endl);
    return 0;
}