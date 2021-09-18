INFINITO = float('infinity')


class Vertice(object):
    def __init__(self, representacao):
        self.rep = representacao
        self.pai = None
        self.peso = INFINITO
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

        # prim so funciona com grafos não dirigidos, portanto ambos os
        # vertices podem ir e voltar para ambos
        # a -> b , assim como, a <- b
        _from.arestas.add(Aresta(to=to, peso=peso))
        return self

    def get_vertice(self, representacao) -> Vertice:
        vertice = Vertice(representacao)
        if vertice in self.vertices:
            index = self.vertices.index(vertice)
            return self.vertices[index]

        self.vertices.append(vertice)
        return vertice


class Dijsktra:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.queue = FilaHeap(key=lambda it: it.peso)

    def clean_vertices(self, source: Vertice):
        for vertice in self.grafo.vertices:
            vertice.pai = None
            vertice.peso = INFINITO
            self.queue.push(vertice)
        source.peso = 0

    def run(self, source, to):
        source = self.grafo.get_vertice(source)
        to = self.grafo.get_vertice(to)

        self.clean_vertices(source)
        while not self.queue.is_empty():
            vertice = self.queue.pop()
            self.relaxa_arestas(vertice)

        return self.build_path(to)

    def build_path(self, end: Vertice):
        path = [end]

        current = end
        while current.pai is not None:
            path.append(current.pai)
            current = current.pai
        return path[::-1]

    def relaxa_arestas(self, vertice: Vertice):
        for aresta in vertice.arestas:
            custo = vertice.peso + aresta.peso

            if custo < aresta.to.peso:
                aresta.to.peso = custo
                aresta.to.pai = vertice


class FilaHeap(object):
    """
    A fila heap aqui foi implementada utilizando ordenação comum para ser
    mais simples, mas é apenas para fins didáticos como mencionado.
    """
    def __init__(self, key):
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


if __name__ == '__main__':
    grafo = Grafo()
    grafo.add('A', 'D', 2).add('A', 'B', 4).add('B', 'D', 3).add('D', 'B', 1) \
        .add('B', 'C', 2).add('B', 'E', 3).add('D', 'C', 4).add('D', 'E', 5) \
        .add('E', 'C', -5)

    path = Dijsktra(grafo).run('A', 'E')
    print(path)
