# A implementação original utiliza uma estrutura de dados `heap`
# como fila de prioridade, mas optei por apenas utilizar uma ordenação
# comum da lista para fins didáticos e por ser mais claro e simples para todos
from typing import Callable, Any

INFINITO = float('infinity')


class Vertice(object):
    def __init__(self, representacao):
        self.rep = representacao
        self.pai = None
        self.peso = INFINITO
        self.arestas = []

    def __eq__(self, other):
        return isinstance(other, Vertice) and other.rep == self.rep

    def __str__(self):
        return str(self.rep)

    def __repr__(self):
        return str(self)


class Aresta(object):
    def __init__(self, de, para, peso):
        self.de = de
        self.para = para
        self.peso = peso

    def __str__(self):
        return f'{self.de} --- {self.peso} --> {self.para}'

    def __repr__(self):
        return str(self)


class FilaHeap(object):
    """
    A fila heap aqui foi implementada utilizando ordenação comum para ser
    mais simples, mas é apenas para fins didáticos como mencionado.
    """
    def __init__(self, key: Callable[[Vertice], Any]):
        self.items = []
        self.key = key

    def push(self, obj):
        self.items.append(obj)

    def pop(self):
        self.items.sort(key=self.key, reverse=True)
        # ordena os elementos do maior para o menor
        # e por fim retorna o último elemento da lista
        # simulando uma fila de prioridades, ou fila heap
        return self.items.pop()

    def is_empty(self) -> bool:
        return not bool(self.items)

    def contains(self, item):
        return item in self.items


class Grafo(object):
    def __init__(self):
        self.vertices = []

    def prim(self):
        for vertice in self.vertices:
            vertice.pai = None
            vertice.peso = INFINITO

        self.vertices[0].peso = 0

        fila = FilaHeap(key=ordenar_pelo_peso_do_vertice)
        for vertice in self.vertices:
            fila.push(vertice)

        while not fila.is_empty():
            atual = fila.pop()

            for aresta in atual.arestas:
                adjacente = aresta.para

                if not fila.contains(adjacente):
                    continue

                if aresta.peso < adjacente.peso:
                    adjacente.peso = aresta.peso
                    adjacente.pai = atual

    def add(self, de, para, peso):
        de = self.get_vertice(de)
        para = self.get_vertice(para)

        # prim so funciona com grafos não dirigidos, portanto ambos os
        # vertices podem ir e voltar para ambos
        # a -> b , assim como, a <- b
        de.arestas.append(Aresta(de, para, peso))
        para.arestas.append(Aresta(para, de, peso))
        return self

    def get_vertice(self, representacao) -> Vertice:
        vertice = Vertice(representacao)
        if vertice in self.vertices:
            index = self.vertices.index(vertice)
            return self.vertices[index]

        self.vertices.append(vertice)
        return vertice


def ordenar_pelo_peso_do_vertice(vertice: Vertice):
    return vertice.peso


if __name__ == '__main__':
    g = Grafo()
    g\
        .add('a', 'b', 3).add('a', 'c', 5).add('a', 'd', 8).add('a', 'e', 9)\
        .add('b', 'd', 2)\
        .add('d', 'e', 1).add('d', 'c', 8)\
        .add('e', 'c', 2)

    g.prim()

    for i in g.vertices:
        print(i, i.pai)
