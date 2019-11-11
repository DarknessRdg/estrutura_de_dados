from pygame.locals import QUIT
import pygame

from config import (
    COLORS, BACKGROUND_COLOR, GRID_SIZE, RESOLUCAO,
    KEY_DOWN, KEY_LEFT, KEY_RIGHT, KEY_UP,
    SCREEN, COBRA_CELL_SURFACE, ESPACO_ENTRE_CELULAS,
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
        self.direcao = KEY_RIGHT
        self.TICK = 10

        for i in range(5):
            self.add_celula_na_cobra()

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

    def atualizar_posicao_da_cobrinha(self):
        aux = self.cobrinha.primeiro
        posicao_anterior = aux.coordenadas()

        proxima_posicao = self.get_proxima_posicao(aux)
        aux.set_coordenadas(proxima_posicao.x, proxima_posicao.y)
        aux = aux.prox
        while aux is not None:
            posicao_do_aux = aux.coordenadas()

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
            ponto = self.get_proxima_posicao(ultimo)

            # Em caso de terem duas cores na iguais na sequencia,
            # o loop abaixo executara até que as cores sejam diferentes
            while cor == ultimo.cor:
                cor = elemento_aleatorio(COLORS)

        self.cobrinha.insere(x=ponto.x, y=ponto.y, cor=cor)

    def get_proxima_posicao(self, posicao_atual):
        """
        Metodo para calcular a nova posicao, dada a posicao atual
        Args:
            posicao_atual: instacia da classe Ponto
        Returns:
            Ponto() com a nova coordenada
        """
        ponto = Ponto(posicao_atual.x, posicao_atual.y)

        if self.direcao == KEY_UP:
            ponto.y -= GRID_SIZE + ESPACO_ENTRE_CELULAS
        elif self.direcao == KEY_DOWN:
            ponto.y += GRID_SIZE + ESPACO_ENTRE_CELULAS
        elif self.direcao == KEY_LEFT:
            ponto.x -= GRID_SIZE + ESPACO_ENTRE_CELULAS
        else:
            ponto.x += GRID_SIZE + ESPACO_ENTRE_CELULAS
        return ponto

    def validar_posicao(self, posicao):
        """
        Metado para
        """


if __name__ == "__main__":
    jogo = Cobrinha()
    jogo.run()
