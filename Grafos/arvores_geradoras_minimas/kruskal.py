from typing import Set


class Vertice(object):
    def __init__(self, representacao):
        self.rep = representacao

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.rep)

    def __eq__(self, other):
        return isinstance(other, Vertice) and other.rep == self.rep

    def __hash__(self):
        return hash(self.rep)


class Aresta(object):
    def __init__(self, de, para, peso):
        self.de = de
        self.para = para
        self.peso = peso

    def __str__(self):
        return f'{self.de} <---- {self.peso} ----> {self.para}'

    def __repr__(self):
        return str(self)


class Grafo(object):
    def __init__(self):
        self.vertices = []
        self.arestas = []
        self.conjuntos = []

    def kruskal(self):
        arestas_utilizads = []

        self.criar_conjuntos()
        self.ordenar_as_arestas_por_peso()

        for aresta in self.arestas:
            conjunto_vertice_de = self.encontrar_conjunto_do_vertice(aresta.de)
            conjunto_vertice_para = self.encontrar_conjunto_do_vertice(
                aresta.para)

            if conjunto_vertice_de != conjunto_vertice_para:
                self.unir_conjuntos(conjunto_vertice_de, conjunto_vertice_para)
                # manter o registro das arestas utilzada em cada vertice
                arestas_utilizads.append(aresta)

        return arestas_utilizads

    def unir_conjuntos(self, a: Set[Vertice], b: Set[Vertice]):
        self.conjuntos.remove(a)
        self.conjuntos.remove(b)
        self.conjuntos.append(b.union(a))

    def ordenar_as_arestas_por_peso(self):
        self.arestas.sort(key=lambda aresta: aresta.peso)

    def criar_conjuntos(self):
        self.conjuntos = [
            {vertice} for vertice in self.vertices
        ]

    def encontrar_conjunto_do_vertice(self, vertice):
        for conjunto in self.conjuntos:
            if vertice in conjunto:
                return conjunto

    def add(self, de, para, peso):
        de = self.get_vertice(de)
        para = self.get_vertice(para)

        # kruskal so funciona com grafos não dirigidos, portanto ambos os
        # vertices podem ir e voltar para ambos
        # a -> b , assim como, a <- b
        # portanto, embora a estrutura de dados tenha `de` `para` , é importante
        # manter em mente que é uma aresta bilateral
        self.arestas.append(Aresta(de, para, peso))
        return self

    def get_vertice(self, representacao):
        vertice = Vertice(representacao)
        if vertice in self.vertices:
            index = self.vertices.index(vertice)
            return self.vertices[index]

        self.vertices.append(vertice)
        return vertice


if __name__ == '__main__':
    g = Grafo() \
        .add('a', 'b', 3).add('a', 'c', 5).add('a', 'd', 8).add('a', 'e', 9) \
        .add('b', 'd', 2) \
        .add('d', 'e', 1).add('d', 'c', 8) \
        .add('e', 'c', 2)

    for aressta in g.kruskal():
        print(aressta)
