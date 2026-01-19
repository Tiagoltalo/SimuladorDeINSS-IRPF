from tkinter import *
from tkinter import ttk

""" --- Variáveis --- """

# Segurados e Modalidades para o cálculo
seguradosComAliquotaProgressiva = [
    "empregado",
    "empregado doméstico",
    "trabalhador avulso"
]

seguradosSemAliquotaProgressiva = [
    "contribuinte individual",
    "segurado facultativo",
    "segurado especial",
]

tiposDeModalidade = [
    "plano normal",
    "plano simplificado",
    "baixa renda",
    "contribuição obrigatória",
    "contribuição optativa"
]

# Segurados e Modalidades para o Select
tiposDeSegurado = [
    "empregado",
    "empregado doméstico",
    "trabalhador avulso",
    "contribuinte individual",
    "segurado facultativo",
    "segurado especial",
]

modalidades = {
    "contribuinte individual" : ["baixa renda", "plano simplificado", "plano normal"],
    "segurado facultativo" : ["baixa renda", "plano simplificado", "plano normal"],
    "segurado especial" : ["contribuição obrigatória", "contribuição optativa"]
}

"""  --- Funções --- """

# Função que cria frames padronizados
def criadorDeFrames(framePrincipal, quantidade):
    listaDeFrames = []


    for i in range(quantidade):
        frame = Frame(framePrincipal, background="#202020")
        frame.pack(expand=True) 

        listaDeFrames.append(frame)

    return listaDeFrames

# Função que verifica as modalidades disponíveis pelo tipo de segurado
def verificarModalidades(frame, segurado, modalidade):
    segurado = segurado.get()

    for widget in frame.winfo_children():
        widget.destroy()

    if segurado == "contribuinte individual":
        labelModalidades = Label(frame, text="Modalidade: ", anchor="w", width=35, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 9, "bold")).grid(column=0, row=0)
        selectModalidades = ttk.Combobox(frame, textvariable=modalidade, values=modalidades["contribuinte individual"], width=37).grid(column=0, row=1)

    elif segurado == "segurado facultativo":
        labelModalidades = Label(frame, text="Modalidade: ", anchor="w", width=35, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 9, "bold")).grid(column=0, row=0)
        selectModalidades = ttk.Combobox(frame, textvariable=modalidade, values=modalidades["segurado facultativo"], width=37).grid(column=0, row=1)

    elif segurado == "segurado especial":
        labelModalidades = Label(frame, text="Modalidade: ", anchor="w", width=35, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 9, "bold")).grid(column=0, row=0)
        selectModalidades = ttk.Combobox(frame, textvariable=modalidade, values=modalidades["segurado especial"], width=37).grid(column=0, row=1)

    else:
        labelModalidades = Label(frame, text="Modalidade: ", anchor="w", width=35, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 9, "bold")).grid(column=0, row=0)
        selectModalidades = ttk.Combobox(frame, textvariable=modalidade, values="", width=37).grid(column=0, row=1)

    return {
        labelModalidades,
        selectModalidades
    }

# Função que verifica se todos os campos necessários foram preenchidos, se não será emitido uma mensagem
def verificarSeCamposForamPreenchidos(frame, salario, segurado, modalidade):
    if (segurado.get() not in tiposDeSegurado or salario.get() == 0.0):
        return Label(frame, text="Preencha todos os campos necessários!!!", fg="#FF0000", anchor="w", width=30, bg="#202020", name="labelAlert", font=("Segoe UI", 10, "bold")).grid(column=0, row=2)
    elif (segurado.get() in seguradosSemAliquotaProgressiva and modalidade.get() not in tiposDeModalidade):
        return Label(frame, text="Preencha todos os campos necessários!!!", fg="#FF0000", anchor="w", width=30, bg="#202020", name="labelAlert", font=("Segoe UI", 10, "bold")).grid(column=0, row=2)
    else:
        for widget in frame.winfo_children():
            if widget.winfo_name() == "labelAlert":
                widget.destroy()

# Funções do hover do botão
def hoverLigado(botao):
    botao.config(bg="#323232")

def hoverDesligado(botao):
    botao.config(bg="#3B3B3B")