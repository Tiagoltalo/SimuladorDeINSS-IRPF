from simuladorComTkinter.app.src.utilitarios import seguradosComAliquotaProgressiva, seguradosSemAliquotaProgressiva, tiposDeModalidade

def calcularINSS(salario=0.0, tipoDeSegurado="", pensao=0.0, dependentes=0, modalidade=""):
    deducaoPorDependente = 189.59
    descontoSimplificado = 607.20

    deducaoTotalDosDependente = deducaoPorDependente * dependentes
    
    if tipoDeSegurado in seguradosComAliquotaProgressiva:

        # (Empregado, Empregado Doméstico e Trabalhador Avulso)
        # Salário de Contribuição (R$) | Alíquota | Dedução
        # Até 1.621,00			       | 7,5%     | 
        # De 1.621,01 a 2.902,84	   | 9%       | 22,77
        # De 2.902,85 até 4.354,28	   | 12%      | 106,59
        # De 4.354,29 até 8.475,55	   | 14%      | 190,40
       
        if salario <= 1621:
            aliquotaDoINSS = 0.075
            contribuicaoDoINSS = salario * aliquotaDoINSS

        elif salario > 1621 and salario <= 2902.84:
            deducaoDoINSS = 22.77
            aliquotaDoINSS = 0.09
            contribuicaoDoINSS = salario * aliquotaDoINSS - deducaoDoINSS

        elif salario > 2902.85 and salario <= 4354.27:
            deducaoDoINSS = 106.59
            aliquotaDoINSS = 0.12
            contribuicaoDoINSS = salario * aliquotaDoINSS - deducaoDoINSS

        elif salario > 4354.28:
            deducaoDoINSS = 190.40
            aliquotaDoINSS = 0.14
            contribuicaoDoINSS = salario * aliquotaDoINSS - deducaoDoINSS

            if contribuicaoDoINSS > 996.17:
                contribuicaoDoINSS = 996.17

    elif tipoDeSegurado in seguradosSemAliquotaProgressiva:

        # As aliquotas são definidas por meio de três planos: baixa renda, plano simplificado e plano normal

        # Plano Normal: aliquota de 20% e permite a aposentadoria por tempo de contribuição
        # Plano Simplificado: aliquota de 11% e só dá direito a aposentadoria por idade
        # Baixa Renda: aliquota de 5% e só dá direito a aposentadoria por idade

        # Obs: todas as modalidades tem sua contribuição para o INSS calculada com base no salário mínimo, porém o plano normal pode ir do salário mínimo até o teto do INSS

        if modalidade == tiposDeModalidade[2]: # baixa renda
            salario = 1621.00
            aliquotaDoINSS = 0.05
            deducaoDoINSS = 0
            contribuicaoDoINSS = salario * aliquotaDoINSS

        elif modalidade == tiposDeModalidade[1]: # plano simplificado
            salario = 1621.00
            aliquotaDoINSS = 0.11
            deducaoDoINSS = 0
            contribuicaoDoINSS = salario * aliquotaDoINSS

        elif modalidade == tiposDeModalidade[0]: # plano normal
            if salario < 1621.00:
                salario = 1621.00
                aliquotaDoINSS = 0.20
                deducaoDoINSS = 0
                contribuicaoDoINSS = salario * aliquotaDoINSS

            else:
                aliquotaDoINSS = 0.20
                deducaoDoINSS = 0
                contribuicaoDoINSS = salario * aliquotaDoINSS

                if contribuicaoDoINSS > 1695.11:
                    contribuicaoDoINSS = 1695.11

        elif tipoDeSegurado == seguradosSemAliquotaProgressiva[2]: # segurado especial 

            if modalidade == tiposDeModalidade[3]: # contribuição obrigatória
                aliquotaDoINSS = 0.013
                deducaoDoINSS = 0
                contribuicaoDoINSS = salario * aliquotaDoINSS

                if contribuicaoDoINSS > 1695.11:
                        contribuicaoDoINSS = 1695.11

            elif modalidade == tiposDeModalidade[4]: # contribuição optativa
                aliquotaDoINSS = 0.20
                deducaoDoINSS = 0
                contribuicaoDoINSS = salario * aliquotaDoINSS

                if contribuicaoDoINSS > 1695.11:
                        contribuicaoDoINSS = 1695.11

    # O desconto legal é dado pela soma da contribuição do INSS, da pensão e da dedução total dos dependentes
    descontoTotal = contribuicaoDoINSS + pensao + deducaoTotalDosDependente

    return salario, round(contribuicaoDoINSS, 2), round((aliquotaDoINSS * 100), 2), deducaoDoINSS, descontoSimplificado, descontoTotal
