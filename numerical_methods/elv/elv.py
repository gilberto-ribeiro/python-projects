import math
import num_functions as nf


def pressao_de_vapor(temperatura, componente, parametros):
    constantes = ('A', 'B', 'C')
    A, B, C = (parametros[componente][constante] for constante in constantes)
    T = temperatura
    lnP = A - B/(T - C)
    P = math.exp(lnP)
    dlnP_dT = B/(T - C)**2
    return P, dlnP_dT


def lambda_(temperatura, componente, parametros):
    constantes = ('a', 'b')
    a, b = (parametros[componente][constante] for constante in constantes)
    T = temperatura
    L = a * math.exp(b / T)
    dL_dT = -((a*b)/T**2) * math.exp(b/T)
    return L, dL_dT


def gamma_(fracao_molar, temperatura, componentes, parametros):
    x = [fracao_molar, 1 - fracao_molar]
    T = temperatura
    L = [lambda_(T, componente, parametros)[0] for componente in componentes]
    dL_dT = [lambda_(T, componente, parametros)[1] for componente in componentes]
    exp = [x[i] + x[j]*L[i] for i, j in [(0, 1), (1, 0)]]
    lngamma, gamma, dlngamma_dT, dlngamma_dx1 = [], [], [], []
    for i, j in [(0, 1), (1, 0)]:
        lngamma.append(1 - math.log(exp[i]) - (x[i])/(exp[i]) - (x[j]*L[j])/(exp[j]))
        gamma.append(math.exp(lngamma[i]))
        dlngamma_dT.append(-(dL_dT[i]*x[j])/(exp[i]) + (dL_dT[i]*x[i]*x[j])/(exp[i]**2) - (dL_dT[j]*x[j]**2)/(exp[j]**2))
        dlngamma_dx1.append(((-1)**i)*((L[i]-1)/(exp[i]) + (L[j]**2)/(exp[j]**2) - (L[i])/(exp[i]**2)))
    return gamma, dlngamma_dT, dlngamma_dx1


def g(fracao_molar, temperatura):
    x = [fracao_molar, 1 - fracao_molar]
    T = temperatura[0]
    P = [pressao_de_vapor(T, componente, parametros)[0] for componente in componentes]
    dlnP_dT = [pressao_de_vapor(T, componente, parametros)[1] for componente in componentes]
    gamma, dlngamma_dT, dlngamma_dx1 = gamma_(x[0], T, componentes, parametros)
    df_dT = sum([x[i]*gamma[i]*P[i]*(dlngamma_dT[i]+dlnP_dT[i]) for i in range(2)])
    df_dx1 = sum([gamma[i]*P[i]*(x[i]*dlngamma_dx1[i]+(-1)**i) for i in range(2)])
    dTdx1 = -df_dx1/df_dT
    return [dTdx1]


def f(temperatura):
    T = temperatura
    x = [0, 1]
    gamma = gamma_(x[0], T, componentes, parametros)[0]
    P = [pressao_de_vapor(T, componente, parametros)[0] for componente in componentes]
    return sum([x[i]*gamma[i]*P[i] for i in range(2)]) - P0


def df(temperatura):
    T = temperatura
    x = [0, 1]
    P = [pressao_de_vapor(T, componente, parametros)[0] for componente in componentes]
    dlnP_dT = [pressao_de_vapor(T, componente, parametros)[1] for componente in componentes]
    gamma = gamma_(x[0], T, componentes, parametros)[0]
    dlngamma_dT = gamma_(x[0], T, componentes, parametros)[1]
    return sum([x[i]*gamma[i]*P[i]*(dlngamma_dT[i]+dlnP_dT[i]) for i in range(2)])


componentes = ('acetato_de_metila', 'metanol')
parametros = {
    'acetato_de_metila': {
        'A': 16.5835, 'B': 2838.7, 'C': 45.16,
        'a': 0.5108, 'b': 54.9958
    },
    'metanol': {
        'A': 18.1412, 'B': 3391.96, 'C': 43.16,
        'a': 1.9578, 'b': -467.79
    }
}

P0 = 760

T0 = nf.nr(f, df, 298)

funcao = nf.rungekutta(g, [0, 1], [T0], 10)

y1 = list()
for x1, T in zip(funcao['x'], funcao['y']):
    T = T[0]
    gamma1 = gamma_(x1, T, componentes, parametros)[0][0]
    P1 = pressao_de_vapor(T, componentes[0], parametros)[0]
    y1.append(x1*gamma1*P1/P0)

nf.dados_edo(funcao, 'elv_x_cor')

funcao['x'] = y1
nf.dados_edo(funcao, 'elv_y_cor')