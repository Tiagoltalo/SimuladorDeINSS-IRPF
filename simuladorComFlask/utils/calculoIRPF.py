from calculoINSS import calcularINSS

def tabelaDoIRPF(baseDeCalculo):
    if baseDeCalculo >= 2428.80 and baseDeCalculo <= 2826.65:
        aliquotaIR = 0.075
        deducao = 182.16

    elif baseDeCalculo >= 2826.66 and baseDeCalculo <= 3751.05:
        aliquotaIR = 0.15
        deducao = 394.16

    elif baseDeCalculo >= 3751.06 and baseDeCalculo <= 4664.68:
        aliquotaIR = 0.225
        deducao = 675.49

    elif baseDeCalculo > 4664.68:
        aliquotaIR = 0.275
        deducao = 908.73

    return deducao, aliquotaIR


def calcularIRPF(salario=0.0, tipoDeSegurado="", pensao=0.0, dependentes=0, modalidade=""):
    _, _, _, _, descontoSimplificado, descontoTotal = calcularINSS(salario, tipoDeSegurado, pensao, dependentes, modalidade)

    # Verificação do desconto mais vantajoso
    if descontoSimplificado > descontoTotal:
        desconto = descontoSimplificado
    else:
        desconto = descontoTotal

    # Acima de R$ 7.500,00
    # Base de cálculo	                | Alíquota	| Dedução
    # Até R$ 2.428,80                   |           | 
    # De R$ 2.428,81 até R$ 2.826,65	| 7,5%	    | R$ 182,16
    # De R$ 2.826,66 até R$ 3.751,05	| 15,0%	    | R$ 394,16
    # De R$ 3.751,06 até R$ 4.664,68	| 22,5%	    | R$ 675,49
    # Acima de R$ 4.664,68	            | 27,5%	    | R$ 908,73

    if descontoSimplificado > descontoTotal:
        desconto = descontoSimplificado
    else:
        desconto = descontoTotal

    baseDeCalculo = salario - desconto

    if baseDeCalculo < 5000:
        deducao, aliquotaIR = tabelaDoIRPF(baseDeCalculo)
        reducao = 312.89
        impostoDeRenda = (baseDeCalculo * aliquotaIR) - deducao - reducao

    elif baseDeCalculo > 5000 and baseDeCalculo <= 7350:
        deducao, aliquotaIR = tabelaDoIRPF(baseDeCalculo)
        reducao = 978.62 - (salario * 0.133145)
        impostoDeRenda = (baseDeCalculo * aliquotaIR) - deducao - reducao

    elif baseDeCalculo > 7350:
        baseDeCalculo -= 7350
        deducao, aliquotaIR = tabelaDoIRPF(baseDeCalculo)
        reducao = 0
        impostoDeRenda = (baseDeCalculo * aliquotaIR) - deducao

    if impostoDeRenda < 0:
        impostoDeRenda = 0

    return round(impostoDeRenda, 2), round((aliquotaIR * 100), 2), deducao, baseDeCalculo, desconto, round(reducao, 2)