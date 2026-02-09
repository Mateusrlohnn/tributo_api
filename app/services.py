def calcular_simples(faturamento: float):
    return faturamento * 0.08


def calcular_presumido(faturamento: float):
    return faturamento * 0.13


def calcular_real(faturamento: float, margem_lucro: float = 0.15):
    lucro = faturamento * margem_lucro
    return lucro * 0.24


def comparar_regimes(faturamento: float, margem_lucro: float = 0.15):
    simples = calcular_simples(faturamento)
    presumido = calcular_presumido(faturamento)
    real = calcular_real(faturamento, margem_lucro)

    impostos = {
        "Simples Nacional": simples,
        "Lucro Presumido": presumido,
        "Lucro Real": real
    }

    melhor = min(impostos, key=impostos.get)

    return simples, presumido, real, melhor
