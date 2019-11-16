"""
Pacote com classes e funcoes que serao uteis durante o jogo
"""

import random


class Ponto:
    """
    Classe que representa as coordenadas de um ponto
    no plano cartesiano
    """

    def __init__(self, x, y):
        """Contrutor da classe"""
        self.set_coordenadas(x, y)
    
    def __str__(self):
        """Metodo chamado atraves da funcao print() do python"""
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        """
        Metodo chamado quando um objeto Ponto() é comparado a outro
        usando operador de igualdade. ex: Ponto() == Ponto()

        Args:
            other: outro objeto da classe Ponto
        Returns:
            boolean: Ponto() é igual ao outro Ponto() ?
        """
        return self.x == other.x and self.y == other.y

    def coordenadas(self):
        """Metodo para retornas as coordenadas do no"""
        return self.x, self.y

    def set_coordenadas(self, x, y):
        """
        Metodo para atualizar os valores de x, y
        Args:
            x: numero - coodenada X
            y: numero - coordenada Y
        """
        self.x, self.y = x, y


class CelulaDaCobra(Ponto):
    """
    Classe que representa uma celula presente no corpo
    da cobra
    """

    def __init__(self, x, y, cor):
        """Contrutor da classe"""
        super(CelulaDaCobra, self).__init__(x, y)
        self.cor = cor
        self.prox = None


def posicao_aleatoria(resolucao, grid):
    """
    Funcao para pegar uma posicao aleatoria da tela
    Args:
        resolucao: objeto da classe Ponto com a resolocao da tela,
        grid: int com o tamanho do grid do jogo

    Return:
        objeto da classe Ponto() com coordenadas aleatorias
   """
    x = random.randint(0, resolucao.x - 1)
    y = random.randint(0, resolucao.y - 1)

    return Ponto(x // grid * grid,
                 y // grid * grid)


def elemento_aleatorio(elementos):
    """
    Funcao que retorna um elmento aleatorio de um iterable
    Args:
        elementos: iterrable
    Returns:
         elemento de uma posicao aleatoria do iterable
    """
    index = random.randint(0, len(elementos) - 1)
    return elementos[index]
