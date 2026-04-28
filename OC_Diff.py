# -*- coding: utf-8 -*-
#
# MODULO DE PROTECAO DIFERENCIAL DO OPENCOORD
# Versao de 06/06/2024
# DANILO MANSUR (oliveiramansur@gmail.com)

import matplotlib.pyplot as plt
import numpy as np

def Plotter_Diff(y1_value, x2_start, x2_end, slope2, x3_start, x3_end, slope3, xlim, ylim, point1, point2, max_idiff):
    """
    Plota o gráfico de segmentos de reta com áreas preenchidas e pontos de dispersão.

    Parameters:
    y1_value (float): Valor constante de y para o primeiro segmento de reta.
    x2_start (float): Início do segundo segmento no eixo x.
    x2_end (float): Fim do segundo segmento no eixo x.
    slope2 (float): Inclinação do segundo segmento.
    x3_start (float): Início do terceiro segmento no eixo x.
    x3_end (float): Fim do terceiro segmento no eixo x.
    slope3 (float): Inclinação do terceiro segmento.
    xlim (tuple): Limites dos eixos x.
    ylim (tuple): Limites dos eixos y.
    point1 (tuple): Coordenadas do primeiro ponto de dispersão.
    point2 (tuple): Coordenadas do segundo ponto de dispersão.
    max_idiff (float): Valor máximo de Idiff para a linha horizontal.
    """
    
    # Gerando os dados para os segmentos de reta
    x1 = np.linspace(0.0, x2_start, 100)
    y1 = np.full_like(x1, y1_value)

    x2 = np.linspace(x2_start, x2_end, 100)
    y2 = y1_value + slope2 * (x2 - x2_start)  # Inclinação do segundo segmento

    x3 = np.linspace(x3_start, x3_end, 100)
    y3 = y2[-1] + slope3 * (x3 - x3_start)  # Inclinação do terceiro segmento

    # Gerando dados para a linha tracejada prolongada do segundo segmento
    x_prolong = np.linspace(x2_end, xlim[1], 100)
    y_prolong = y2[-1] + slope2 * (x_prolong - x2_end)

    # Criando o gráfico
    plt.figure(figsize=(8, 6))

    # Pintando as regiões abaixo das retas com a mesma cor azul claro
    plt.fill_between(x1, 0, y1, color='lightblue', alpha=0.5)
    plt.fill_between(x2, 0, y2, color='lightblue', alpha=0.5)
    plt.fill_between(x3, 0, y3, color='lightblue', alpha=0.5)

    # Plotando as retas por cima das áreas preenchidas com a mesma cor azul escuro
    plt.plot(x1, y1, color='darkblue')
    plt.plot(x2, y2, color='darkblue')
    plt.plot(x3, y3, color='darkblue')

    # Plotando a linha tracejada prolongada do segundo segmento, sem adicionar à legenda
    plt.plot(x_prolong, y_prolong, color='blue', linestyle=':')

    # Adicionando uma reta horizontal na parte superior do gráfico
    plt.axhline(y=max_idiff, color='gray', linestyle='--', label='Limite superior de Idiff')

    # Adicionando pontos de dispersão independentes
    plt.scatter([point1[0]], [point1[1]], color='red', marker='*', label='Falta Interna')
    plt.scatter([point2[0]], [point2[1]], color='green', marker='*', label='Falta Externa')
    plt.text(point1[0] + 0.3, point1[1], "Interna.", fontsize=10, bbox=dict(facecolor='white', alpha=0.5))
    plt.text(point2[0] + 0.3, point2[1], "Externa.", fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

    # Adicionando retas pontilhadas partindo da origem até os pontos
    plt.plot([0, point1[0]], [0, point1[1]], 'r--')
    plt.plot([0, point2[0]], [0, point2[1]], 'g--')

    # Adicionando título e legendas
    plt.title('CARACTERÍSTICA DIFERENCIAL - ANSI 87', fontname='Arial', fontsize=16, fontweight='bold')
    plt.xlabel('CORRENTE DE RESTRIÇÃO (Ires) [pu]', fontname='Arial', fontsize=12, fontweight='bold')
    plt.ylabel('CORRENTE DE OPERAÇÃO (Iop) [pu]', fontname='Arial', fontsize=12, fontweight='bold')
    plt.grid(True)

    # Definindo os limites dos eixos
    plt.xlim(xlim)
    plt.ylim(ylim)

    # Exibindo a legenda apenas com a reta horizontal e os pontos de dispersão
    handles, labels = plt.gca().get_legend_handles_labels()
    handles = [h for h, l in zip(handles, labels) if 'Limite superior de Idiff' in l or 'Falta' in l]
    labels = [l for l in labels if 'Limite superior de Idiff' in l or 'Falta' in l]
    plt.legend(handles, labels)
    plt.legend(loc='upper right') 

    # Exibindo as indicações de slope
    plt.text(slope2LegX, slope2LegY, str(slope2 * 100) + "%", fontsize=10, bbox=dict(facecolor='white', alpha=0.5))
    plt.text(slope3LegX, slope3LegY, str(slope3 * 100) + "%", fontsize=10, bbox=dict(facecolor='white', alpha=0.5))

    # Exibindo o gráfico
    plt.show()

def Calc_Diff():
    """
    Define os parâmetros geométricos e limites dos eixos para o gráfico diferencial.
    """
    global y1_value 
    global x2_start
    global x2_end
    global slope2
    global x3_start
    global x3_end
    global slope3
    global xlim
    global ylim
    global point1
    global point2
    global max_idiff

    global slope2LegX
    global slope2LegY
    global slope3LegX
    global slope3LegY

    # OBRIGATORIO: Definindo os parâmetros geométricos e limites dos eixos
    y1_value = 0.2       # corrente diferencial (Id) minima
    x2_start = 1.5       # inicio do primeiro slope
    x2_end = 7.5         # fim do primeiro slope
    slope2 = 0.40      # inclinacao do primeiro slope
    x3_start = x2_end    # corrente de restricao para inicio do 2o slope
    x3_end = 20         # termino da area de restricao
    slope3 = 0.45         # inclinacao do segundo slope
    max_idiff = 2       # threshold superior de atuação sem restrição

    point1 = (0.356, 0.71)  # falta interna  (IRES, IDIF)
    point2 = (1.8, 0.03)  # falta externa (IRES, IDIF)

    #OPCIONAL: posicoes de legendas e caixas de texto
    xlim = (0, 4)
    ylim = (0, 2.2)
    slope2LegX = 2.5
    slope2LegY = 1.0
    slope3LegX = 20.5
    slope3LegY = 10.5


def main():
    Calc_Diff()
    Plotter_Diff(y1_value, x2_start, x2_end, slope2, x3_start, x3_end, slope3, xlim, ylim, point1, point2, max_idiff)
    return 0

if __name__ == "__main__":
    main()
