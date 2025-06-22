import turtle
import math
import time

# Configuração inicial otimizada
screen = turtle.Screen()
screen.setup(width=360, height=640)  # Proporção mobile
screen.bgcolor("#f5f5f5")
screen.title("❤️ Coração Completo a Lápis ❤️")
screen.tracer(0)  # Melhora performance

# Cria o lápis
pencil = turtle.Turtle()
pencil.speed(0)
pencil.color("#ff3366")  # Vermelho vibrante
pencil.pensize(3)
pencil.hideturtle()

# Cria um segundo turtle para o preenchimento
fill = turtle.Turtle()
fill.speed(0)
fill.color("#ff3366")
fill.pensize(1)
fill.hideturtle()
fill.begin_fill()  # Começa o preenchimento

# Cursor em forma de lápis
screen.register_shape("pencil", ((-3,0), (0,8), (3,0)))
pencil.shape("pencil")
pencil.showturtle()

# Fórmula do coração otimizada
def heart_pos(t):
    x = 15 * (math.sin(t)**3)
    y = 12*math.cos(t) - 4*math.cos(2*t) - 2*math.cos(3*t) - math.cos(4*t)
    return x*10, y*10

# Animação principal
try:
    pencil.penup()
    fill.penup()
    
    # Primeiro ponto
    x, y = heart_pos(0)
    pencil.goto(x, y)
    fill.goto(x, y)
    pencil.pendown()
    fill.pendown()
    
    for i in range(0, 630, 3):  # Passo maior = melhor performance
        t = i/100
        x, y = heart_pos(t)
        
        # Move o lápis
        pencil.goto(x, y)
        
        # Move o preenchimento
        fill.goto(x, y)
        
        # Atualiza ângulo do lápis
        if i < 627:
            next_x, next_y = heart_pos((i+3)/100)
            angle = math.degrees(math.atan2(next_y-y, next_x-x))
            pencil.setheading(angle)
        
        screen.update()
        time.sleep(0.02)  # Controla velocidade
    
    # Completa o preenchimento
    fill.end_fill()
    
    # Efeito final
    for _ in range(2):
        pencil.color("#ff9999")
        fill.color("#ff9999")
        screen.update()
        time.sleep(0.15)
        pencil.color("#ff3366")
        fill.color("#ff3366")
        screen.update()
        time.sleep(0.15)

except:
    pass

screen.mainloop()
