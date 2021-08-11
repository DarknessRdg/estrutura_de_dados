from contextlib import suppress
from typing import Optional


class VerticeNaoEncontradoException(Exception):
    pass


class StatusVisita:
    NAO_INICIADA = 1
    PARCIAL = 2
    COMPLETA = 3


class Vertice(object):
    def __init__(self, rep):
        self.rep = rep
        self.visita = StatusVisita.NAO_INICIADA
        self.pai = None
        self.termino = 0
        self.arestas = set()

    @property
    def adjacentes(self):
        return {aresta.para for aresta in self.arestas}

    def add_aresta(self, para, peso):
        self.arestas.add(Aresta(de=self, para=para, peso=peso))

    def remover_aresta(self, aresta):
        self.arestas.remove(aresta)

    def clone(self):
        copia = Vertice(self.rep)
        copia.termino = self.termino
        copia.visita = self.visita
        copia.pai = None if self.pai is None else self.pai.clone()
        return copia

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.rep)

    def __eq__(self, other):
        return isinstance(other, Vertice) \
               and other.rep == self.rep

    def __hash__(self):
        return hash(self.rep)


class Aresta(object):
    def __init__(self, de: Vertice, para: Vertice, peso: Optional[int]):
        self.de = de
        self.para = para
        self.peso = peso

    def __hash__(self):
        return hash(str(self))

    def __repr__(self):
        return str(self)

    def __str__(self):
        seta = '----' if self.peso is None else f'---- {self.peso} ----'
        seta += '>'

        return f'{self.de} {seta} {self.para.rep}'

    def __eq__(self, other):
        return isinstance(other, Aresta) \
               and self.de == other.de \
               and self.para == other.para


class Grafo(object):
    def __init__(self):
        self.vertices = set()
        self._tempo = 0

    def transposta(self):
        grafo_transposto = Grafo()

        for vertice in self.vertices:
            for aresta in vertice.arestas:
                grafo_transposto.add_instancias_de_vertice(
                    de=grafo_transposto.get_clone(aresta.para),
                    para=grafo_transposto.get_clone(vertice),
                    peso=aresta.peso
                )

        return grafo_transposto

    def get_clone(self, vertice: Vertice):
        vertice_clone = vertice.clone()
        if vertice in self.vertices:
            vertice_clone = self.encontar_vertice(vertice.rep)
        return vertice_clone

    def add_instancias_de_vertice(self, de, para, peso):
        de.add_aresta(para, peso)
        self.vertices.add(de)
        self.vertices.add(para)

    def add(self, de, para, peso=None):
        de = Vertice(de)

        with suppress(VerticeNaoEncontradoException):
            de = self.encontar_vertice(de.rep)

        para = Vertice(para)
        with suppress(VerticeNaoEncontradoException):
            para = self.encontar_vertice(para.rep)

        self.add_instancias_de_vertice(de, para, peso)
        return self

    def encontar_vertice(self, rep) -> Vertice:
        for vertice in self.vertices:
            if vertice.rep == rep:
                return vertice

        raise VerticeNaoEncontradoException(f"Vertice de id {rep} não existe.")

    def busca_em_profundidade(self, vertices):
        self._tempo = 0

        for vert in vertices:
            vert.visita = StatusVisita.NAO_INICIADA
            vert.pai = None

        for vert in vertices:
            if vert.visita == StatusVisita.NAO_INICIADA:
                self.visit(vert)

    def visit(self, vertice: Vertice):
        self._tempo += 1
        vertice.visita = StatusVisita.PARCIAL

        for adj in vertice.adjacentes:
            if adj.visita == StatusVisita.NAO_INICIADA:
                adj.pai = vertice
                self.visit(adj)

        vertice.visita = StatusVisita.COMPLETA
        self._tempo += 1
        vertice.termino = self._tempo

    def componentes_fortemente_conectados(self):
        self.busca_em_profundidade(self.vertices)
        transposto = self.transposta()

        vertices_invertidos = sorted(
            transposto.vertices,
            key=lambda it: it.termino,
            reverse=True
        )

        self.busca_em_profundidade(vertices_invertidos)

        for vert in vertices_invertidos:
            vert.visita = StatusVisita.NAO_INICIADA

        componentes = []
        for vert in vertices_invertidos:
            if vert.visita == StatusVisita.NAO_INICIADA:
                c = self.push_componentes(vert, [])
                componentes.append(c)

        return componentes

    def push_componentes(self, vert, components):
        vert.visita = StatusVisita.COMPLETA

        components.append(vert)

        for adj in vert.adjacentes:
            if adj.visita == StatusVisita.NAO_INICIADA:
                self.push_componentes(adj, components)
        return components


if __name__ == '__main__':
    g = Grafo()
    g.add('a', 'b') \
        .add('b', 'e').add('b', 'f')\
        .add('c', 'd')\
        .add('d', 'c')\
        .add('e', 'f').add('e', 'a')\
        .add('f', 'g')\
        .add('g', 'f').add('g', 'h')\
        .add('h', 'h')

    print(g.vertices)
    print(g.componentes_fortemente_conectados())
