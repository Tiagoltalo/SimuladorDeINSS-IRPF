from flask import Flask, render_template, request
from utils.calculoINSS import calcularINSS
from utils.calculoIRPF import calcularIRPF
from utils.utilitarios import tornarTextoBruto

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SENHA'

@app.route('/')
def telaInicial():    
    return render_template("index.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")

# Resultado e Calculo do INSS ( Instituto Nacional de Seguro Social )
@app.route('/resultadoINSS', methods=["POST"])
def resultadoINSS():
    dados = {
            "salario": float(tornarTextoBruto(request.form["salario"])) / 100,
            "segurado": request.form["segurado"],
            "dependentes": int(request.form["dependentes"]),
            "pensao": float(tornarTextoBruto(request.form["pensao"])) / 100,
            "modalidade": (request.form["modalidade"] if "modalidade" in request.form else ""),
        }
    
    resultado = calcularINSS(dados)

    return render_template("resultadoINSS.html", resultado=resultado)

# Resultado e Calculo do IRPF ( Imposto de Renda Pessoa Física)
@app.route('/resultadoIRPF', methods=["POST"])
def resultadoIRPF():
    dados = {
        "salario": float(tornarTextoBruto(request.form["salario"])) / 100,
        "segurado": request.form["segurado"],
        "dependentes": int(request.form["dependentes"]),
        "pensao": float(tornarTextoBruto(request.form["pensao"])) / 100,
        "modalidade": (request.form["modalidade"] if "modalidade" in request.form else ""),
    }
    
    resultado = calcularIRPF(dados)
    
    return render_template("resultadoIRPF.html", resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)