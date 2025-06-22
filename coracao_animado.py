import turtle
import math

# Configuração inicial da tela e do "pincel"
screen = turtle.Screen()
screen.bgcolor("black")  # Fundo preto
screen.title("Coração Animado")

t = turtle.Turtle()
t.speed(0)          # Velocidade mais rápida
t.color("red")      # Cor do desenho
t.pensize(2)        # Espessura da linha

# Função que calcula as coordenadas de um ponto do coração
def calcular_ponto_coracao(n):
    x = 16 * (math.sin(n) ** 3)
    y = 13 * math.cos(n) - 5 * math.cos(2*n) - 2 * math.cos(3*n) - math.cos(4*n)
    return x, y

# Desenha o coração com efeito de crescimento
def desenhar_coracao():
    for i in range(1, 16):  # Vamos desenhar 15 corações
        t.penup()
        t.goto(0, 0)        # Volta ao centro a cada novo coração
        t.pendown()
        
        # Desenha um coração completo
        for n in range(0, 628, 5):  # De 0 a 2*pi (aproximadamente 628/100)
            angulo = n / 100        # Converte para radianos
            x, y = calcular_ponto_coracao(angulo)
            t.goto(x * i, y * i)    # Escala o tamanho pelo fator i
        
        t.penup()

# Executa a função principal
desenhar_coracao()

# Finaliza o programa
t.hideturtle()
screen.mainloop()