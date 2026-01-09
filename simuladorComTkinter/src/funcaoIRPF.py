from .funcaoINSS import calcularINSS

def calcularIRPF(salario=0.0, tipoDeSegurado="", pensao=0.0, dependentes=0, modalidade=""):
    _, _, _, _, baseSimplificada, baseTotal, descontoSimplificado, descontoTotal = calcularINSS(salario, tipoDeSegurado, pensao, dependentes, modalidade)

    # Verificação da base de cálculo e do desconto
    if baseTotal < baseSimplificada:
        baseDeCalculo = round(baseTotal, 2)
        desconto = descontoTotal
    elif baseSimplificada < baseTotal:
        baseDeCalculo = round(baseSimplificada, 2)
        desconto = descontoSimplificado

    
    # Base de cálculo	                | Alíquota	| Dedução
    # Até R$ 2.428,80                   |           | 
    # De R$ 2.428,81 até R$ 2.826,65	| 7,5%	    | R$ 182,16
    # De R$ 2.826,66 até R$ 3.751,05	| 15,0%	    | R$ 394,16
    # De R$ 3.751,06 até R$ 4.664,68	| 22,5%	    | R$ 675,49
    # Acima de R$ 4.664,68	            | 27,5%	    | R$ 908,73

    if baseDeCalculo >= 2259.21 and baseDeCalculo <= 2826.65:
        aliquotaIR = 0.075
        deducao = 182.16
        impostoDeRenda = baseDeCalculo * aliquotaIR - deducao

    elif baseDeCalculo >= 2826.66 and baseDeCalculo <= 3751.05:
        aliquotaIR = 0.15
        deducao = 394.16
        impostoDeRenda = baseDeCalculo * aliquotaIR - deducao

    elif baseDeCalculo >= 3751.06 and baseDeCalculo <= 4664.68:
        aliquotaIR = 0.225
        deducao = 675.49
        impostoDeRenda = baseDeCalculo * aliquotaIR - deducao

    elif baseDeCalculo > 4664.68:
        aliquotaIR = 0.275
        deducao = 908.73
        impostoDeRenda = baseDeCalculo * aliquotaIR - deducao

    else:
        aliquotaIR = 0
        deducao = 0
        impostoDeRenda = 0

    if impostoDeRenda < 0:
        impostoDeRenda = 0
        
    return round(impostoDeRenda, 2), round(aliquotaIR, 2), deducao, baseDeCalculo, desconto