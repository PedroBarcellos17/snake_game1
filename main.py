from turtle import Screen
from campo import Campo
from cobra import Cobra
import time
from maca import Maca
from pontuacao import Pontuacao
tela = Screen()
tela.title('Jogo da Cobrinha')
tela.setup(600,620)
tela.tracer(0)
tela.bgcolor('beige')
campo = Campo()
cobra = Cobra()
pontuacao = Pontuacao()
tela.listen()
tela.onkey(cobra.mover_direita, 'd')
tela.onkey(cobra.mover_esquerda, 'a')
tela.onkey(cobra.mover_cima, 'w')
tela.onkey(cobra.mover_baixo, 's')
maca = Maca()
jogo_on = True
while jogo_on:
    time.sleep(0.1)
    if cobra.cabeca.distance(maca)< 20:
        maca.nova_maca()
        cobra.crescer_cobra()
        pontuacao.marca_ponto()
    cobra.mover()
    if cobra.cabeca.xcor() > 285 or cobra.cabeca.xcor() < -285 or cobra.cabeca.ycor() < -285 or cobra.cabeca.ycor() > 285:
        pontuacao.game_over()
        jogo_on = False
        print('Cobra morreu')
    tela.update()
tela.exitonclick()
