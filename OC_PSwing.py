import numpy as np
import matplotlib.pyplot as plt

def plot_quadrilateros(largura1, altura1, largura2, altura2, angulo, 
                       xlim, ylim, L, teta, rotacao):
    # Conversão de ângulos para radianos
    angulo_rad = np.radians(angulo)
    teta_rad = np.radians(teta)
    rotacao_rad = np.radians(rotacao)
    
    # Coordenadas dos vértices do primeiro quadrilátero (Q1)
    x1_base = -largura1 / 2
    x1_topo = largura1 / 2
    y1_base = -altura1 / 2
    y1_topo = altura1 / 2
    
    # Coordenadas dos vértices do segundo quadrilátero (Q2)
    x2_base = -largura2 / 2
    x2_topo = largura2 / 2
    y2_base = -altura2 / 2
    y2_topo = altura2 / 2
    
    # Deslocamento horizontal baseado no ângulo e na altura
    deslocamento1 = (altura1 / 2) * np.tan(angulo_rad)
    deslocamento2 = (altura2 / 2) * np.tan(angulo_rad)
    
    # Vértices do primeiro quadrilátero após deslocamento
    x1 = np.array([x1_base - deslocamento1, x1_topo - deslocamento1, 
                   x1_topo + deslocamento1, x1_base + deslocamento1])
    y1 = np.array([y1_base, y1_base, y1_topo, y1_topo])
    
    # Vértices do segundo quadrilátero após deslocamento
    x2 = np.array([x2_base - deslocamento2, x2_topo - deslocamento2, 
                   x2_topo + deslocamento2, x2_base + deslocamento2])
    y2 = np.array([y2_base, y2_base, y2_topo, y2_topo])
    
    # Função para rotacionar pontos
    def rotacionar_pontos(x, y, angulo):
        x_rot = x * np.cos(angulo) - y * np.sin(angulo)
        y_rot = x * np.sin(angulo) + y * np.cos(angulo)
        return x_rot, y_rot
    
    # Rotacionar os quadriláteros
    x1_rot, y1_rot = rotacionar_pontos(x1, y1, rotacao_rad)
    x2_rot, y2_rot = rotacionar_pontos(x2, y2, rotacao_rad)
    
    # Coordenadas da reta inclinada partindo da origem
    x_reta = L * np.cos(teta_rad)
    y_reta = L * np.sin(teta_rad)
    
    # Plotar os quadriláteros
    plt.figure()
    plt.fill(x1_rot, y1_rot, 'b', alpha=0.5, label='Zona Externa')
    plt.fill(x2_rot, y2_rot, 'r', alpha=0.5, label='Zona Interna')
    
    # Plotar a reta inclinada
    plt.plot([0, x_reta], [0, y_reta], 'g', linewidth=2, label='LT')
    
    # Adicionar pequenos traços perpendiculares nos extremos do segmento
    offset = 0.2  # Tamanho dos traços
    plt.plot([0 - offset * np.sin(teta_rad), 0 + offset * np.sin(teta_rad)], 
             [0 + offset * np.cos(teta_rad), 0 - offset * np.cos(teta_rad)], 'g')
    plt.plot([x_reta - offset * np.sin(teta_rad), x_reta + offset * np.sin(teta_rad)], 
             [y_reta + offset * np.cos(teta_rad), y_reta - offset * np.cos(teta_rad)], 'g')
    
    # Configurações do gráfico
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.gca().set_aspect('equal', adjustable='box')
    
    # Títulos do gráfico e dos eixos
    plt.title('Função de Restrição por Oscilação de Potência (ANSI 68OSB)')
    plt.xlabel('Resistência (Ohm)')
    plt.ylabel('Reatância (Ohm)')
    
    plt.show()

# Parâmetros dos quadriláteros, ângulo de inclinação, limites dos eixos, comprimento e ângulo da reta, rotação
largura1 = 8
altura1 = 8

largura2 = 5
altura2 = 6
angulo = 15

xlim = (-8, 8)
ylim = (-6, 6)

#Parametros da LT
L = 2.3
teta = 85
rotacao = 0

# Chamar a função para plotar os quadriláteros e a reta
plot_quadrilateros(largura1, altura1, largura2, altura2, angulo, xlim, ylim, L, teta, rotacao)



