from pygame.locals import QUIT
import pygame

from config import (
    COLORS, BACKGROUND_COLOR, GRID_SIZE, RESOLUCAO,
    KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP,
    SCREEN, COBRA_CELL_SURFACE,
    GAME_CLOCK)

from fila import Fila
from utils import CelulaDaCobra, Ponto, posicao_aleatoria, elemento_aleatorio


class Cobrinha:
    """
    Classe para o jogo da cobrinha
    Attributes:
        GAME_OVER: boolean
        cobrinha: Fila( class_no= Celula Da Cobra )
        direcao: int que pode ser (KEY_DOWN, KEY_UP, KEY_LEFT ou KEY_RIGHT)
    """

    def __init__(self):
        """Contrutor da classe"""

        pygame.init()
        self.GAME_OVER = False
        self.cobrinha = Fila(class_no=CelulaDaCobra)
        self.comidas = Fila(class_no=CelulaDaCobra)
        self.direcao = KEY_RIGHT
        self.TICK = 10

        for i in range(50):
            self.add_celula_na_cobra()

        for i in range(3):
            self.adicionar_comida()

    def run(self):
        """Metodo que executa loop do jogo"""

        while not self.GAME_OVER:
            GAME_CLOCK.tick(self.TICK)
            self.verifica_eventos()
            self.atualizar_posicao_da_cobrinha()
            self.atualizar_tela()
            pygame.display.update()

        self.sair()

    def verifica_eventos(self):
        """Metodo para tratar o evento do jogo"""

        for evento in pygame.event.get():
            if evento.type == QUIT:
                self.sair()
            elif evento.type == pygame.KEYDOWN:
                self.set_direcao(evento.key)

    def set_direcao(self, evento):
        """
        Altera a direcao do movimento da cobrinha de acordo com a tecla
        pressionada pelo usuario
        """

        if evento == pygame.K_UP and self.direcao != KEY_DOWN:
            self.direcao = KEY_UP
        elif evento == pygame.K_DOWN and self.direcao != KEY_UP:
            self.direcao = KEY_DOWN
        elif evento == pygame.K_LEFT and self.direcao != KEY_RIGHT:
            self.direcao = KEY_LEFT
        elif evento == pygame.K_RIGHT and self.direcao != KEY_LEFT:
            self.direcao = KEY_RIGHT

    def atualizar_tela(self):
        """Metodo para mostrar na tela todas as novas posicoes"""

        SCREEN.fill(BACKGROUND_COLOR)
        aux = self.cobrinha.primeiro
        while aux is not None:
            COBRA_CELL_SURFACE.fill(aux.cor)
            SCREEN.blit(COBRA_CELL_SURFACE, aux.coordenadas())
            aux = aux.prox

        aux = self.comidas.primeiro
        while aux is not None:
            COBRA_CELL_SURFACE.fill(aux.cor)
            SCREEN.blit(COBRA_CELL_SURFACE, aux.coordenadas())
            aux = aux.prox

    def atualizar_posicao_da_cobrinha(self):
        """Metodo para autializar a posicao de cada celula da cobrinha"""

        aux = self.cobrinha.primeiro
        posicao_anterior = aux.coordenadas()

        proxima_posicao = self.get_proxima_posicao_da_cabeca()
        self.validar_posicao(proxima_posicao)
        # proxima posicao da cabeca (dependendo da direcao atual da cobra)
        # em seguida, chama funcao para verificar se essa nova posicao é uma posicao
        # já presente na cobrinha, ou seja, está passando por cima dela mesmas

        aux.set_coordenadas(proxima_posicao.x, proxima_posicao.y)  # atualiza o primeiro
        aux = aux.prox
        while aux is not None:
            posicao_do_aux = aux.coordenadas()
            # salvar posicao da celula, antes de altrar, para entao passar essa
            # posicao antiga para a celula da frente

            aux.set_coordenadas(posicao_anterior[0], posicao_anterior[1])
            posicao_anterior = posicao_do_aux

            aux = aux.prox

    def sair(self):
        """Metodo para finalizar o jogo"""

        self.GAME_OVER = True

    def add_celula_na_cobra(self):
        """Metodo para adicionar uma celula na cobra"""

        cor = elemento_aleatorio(COLORS)

        if self.cobrinha.esta_vazia():
            ponto = posicao_aleatoria(RESOLUCAO, GRID_SIZE)
        else:
            ultimo = self.cobrinha.ultimo
            ponto = Ponto(ultimo.x, ultimo.y)

            if self.direcao == KEY_UP:
                ponto.y -= GRID_SIZE
            elif self.direcao == KEY_DOWN:
                ponto.y += GRID_SIZE
            elif self.direcao == KEY_RIGHT:
                ponto.x -= GRID_SIZE
            elif self.direcao == KEY_LEFT:
                ponto.x += GRID_SIZE

            # Em caso de terem duas cores na iguais na sequencia,
            # o loop abaixo executara até que as cores sejam diferentes
            while cor == ultimo.cor:
                cor = elemento_aleatorio(COLORS)

        self.cobrinha.insere(x=ponto.x, y=ponto.y, cor=cor)

    def adicionar_comida(self):
        """Metodo para adicionar uma comida em uma posicao aleatoria"""
        cor = elemento_aleatorio(COLORS)
        ponto = posicao_aleatoria(RESOLUCAO, GRID_SIZE)

        while self.cobrinha.esta_presente(ponto):  # nao permitir colocar comida em cima da cobra
            ponto = posicao_aleatoria(RESOLUCAO, GRID_SIZE)

        self.comidas.insere(x=ponto.x, y=ponto.y, cor=cor)

    def get_proxima_posicao_da_cabeca(self):
        """
        Metodo para calcular a nova posicao da cabeca durante o movinto da cobrinha

        Returns:
            Ponto() com a nova coordenada
        """
        ponto = Ponto(self.cobrinha.primeiro.x, self.cobrinha.primeiro.y)

        if self.direcao == KEY_UP:
            ponto.y -= GRID_SIZE
        elif self.direcao == KEY_DOWN:
            ponto.y += GRID_SIZE
        elif self.direcao == KEY_LEFT:
            ponto.x -= GRID_SIZE
        else:
            ponto.x += GRID_SIZE

        # verificar se a posicao está fora da resolucao da tela
        # caso tivar, mover a posicao para a lateral oposta
        if ponto.x < 0:  # se estiver fora da lateral esquerda
            ponto.x = RESOLUCAO.x - GRID_SIZE
        elif ponto.x >= RESOLUCAO.x:  # se estiver fora da lateral direita
            ponto.x = 0

        if ponto.y < 0:  # se estiver fora da lateral de cima
            ponto.y = RESOLUCAO.y - GRID_SIZE
        elif ponto.y >= RESOLUCAO.y:  # se estiver fora da lateral de baixo
            ponto.y = 0

        return ponto

    def validar_posicao(self, posicao):
        """
        Metado para fazer todas as verificacoes da posicao
        """
        if self.cobrinha.esta_presente(posicao):
            self.cobrinha.remove()  # remove a cabeca
            if self.cobrinha.esta_vazia():
                self.sair()

        elif self.comidas.esta_presente(posicao):
            self.handle_comer_comida(posicao)

    def handle_comer_comida(self, posicao_da_comida):
        """Metodo que trata as acoes quando a cobra comer uma comida"""

        nova_fila_de_comidas = Fila(class_no=CelulaDaCobra)

        while self.comidas.esta_vazia() is False:
            comida = self.comidas.remove()

            if comida == posicao_da_comida:
                self.adicionar_comida()
                if comida.cor == self.cobrinha.primeiro.cor:
                    self.cobrinha.remove()
                else:
                    self.add_celula_na_cobra()
            else:
                nova_fila_de_comidas.insere(x=comida.x, y=comida.y, cor=comida.cor)

        if self.cobrinha.esta_vazia():
            self.sair()
        self.comidas = nova_fila_de_comidas


if __name__ == "__main__":
    jogo = Cobrinha()
    jogo.run()
