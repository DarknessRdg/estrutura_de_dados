"""
Algoritmo para inverter uma lista ligada.
Author: Luan Rodrigues


Ele funciona da seguinte forma:
Dada uma lista ligada: cebeca -> 1 -> 2 -> 3 -> 4 -> null

O último (4) elemento passa ser o primeiro da lista, e ele apontará
para o antigo primeiro (1)

cabeca -> 4 -> 1 -> null

Após isso o algoritmo funciona como uma inserção dos outros
elementos. Eles serão inseridos como o próximo do último (4).

Portanto,

será inserido o 2:
cabeca -> 4 -> 2 -> 1 -> null

será inserido o 3:
cabeca -> 4 -> 3 -> 2 -> 1 -> null

o próximo elemento a ser inserido seria o último (4),
porém ele já está no lugar certo.
"""


class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

    def __str__(self):
        return str(self.valor)


def reverse(cabeca_da_lista):
    if (cabeca_da_lista is None
            or cabeca_da_lista.prox is None  # len == 0
            or cabeca_da_lista.prox.prox is None):  # len == 1
        return

    atual = cabeca_da_lista.prox
    ultimo = atual
    while ultimo.prox is not None:
        ultimo = ultimo.prox

    # altera o ponteiro da cabeca para apontar para o último
    # elemento da lista
    ultimo.prox = atual
    cabeca_da_lista.prox = ultimo
    temp = atual.prox
    atual.prox = None

    # temporario será o "atual", onde esse temporário
    # ele será o elemento a ser inserido após o último (que comporta-se
    # como primeiro)
    while temp != ultimo:
        ultimo.prox = temp

        temp2 = temp.prox
        temp.prox = atual
        atual = temp
        temp = temp2


def cria_uma_lista_de_tamanho(n) -> No:
    cabeca = No(None)

    x = [No(i+1) for i in range(n)]

    for i in range(len(x) - 1):
        x[i].prox = x[i+1]

    cabeca.prox = x[0]
    return cabeca


def print_da_lista(cabeca: No):
    if cabeca.prox is None:
        return

    at = cabeca.prox
    print('[', end='')
    while at:
        print(at, end=', ')
        at = at.prox
    print(']')


if __name__ == '__main__':
    head = cria_uma_lista_de_tamanho(10)
    print_da_lista(head)
    reverse(head)
    print_da_lista(head)
