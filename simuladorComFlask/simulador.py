from flask import Flask, render_template, redirect, url_for, request
from utils.calculoINSS import calcularINSS
from utils.calculoIRPF import calcularIRPF

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SENHA'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")

@app.route('/resultado', methods=["POST"])
def resultado():
    data = {
            "salario": float(request.form["salario"]),
            "segurado": request.form["segurado"],
            "dependentes": int(request.form["dependentes"]),
            "pensao": float(request.form["pensao"]),
            "modalidade": request.form["modalidades"]
        }
    


    return render_template("resultado.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)