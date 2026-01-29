from flask import Flask, render_template, request
from re import sub
from utils.calculoINSS import calcularINSS
from utils.calculoIRPF import calcularIRPF

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
            "salario": float(sub(r"\D", "", request.form["salario"])) / 100,
            "segurado": request.form["segurado"],
            "dependentes": int(request.form["dependentes"]),
            "pensao": float(sub(r"\D", "", request.form["pensao"])) / 100,
            "modalidade": (request.form["modalidade"] if "modalidede" in request.form else ""),
        }
    
    resultado = calcularINSS(dados)

    return render_template("resultadoINSS.html", resultado=resultado)

# Resultado e Calculo do IRPF ( Imposto de Renda Pessoa Física)
@app.route('/resultadoIRPF', methods=["POST"])
def resultadoIRPF():
    dados = {
        "salario": float(sub(r"\D", "", request.form["salario"])) / 100,
        "segurado": request.form["segurado"],
        "dependentes": int(request.form["dependentes"]),
        "pensao": float(sub(r"\D", "", request.form["pensao"])) / 100,
        "modalidade": (request.form["modalidade"] if "modalidade" in request.form else ""),
    }
    
    resultado = calcularIRPF(dados)
    
    return render_template("resultadoIRPF.html", resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)