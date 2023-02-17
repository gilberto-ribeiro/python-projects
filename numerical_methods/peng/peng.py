import math


def subintervalos(inicio, fim, passos = 1000):
    N = int(passos)
    h = (fim - inicio)/N
    pontos = [float(inicio)]
    for i in range(N):
        pontos.append(pontos[i] + h)
    intervalos = [(pontos[i], pontos[i+1]) for i in range(N)]
    return pontos, intervalos, h


def imprimir_dados(temperatura_reduzida, pressao_reduzida, constantes_criticas):
    temperatura_critica = constantes_criticas[0]
    pressao_critica = constantes_criticas[1]

    dados = list()
    for pr in pressao_reduzida:
        linha = list()
        for tr in temperatura_reduzida:
            p = pr * pressao_critica
            t = tr * temperatura_critica
            linha.append(peng_robinson(t, p, constantes_criticas))
        dados.append(linha)

    with open('dados_peng', 'w') as arquivo:
        for p, linha in zip(pressao_reduzida, dados):
            linha = [str(i) for i in linha]
            linha = ' '.join(linha)
            p = str(p)
            arquivo.write(p+' '+linha+'\n')
        arquivo.close()


def newton_rhapson(f, df, x_estimado, erro = 1e-8, maximo_de_iteracoes = 100):
    x = [x_estimado]
    erro_relativo = [math.nan]
    for i in range(maximo_de_iteracoes):
        x.append(x[i] - f(x[i]) / df(x[i]))
        if i > 0:
            erro_relativo.append(abs((x[i] - x[i-1]) / x[i-1]))
        if erro_relativo[i] <= erro:
            break
    return x[-1]


def peng_robinson(temperatura, pressao, constantes_criticas, estimativa_inicial = 1):


    def equacao_de_estado(Z):
        return Z**3 - (1 - B) * Z**2 + (A - 3 * B**2 - 2*B) * Z - (A*B - B**2 - B**3)


    def derivada_da_equacao_de_estado(Z):
        return 3 * Z**2 - 2 * (1 - B) * Z + (A - 3 * B**2 - 2*B)


    R = 8.3145 # Constante dos gases ideais

    Tc = constantes_criticas[0] # Temperatura crítica, K
    Pc = constantes_criticas[1] # Pressão crítica, Pa
    omega = constantes_criticas[2] # Fator acêntrico

    T = temperatura # Temperatura, K
    P = pressao # Pressão, bar

    Tr = T / Tc # Temperatura reduzida

    kappa = 0.37464 + 1.54226 * omega - 0.26992 * omega**2 # Constante característica
    alpha = (1 + kappa * (1 - math.sqrt(Tr)))**2 # Fator de escala

    a_Tc = 0.45724 * (R**2 * Tc**2) / Pc
    b_Tc = 0.07780 * (R * Tc) / Pc

    a = a_Tc * alpha # Parâmetro de atração
    b = b_Tc # Covolume de Van der Walls

    A = (a * P) / (R**2 * T**2) # Constante da equação de estado
    B = (b * P) / (R * T) # Constante da equação de estado

    Z = newton_rhapson(equacao_de_estado, derivada_da_equacao_de_estado, estimativa_inicial)

    return Z


# Constantes críticas do Metano
# Tabela 2-141 do Perry 8a Edição
temperatura_critica = 190.564 # K
pressao_critica = 4.599e6 # Pa
fator_acentrico = 0.0115

constantes_criticas = (temperatura_critica, pressao_critica, fator_acentrico)

T = [200, 250, 300, 400, 500, 600]
for temp in T:
    z = peng_robinson(temp, 5000000, constantes_criticas, 1)
    print(temp,z)

# pressao_reduzida = subintervalos(0, 6)[0]
# temperatura_reduzida = [1, 1.1, 1.2, 1.3, 1.5, 2]

# imprimir_dados(temperatura_reduzida, pressao_reduzida, constantes_criticas)