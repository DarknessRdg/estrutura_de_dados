from contextlib import suppress
from enum import Enum
from typing import Optional


class VerticeNaoEncontradoException(Exception):
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
        self.tempo_inicial = 0
        self.tempo_final = 0
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
        self._tempo = 0

    def add(self, vertice_de: int, vertice_para: int, peso: int):
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

    def encontar_vertice(self, id: int) -> Vertice:
        for vertice in self.vertices:
            if vertice.id == id:
                return vertice

        raise VerticeNaoEncontradoException(f"Vertice de id {id} não existe.")

    def busca_em_profundidade(self):
        self._tempo = 0
        for vert in self.vertices:
            vert.status = Status.NAO_VISITADO
            vert.pai = None

        v = list(self.vertices)
        v.remove(self.encontar_vertice(1))
        v.insert(0, self.encontar_vertice(1))

        for vert in v:
            if vert.status == Status.NAO_VISITADO:
                self.visit(vert)

    def visit(self, vertice: Vertice):
        self._tempo += 1

        vertice.tempo_inicial = self._tempo
        vertice.status = Status.VISITADO_PARCIALMENTE

        for adj in vertice.adjacentes:
            if adj.status == Status.NAO_VISITADO:
                adj.pai = vertice
                self.visit(adj)

        vertice.status = Status.VISITA_COMPLETA
        self._tempo += 1
        vertice.tempo_final = self._tempo

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
    g = Grafo()
    g\
        .add(0, 2, 1) \
        .add(0, 3, 2) \
        .add(1, 3, 3) \
        .add(2, 4, 4) \
        .add(4, 1, 5)

    g.busca_em_profundidade()


if __name__ == '__main__':
    main()
