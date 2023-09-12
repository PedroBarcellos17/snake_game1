import random
from turtle import Turtle

class Cobra:
    POS_INICIAL = [(0,0), (0,20)]
    VEL = 10
    DIREITA = 0
    ESQUERDA = 180
    CIMA = 90
    BAIXO = 270
    def __init__(self):
        self.corpo = []
        self.inicializar_cobra()
        self.cabeca = self.corpo[0]

    def mover(self):
        for index in range(len(self.corpo) -1, 0, -1):
            novo_x, novo_y = self.corpo[index -1].xcor(), self.corpo[index -1].ycor()
            self.corpo[index].goto(novo_x, novo_y)
        self.cabeca.forward(self.VEL)
    def crescer_cobra(self):
        self.novo_segmento(self.corpo[-1].pos())
    def inicializar_cobra(self):
        for pos in self.POS_INICIAL:
            self.novo_segmento(pos)
    def novo_segmento(self, pos):
        nova_cobra = Turtle()
        nova_cobra.shape('square')
        nova_cobra.color(random.choice(self.sorteia_cores()))
        nova_cobra.penup()
        nova_cobra.goto(pos)
        self.corpo.append(nova_cobra)
    def sorteia_cores(self):
        cores = ['brown', 'blue', 'purple', 'white', 'black', 'cyan', 'grey', 'yellow']
        return cores
    def mover_direita(self):
        if self.cabeca.heading() != self.ESQUERDA:
            self.cabeca.setheading(self.DIREITA)
    def mover_esquerda(self):
        if self.cabeca.heading() != self.DIREITA:
            self.cabeca.setheading(self.ESQUERDA)
    def mover_cima(self):
        if self.cabeca.heading() != self.BAIXO:
            self.cabeca.setheading(self.CIMA)
    def mover_baixo(self):
        if self.cabeca.heading() != self.CIMA:
            self.cabeca.setheading(self.BAIXO)