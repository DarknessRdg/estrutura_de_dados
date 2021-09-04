from typing import Optional


class CelulaDeMemoria:
    def __init__(self, _id):
        self._id = _id
        self.vazia = True

    def __str__(self):
        return self._id

    def __repr__(self):
        return f'CelulaDeMemoria(id={self._id}, vazia={self.vazia})'


TAMANHO_DA_MEMORIA = 100

MEMORIA = [
    CelulaDeMemoria(indice+1)
    for indice in range(TAMANHO_DA_MEMORIA)
]


class Processo:
    def __init__(self, tamanho_de_espaco_necessario):
        self.espaco = tamanho_de_espaco_necessario
        self.celulas_alocadas = []


class AreaLivre:
    def __init__(self, inicio=0, fim=0):
        self.inicio = inicio
        self.fim = fim

    @property
    def tamanho(self):
        return self.fim - self.inicio


def get_worst() -> Optional[AreaLivre]:
    maior_area_livre = AreaLivre(inicio=-1)

    indice = 0

    while indice < TAMANHO_DA_MEMORIA:
        if not MEMORIA[indice].vazia:
            indice += 1
            continue

        area_livre_temp = AreaLivre(inicio=indice)

        while indice < TAMANHO_DA_MEMORIA and MEMORIA[indice].vazia:
            indice += 1

        area_livre_temp.fim = indice

        if area_livre_temp.tamanho > maior_area_livre.tamanho:
            maior_area_livre = area_livre_temp

    if maior_area_livre.inicio == -1:
        return None
    return maior_area_livre


def worst_fit(processo):
    area_livre = get_worst()

    if area_livre.tamanho >= processo.espaco:
        for padding in range(processo.espaco):
            indice = area_livre.inicio + padding

            celula = MEMORIA[indice]

            celula.vazia = False
            processo.celulas_alocadas.append(celula)
        print(processo.celulas_alocadas)
    else:
        print('Não há espaço suficiente')


if __name__ == '__main__':
    MEMORIA[0].vazia = False
    MEMORIA[1].vazia = False
    MEMORIA[2].vazia = False
    MEMORIA[3].vazia = False
    MEMORIA[4].vazia = False
    MEMORIA[5].vazia = False

    for i in range(10, 95):
        MEMORIA[i].vazia = False

    worst_fit(Processo(5))
