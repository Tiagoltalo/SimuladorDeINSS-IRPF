from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SENHA'

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/formulario', methods=['POST', 'GET'])
def formulario():
    if request.method == 'POST':
        data = {
            "salario": float(request.form["salario"]),
            "segurado": request.form["segurado"],
            "dependentes": int(request.form["dependentes"]),
            "pensao": float(request.form["pensao"]),
            "modalidade": request.form["modalidade"]
        }

    return render_template("formulario.html")

@app.route('/resultado')
def resultado():
    data = session.get('resultado')

    if not data:
        return redirect(url_for('formulario'))

    return render_template("resultado.html")

if __name__ == '__main__':
    app.run(debug=True)