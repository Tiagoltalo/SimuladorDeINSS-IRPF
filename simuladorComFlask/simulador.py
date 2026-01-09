from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SENHA'

@app.route('/')
def home():
    return render_template("simulador.html")

@app.route('/simuladorIr', methods=['POST'])
def informacoesIr():
    salario = float(request.form["salario"]) # salário total
    tipoSegurado = request.form["tipoSegurado"] # tipo de segurado
    dependentes = int(request.form["dependentes"]) # quantidade de dependentes
    pensao = float(request.form["pensao"]) # quantidade de pensão paga pela pessoa
    modalidade = request.form["modalidade"] # modalidade do segurado, se não for do tipo de segurado progressivo
    
    # Verificação do tipo de segurador
    # Os segurados empregado, empregado doméstico e trabalhador avulso sofrem um aumento de aliquota progressiva de acordo com o salário
    # Os segurados contribuinte individual, segurado facultativo, mei e segurado especial tem suas aliquotas definidas de acordo com o seu plano/modalidade

    if tipoSegurado in ["empregado", "empregado doméstico", "trabalhador avulso"]:

        # (Empregado, Empregado Doméstico e Trabalhador Avulso)
        # Salário de Contribuição (R$) 	Alíquota progressiva para fins de recolhimento ao INSS
        # Até 1.518,00			7,5%
        # De 1.518,01 a 2.793,88		9%
        # De 2.793,89 até 4.190,83	12%
        # De 4.190,84 até 8.157,41	14%

        # Obs: aliquotas atuais - data: 09/10/2025

        # A contribuição do INSS será usada para abater o valor do salário bruto e dar a base de cálculo para o Imposto de Renda

        # Como o cálculo ocorre? O calculo da contribuição é dada pela multiplicação do sálario pela aliquota, menos uma dedução fixa
       
        if salario <= 1518:
            aliquotaINSS = 0.075
            contribuicaoINSS = salario * aliquotaINSS

        elif salario > 1518 and salario <= 2793.88:
            deducaoINSS = 22.77
            aliquotaINSS = 0.09
            contribuicaoINSS = salario * aliquotaINSS - deducaoINSS

        elif salario > 2793.88 and salario <= 4190.83:
            deducaoINSS = 106.59
            aliquotaINSS = 0.12
            contribuicaoINSS = salario * aliquotaINSS - deducaoINSS

        elif salario > 4190.83:
            deducaoINSS = 190.40
            aliquotaINSS = 0.14
            contribuicaoINSS = salario * aliquotaINSS - deducaoINSS

            if contribuicaoINSS > 1631.48:
                contribuicaoINSS = 1631.48

    elif tipoSegurado in ["contribuinte individual", "segurado facultativo", "mei"]:

        # As aliquotas são definidas por meio de três planos: baixa renda, plano simplificado e plano normal
        # Baixa Renda: aliquota de 5% e só dá direito a aposentadoria por idade
        # Plano Simplificado: aliquota de 11% e só dá direito a aposentadoria por idade
        # Plano Normal: aliquota de 20% e permite a aposentadoria por tempo de contribuição
        # Obs: todas as modalidades tem sua contribuição para o INSS calculada com base no salário mínimo, porém a plano normal pode ir do salário mínimo até o teto do INSS

        if modalidade == "baixa renda":
            salario = 1518.00
            aliquotaINSS = 0.05
            contribuicaoINSS = salario * aliquotaINSS

        elif modalidade == "plano simplificado":
            salario = 1518.00
            aliquotaINSS = 0.11
            contribuicaoINSS = salario * aliquotaINSS

        elif modalidade == "plano normal":
            if salario < 1518.00:
                salario = 1518.00
                aliquotaINSS = 0.20
                contribuicaoINSS = salario * aliquotaINSS

            else:
                aliquotaINSS = 0.20
                contribuicaoINSS = salario * aliquotaINSS

                if contribuicaoINSS > 1631.48:
                    contribuicaoINSS = 1631.48

    elif tipoSegurado == "segurado especial":
        if modalidade == "contribuição obrigatória":
            aliquotaINSS = 0.013
            contribuicaoINSS = salario * aliquotaINSS

            if contribuicaoINSS > 1631.48:
                    contribuicaoINSS = 1631.48

        elif modalidade == "contribuição optativa":
            aliquotaINSS = 0.20
            contribuicaoINSS = salario * aliquotaINSS

            if contribuicaoINSS > 1631.48:
                    contribuicaoINSS = 1631.48

    print(contribuicaoINSS)
    # Definimos a dedução por cada dependente que a pessoa física possui
    # Definimos o desconto simplificado

    deducaoDependente = 189.59
    descontoSimplificado = 607.20
    deducaoTotalDependente = deducaoDependente * dependentes

    # Desconto legal é dado pela soma da contribuição do INSS, da pensão e da dedução total dos dependentes
    # Verificamos o desconto simplificado e o desconto total na formulação da base de cálculo do imposto de renda e consideramos a mais vantajosa

    descontoTotal = contribuicaoINSS + pensao + deducaoTotalDependente

    basePrimeiro = salario - descontoTotal
    baseSegundo = salario - descontoSimplificado
    
    # Nós utlizamos a função round para mostrar somente duas casas decimais e evitar dizimas periódicas

    if basePrimeiro < baseSegundo:
        baseCalculo = round(basePrimeiro, 2)
        descontoSimplificado = 0
    elif baseSegundo < basePrimeiro:
        baseCalculo = round(baseSegundo, 2)
        contribuicaoINSS = 0

    # Baseado na base de cálculo faremos o cálculo do imposto de renda que evolui de forma progressiva

    if baseCalculo >= 2259.21 and baseCalculo <= 2826.65:
        aliquotaIR = 0.075
        deducao = 182.16
        impostoRenda = baseCalculo * aliquotaIR - deducao

    elif baseCalculo >= 2826.66 and baseCalculo <= 3751.05:
        aliquotaIR = 0.15
        deducao = 394.16
        impostoRenda = baseCalculo * aliquotaIR - deducao

    elif baseCalculo >= 3751.06 and baseCalculo <= 4664.68:
        aliquotaIR = 0.225
        deducao = 675.49
        impostoRenda = baseCalculo * aliquotaIR - deducao

    elif baseCalculo > 4664.68:
        aliquotaIR = 0.275
        deducao = 908.73
        impostoRenda = baseCalculo * aliquotaIR - deducao
    else:
        aliquotaIR = 0
        deducao = 0
        impostoRenda = 0


    return render_template("resultado.html", salario=salario, tipoSegurado=tipoSegurado, dependentes=dependentes, impostoRenda=round(float(impostoRenda), 2), deducao=deducao, baseCalculo=baseCalculo, contribuicaoINSS=contribuicaoINSS, \
                           deducaoDependente=deducaoDependente, aliquotaIR=round(float(aliquotaIR * 100), 2), aliquotaINSS=round(float(aliquotaINSS * 100), 2), modalidade=modalidade, pensao=pensao, descontoSimplificado=descontoSimplificado, deducaoTotalDependente=deducaoTotalDependente)

@app.route("/resultado.html")
def retorna():
    return redirect(url_for('simulador.html'))

if __name__ == '__main__':
    app.run(debug=True)