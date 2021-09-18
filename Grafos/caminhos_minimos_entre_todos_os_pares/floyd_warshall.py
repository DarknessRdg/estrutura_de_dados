from copy import deepcopy

INFINITO = float('infinity')


class Vertice(object):
    def __init__(self, representacao):
        self.rep = representacao
        self.arestas = set()

    def __hash__(self):
        return hash(self.rep)

    def __str__(self):
        return str(self.rep)

    def __eq__(self, other):
        return self.rep == other

    def __repr__(self):
        return str(self)


class Aresta:
    def __init__(self, to: Vertice, peso):
        self.to = to
        self.peso = peso

    def __hash__(self):
        return hash(self.to) + hash(self.peso)

    def __str__(self):
        return f'(to={self.to}, peso={self.peso})'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return isinstance(other, Aresta) and other.to == self.to


class Grafo:
    def __init__(self):
        self.vertices = []

    def add(self, _from, to, peso):
        _from = self.get_vertice(_from)
        to = self.get_vertice(to)

        _from.arestas.add(Aresta(to=to, peso=peso))
        return self

    def get_vertice(self, representacao) -> Vertice:
        vertice = Vertice(representacao)
        if vertice in self.vertices:
            index = self.vertices.index(vertice)
            return self.vertices[index]

        self.vertices.append(vertice)
        return vertice


class FloydWarshall:
    def __init__(self, grafo: Grafo):
        self.vertices = sorted(grafo.vertices, key=lambda it: it.rep)
        self.quantidade_de_vertices = len(self.vertices)
        self.matriz = []

    def _initi_matriz(self):
        self.matriz = [
            [INFINITO for _ in range(self.quantidade_de_vertices)]
            for _ in range(self.quantidade_de_vertices)
        ]

        for vertice in self.vertices:
            indice_vertice = self.vertices.index(vertice)

            for aresta in vertice.arestas:
                indice_aresta = self.vertices.index(aresta.to)

                self.matriz[indice_vertice][indice_aresta] = aresta.peso

    def run(self):
        self._initi_matriz()
        for coluna in range(self.quantidade_de_vertices):
            self.relaxa(coluna)

    def relaxa(self, coluna):
        for j in range(self.quantidade_de_vertices):
            valor_da_coluna = self.matriz[j][coluna]

            for i in range(self.quantidade_de_vertices):
                valor_da_linha = self.matriz[coluna][i]

                if not self._da_para_somar(valor_da_coluna, valor_da_linha):
                    continue
                if not self._pode_alterar(j, i):
                    continue

                custo = valor_da_coluna + valor_da_linha
                if custo < self.matriz[j][i]:
                    self.matriz[j][i] = custo

    def _da_para_somar(self, a, b):
        if INFINITO == a or INFINITO == b:
            return False
        return True

    def _pode_alterar(self, i, j):
        diagonal_principal = i == j
        return not diagonal_principal

    def get_matriz_com_repr(self):
        matriz = deepcopy(self.matriz)

        for i, linha in enumerate(matriz):
            linha.insert(0, self.vertices[i].rep)
        matriz.insert(0, self.vertices)
        matriz[0].insert(0, ' ')
        return matriz


if __name__ == '__main__':
    grafo = Grafo()
    grafo.add('A', 'B', 3).add('A', 'C', 4) \
        .add('B', 'D', 5) \
        .add('D', 'A', 8) \
        .add('C', 'D', 3)

    floyd = FloydWarshall(grafo)
    floyd.run()

    for i in floyd.get_matriz_com_repr():
        print(i)

