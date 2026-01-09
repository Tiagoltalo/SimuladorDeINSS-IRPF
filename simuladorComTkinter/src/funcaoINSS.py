from .arquivoAuxiliar import seguradosComAliquotaProgressiva, seguradosSemAliquotaProgressiva, tiposDeModalidade

def calcularINSS(salario=0.0, tipoDeSegurado="", pensao=0.0, dependentes=0, modalidade=""):
    deducaoPorDependente = 189.59
    descontoSimplificado = 607.20

    deducaoTotalDosDependente = deducaoPorDependente * dependentes
    
    if tipoDeSegurado in seguradosComAliquotaProgressiva:

        # (Empregado, Empregado Doméstico e Trabalhador Avulso)
        # Salário de Contribuição (R$) | Alíquota | Dedução
        # Até 1.518,00			       | 7,5%     | 
        # De 1.518,01 a 2.793,88	   | 9%       | 22,77
        # De 2.793,89 até 4.190,83	   | 12%      | 106,59
        # De 4.190,84 até 8.157,41	   | 14%      | 190,40
       
        if salario <= 1518:
            aliquotaDoINSS = 0.075
            contribuicaoDoINSS = salario * aliquotaDoINSS

        elif salario > 1518 and salario <= 2793.88:
            deducaoDoINSS = 22.77
            aliquotaDoINSS = 0.09
            contribuicaoDoINSS = salario * aliquotaDoINSS - deducaoDoINSS

        elif salario > 2793.88 and salario <= 4190.83:
            deducaoDoINSS = 106.59
            aliquotaDoINSS = 0.12
            contribuicaoDoINSS = salario * aliquotaDoINSS - deducaoDoINSS

        elif salario > 4190.83:
            deducaoDoINSS = 190.40
            aliquotaDoINSS = 0.14
            contribuicaoDoINSS = salario * aliquotaDoINSS - deducaoDoINSS

            if contribuicaoDoINSS > 1631.48:
                contribuicaoDoINSS = 1631.48

    elif tipoDeSegurado in seguradosSemAliquotaProgressiva:

        # As aliquotas são definidas por meio de três planos: baixa renda, plano simplificado e plano normal

        # Plano Normal: aliquota de 20% e permite a aposentadoria por tempo de contribuição
        # Plano Simplificado: aliquota de 11% e só dá direito a aposentadoria por idade
        # Baixa Renda: aliquota de 5% e só dá direito a aposentadoria por idade

        # Obs: todas as modalidades tem sua contribuição para o INSS calculada com base no salário mínimo, porém o plano normal pode ir do salário mínimo até o teto do INSS

        if modalidade == tiposDeModalidade[2]: # baixa renda
            salario = 1518.00
            aliquotaDoINSS = 0.05
            deducaoDoINSS = 0
            contribuicaoDoINSS = salario * aliquotaDoINSS

        elif modalidade == tiposDeModalidade[1]: # plano simplificado
            salario = 1518.00
            aliquotaDoINSS = 0.11
            deducaoDoINSS = 0
            contribuicaoDoINSS = salario * aliquotaDoINSS

        elif modalidade == tiposDeModalidade[0]: # plano normal
            if salario < 1518.00:
                salario = 1518.00
                aliquotaDoINSS = 0.20
                deducaoDoINSS = 0
                contribuicaoDoINSS = salario * aliquotaDoINSS

            else:
                aliquotaDoINSS = 0.20
                deducaoDoINSS = 0
                contribuicaoDoINSS = salario * aliquotaDoINSS

                if contribuicaoDoINSS > 1631.48:
                    contribuicaoDoINSS = 1631.48

        elif tipoDeSegurado == seguradosSemAliquotaProgressiva[2]: # segurado especial 

            if modalidade == tiposDeModalidade[3]: # contribuição obrigatória
                aliquotaDoINSS = 0.013
                deducaoDoINSS = 0
                contribuicaoDoINSS = salario * aliquotaDoINSS

                if contribuicaoDoINSS > 1631.48:
                        contribuicaoDoINSS = 1631.48

            elif modalidade == tiposDeModalidade[4]: # contribuição optativa
                aliquotaDoINSS = 0.20
                deducaoDoINSS = 0
                contribuicaoDoINSS = salario * aliquotaDoINSS

                if contribuicaoDoINSS > 1631.48:
                        contribuicaoDoINSS = 1631.48

    # O desconto legal é dado pela soma da contribuição do INSS, da pensão e da dedução total dos dependentes
    descontoTotal = contribuicaoDoINSS + pensao + deducaoTotalDosDependente

    # Verificamos o desconto simplificado e o desconto total na formulação da base de cálculo do imposto de renda e consideramos a mais vantajosa
    baseTotal = salario - descontoTotal
    baseSimplificada = salario - descontoSimplificado

    return salario, round(contribuicaoDoINSS, 2), round(aliquotaDoINSS, 2), deducaoDoINSS, baseSimplificada, baseTotal, descontoSimplificado, descontoTotal
