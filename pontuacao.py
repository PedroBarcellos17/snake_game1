from turtle import Turtle


class Pontuacao(Turtle):
    def __init__(self):
        super(Pontuacao, self).__init__()
        self.penup()
        self.goto(0, 285)
        self.pontuacao = -10
        self.hideturtle()
        self.mostra_ponto()

    def marca_ponto(self):
        self.pontuacao += 10
        self.mostra_ponto()

    def mostra_ponto(self, nome='Jogador'):
        self.clear()
        self.write(f'{self.pontuacao} / {nome}',
                   font=('arial', 15, 'bold'), align='center')

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f'{self.pontuacao} VOCÊ PERDEU', font=(
            'arial', '30', 'bold'), align='center')
