"""
Arquivo para a implementação de uma fila
"""

class Fila:
    def __init__(self, class_no):
        """Contrutor da fila"""
        self._len = 0
        self._inicio = None
        self._ultimo = None

        self._class_no = class_no
    
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

    @property
    def primeiro(self):
        """property para pegar o primeiro elemento da fila"""
        return self._inicio

    @property
    def ultimo(self):
        """property para pegar o ultimo elemento da fila"""
        return self._ultimo

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
            **kwargs, 
                opcoes sao os paramentos do construtor
                da class_no
        """
        novo_no = self._class_no(**kwargs)

        if self.esta_vazia():
            self._inicio = novo_no
        else:
            self._ultimo.prox = novo_no
        self._ultimo = novo_no
        self._len += 1
    
    def remove(self):
        """Metodo para remover primero elemto da fila"""
        primeiro = self._inicio
        if not self.esta_vazia():    
            self._inicio = primeiro.prox
            self._len -= 1
        
        return primeiro

    def esta_presente(self, celula):
        """
        Metodo que retorna se uma celula esta na fila
        Args:
            celula: objeto da classe classe_no()
        Returns:
            boolean que representa se a celula dada esta na fila
        """

        aux = self._inicio
        while aux is not None and aux != celula:
            aux = aux.prox
        return aux is not None


if __name__ == '__main__':
    pass
