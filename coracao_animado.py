"""
CORAÇÃO ANIMADO - Versão PC para Visualização Mobile
Autor: [Seu Nome]
Descrição: Código desenvolvido no VS Code PC, mas otimizado para ficar perfeito em dispositivos móveis
"""

import turtle
import math
import time

# ============= CONFIGURAÇÕES VISUAIS =============
def configurar_tela():
    """Prepara a janela com dimensões ideais para mobile"""
    screen = turtle.Screen()
    screen.setup(width=360, height=640)  # Proporção de celular (9:16)
    screen.bgcolor('#0a0a0a')  # Preto levemente acinzentado
    screen.title("❤️ Coração Animado ❤️")
    screen.tracer(0)  # Desativa atualização automática para melhor performance
    return screen

def configurar_caneta():
    """Configura o objeto turtle para desenho suave"""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(3)
    t.color('#ff3366')  # Rosa-vermelho vibrante
    return t

# ============= CÁLCULO DO CORAÇÃO =============
def calcular_ponto(angulo_rad):
    """Calcula as coordenadas x,y usando equação paramétrica otimizada"""
    seno = math.sin(angulo_rad)
    cosseno = math.cos(angulo_rad)
    
    x = 15 * (seno ** 3)
    y = 12 * cosseno - 4 * math.cos(2*angulo_rad) - 2 * math.cos(3*angulo_rad) - math.cos(4*angulo_rad)
    
    return x * 10, y * 10  # Aumenta o tamanho

# ============= ANIMAÇÃO PRINCIPAL =============
def animar_coracao():
    """Controla o fluxo da animação com efeitos suaves"""
    screen = configurar_tela()
    t = configurar_caneta()
    
    try:
        for frame in range(150):  # 150 frames de animação
            t.clear()
            
            # Calcula um fator de escala pulsante
            pulsacao = 0.8 + 0.2 * math.sin(frame * 0.1)
            
            # Desenha o coração
            t.begin_fill()
            for angulo in range(0, 628, 15):  # 6.28 radianos (360°)
                x, y = calcular_ponto(angulo/100)
                t.goto(x * pulsacao, y * pulsacao)
                if angulo == 0:
                    t.pendown()
            t.end_fill()
            
            # Atualiza a tela de forma otimizada
            screen.update()
            time.sleep(0.05)  # Controla a velocidade
            
    except turtle.Terminator:
        pass  # Permite fechar a janela sem erros
    
    screen.mainloop()

# ============= EXECUÇÃO =============
if __name__ == "__main__":
    animar_coracao()
