INFINITO = float('infinity')


def max_by(extract, iterable):
    tmp_max = None
    for item in iterable:
        if tmp_max is None:
            tmp_max = item
            continue

        if extract(item) > extract(tmp_max):
            tmp_max = item
    return tmp_max


class Vertice(object):
    def __init__(self, representacao):
        self.rep = representacao
        self.arestas = set()
        self._existe_aresta_valida = True
        self.esta_valido = True
        self.visitado = False

    @property
    def existe_aresta_valida(self):
        if self._existe_aresta_valida:
            self._existe_aresta_valida = any(
                [it.esta_valida for it in self.arestas]
            )
            if not self._existe_aresta_valida:
                self.esta_valido = False
        return self._existe_aresta_valida

    def can_go_to(self, target):
        return target in map(lambda it: it.to, self.arestas)

    def find_arest_to(self, target):
        for aresta in self.arestas:
            if aresta.to == target:
                return aresta

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
        self.visitada = False

    @property
    def esta_valida(self):
        valido = self.peso > 0 and self.to.esta_valido
        return valido

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


class Rotulacao:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo

    def run(self, source, target):
        source = self.grafo.get_vertice(source)
        target = self.grafo.get_vertice(target)

        total = []
        while source.existe_aresta_valida:
            max_found = self.find_max_path(source, target)
            total.append(max_found)
        return sum(total)

    def find_max_path(
            self,
            current: Vertice,
            target: Vertice,
            max_peso_do_caminho=None
    ):
        if not current.existe_aresta_valida:
            current.esta_valido = False
            return 0

        maior_aresta = max_by(self._filter_aresta, current.arestas)
        if maior_aresta.to.visitado:
            return max_peso_do_caminho

        maior_aresta.visitada = True
        if maior_aresta.to == target:  # chegou no final
            aresta_final = maior_aresta

            if max_peso_do_caminho is None:
                max_peso_do_caminho = aresta_final.peso

            if aresta_final.peso >= max_peso_do_caminho:
                aresta_final.peso -= max_peso_do_caminho
            else:
                max_peso_do_caminho = aresta_final.peso
                aresta_final.peso = 0
            return max_peso_do_caminho

        # ainda está procurando o caminho
        if max_peso_do_caminho is None \
                or max_peso_do_caminho > maior_aresta.peso:
            max_peso_do_caminho = maior_aresta.peso

        current.visitado = True
        max_found = self.find_max_path(
            current=maior_aresta.to,
            target=target,
            max_peso_do_caminho=max_peso_do_caminho
        )
        current.visitado = False
        maior_aresta.peso -= max_found
        return max_found

    def _filter_aresta(self, aresta):
        if aresta.to.visitado or not aresta.to.esta_valido:
            return -INFINITO
        return aresta.peso


if __name__ == '__main__':
    assert Rotulacao(
        Grafo() \
            .add('s', 'v1', 16).add('s', 'v2', 13) \
            .add('v2', 'v1', 4).add('v2', 'v4', 14) \
            .add('v1', 'v3', 12) \
            .add('v3', 'v2', 9).add('v3', 't', 20) \
            .add('v4', 'v3', 7).add('v4', 't', 4)
    ).run('s', 't') == 23

    assert Rotulacao(
        Grafo().add('s', 'v1', 16) \
            .add('s', 'v2', 13) \
            .add('v2', 't', 30)
    ).run('s', 't') == 13

    assert Rotulacao(
        Grafo().add('s', 'v1', 16) \
            .add('s', 'v2', 13)
    ).run('s', 'v1') == 16

    assert Rotulacao(
        Grafo().add('s', 'v1', 16).add('v1', 't', 3) \
            .add('s', 'v2', 13).add('v2', 't', 4)
    ).run('s', 't') == 7

    assert Rotulacao(
        Grafo().add('s', 'v1', 16)\
            .add('s', 'v2', 13)\
            .add('v2', 'v1', 5)
    ).run('s', 'v1') == 21

    assert Rotulacao(
        Grafo().add('s', 'v1', 16)\
            .add('s', 'v2', 13)\
            .add('v2', 'v1', 5)\
            .add('v1', 'v3', 10)
    ).run('s', 'v1') == 21
