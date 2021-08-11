from contextlib import suppress
from enum import Enum
from queue import Queue
from typing import Optional


class VerticeNaoEncontradoException(Exception):
    pass


class CaminhoNaoEncontrado(Exception):
    pass


class Status(Enum):
    NAO_VISITADO = 1
    VISITADO_PARCIALMENTE = 2
    VISITA_COMPLETA = 3


class Vertice:
    def __init__(self, id: int):
        self.id = id
        self.adjacentes = []
        self.arestas = []

        self.pai = None
        self.altura = 0
        self.status = Status.NAO_VISITADO

    def add_adj(self, vertice_para, peso):
        self.adjacentes.append(vertice_para)
        self.arestas.append(Aresta(vertice_para, peso))

    def __str__(self):
        return self.id.__str__()

    def __eq__(self, other):
        if isinstance(other, Vertice):
            return other.id == self.id
        return False

    def __hash__(self):
        return hash(self.id)


class Grafo:
    def __init__(self):
        self.vertices = set()

    def add(self, vertice_de: int, vertice_para: int, peso: int = None):
        vertice_de = Vertice(vertice_de)
        with suppress(VerticeNaoEncontradoException):
            vertice_de = self.encontar_vertice(vertice_de.id)

        vertice_para = Vertice(vertice_para)
        with suppress(VerticeNaoEncontradoException):
            vertice_para = self.encontar_vertice(vertice_para.id)

        vertice_de.add_adj(vertice_para, peso)

        self.vertices.add(vertice_de)
        self.vertices.add(vertice_para)

        return self

    def mostrar_caminho(self, iniciar_em: int, ate: int):
        de = self.encontar_vertice(iniciar_em)
        para = self.encontar_vertice(ate)

        self.busca_em_largura(de)

        caminho = []
        atual = para
        while atual is not None:
            caminho.insert(0, atual)
            atual = atual.pai

        sem_caminho_possivel = para.pai is None
        if sem_caminho_possivel:
            print(f"Não foi possível achar um caminho de {de} para {para}")
        else:
            caminho = map(str, caminho)
            print(f'Caminho do {de} para {para} =', ' -> '.join(caminho))

    def busca_em_largura(self, vertice: Vertice):
        vertice.status = Status.VISITADO_PARCIALMENTE

        fila = Queue()
        fila.put(vertice)

        while not fila.empty():
            vertice = fila.get()

            for adjacente in vertice.adjacentes:
                if adjacente.status == Status.NAO_VISITADO:
                    adjacente.status = Status.VISITADO_PARCIALMENTE
                    adjacente.altura = vertice.altura + 1
                    adjacente.pai = vertice
                    fila.put(adjacente)

            vertice.status = Status.VISITA_COMPLETA

    def encontar_vertice(self, id: int) -> Vertice:
        for vertice in self.vertices:
            if vertice.id == id:
                return vertice

        raise VerticeNaoEncontradoException(f"Vertice de id {id} não existe.")

    def __str__(self):
        ligacoes = []

        for vertice in self.vertices:
            ligacoes.append(
                str(vertice) + '->' + str(list(map(str, vertice.adjacentes)))
            )
        return '\n'.join(ligacoes)


class Aresta:
    def __init__(self, vertice_para: Vertice, peso: Optional[int]):
        self.para = vertice_para
        self.peso = peso


def main():
    com_peso = load_com_peso()
    sem_peso = load_sem_peso()

    com_peso.mostrar_caminho(iniciar_em=0, ate=1)
    sem_peso.mostrar_caminho(iniciar_em=3, ate=2)


def load_sem_peso() -> Grafo:
    return Grafo() \
        .add(0, 2) \
        .add(0, 3) \
        .add(1, 3) \
        .add(2, 4) \
        .add(4, 1)


def load_com_peso() -> Grafo:
    return Grafo() \
        .add(0, 2, 11) \
        .add(0, 3, 3) \
        .add(1, 3, 42) \
        .add(2, 4, 7) \
        .add(4, 1, 3)


if __name__ == '__main__':
    main()
