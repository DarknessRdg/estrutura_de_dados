"""
Arquivo para a implementação de uma fila
"""

import sys


class No:
    """
    Nó que representa cada celula da fila,
    onde cada nó possui como atributo suas
    coodenadas (x, y) e uma cor
    """

    def __init__(self, x, y, cor):
        """Contrutor da classe"""
        self.x, self.y = x, y
        self.cor = cor
        self.prox = None
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def coodenadas(self):
        """Metodo para retornas as coordenadas do no"""
        return self.x, self.y


class Fila:
    def __init__(self):
        """Contrutor da fila"""
        self._len = 0
        self._inicio = None
        self._ultimo = None
    
    def __len__(self):
        """
        Metodo chamado atraves da funcao len() do python
        """
        return self._len
    
    def __str__(self):
        """Metodo chamado atraves da funcao print() do python"""
        aux = self._inicio
        
        string = ''
        while aux is not None:
            string += aux.__str__()

            if aux.prox is not None:
                string += ', '
            aux = aux.prox
        return '[' + string + ']'
    
    def esta_vazia(self):
        """
        Meotodo que rotorna booleano indicando se a fila esta
        vazia
        """
        return len(self) == 0

    def insere(self, **kwargs):
        """
        Metodo para adicionar um elemento na lista
        argr:
            **kwargs, opcoes: x, y, cor
        """
        novo_no = No(**kwargs)

        if self.esta_vazia():
            self._inicio = novo_no
            self._ultimo = novo_no
        else:
            self._ultimo.prox = novo_no
            self._ultimo = novo_no


        self._len += 1
    
    def remove(self):
        """Metodo para remover primero elemto da fila"""
        primeiro = self._inicio
        if not self.esta_vazia():    
            self.primeiro = self.primeiro.prox
            self._len -= 1
        
        return primeiro


if __name__ == '__main__':
    pass