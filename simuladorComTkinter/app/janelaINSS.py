from tkinter import *
from tkinter import ttk
from src.arquivoAuxiliar import tiposDeSegurado, verificarModalidades, criadorDeFrames, hoverLigado, hoverDesligado, verificarSeCamposForamPreenchidos
from src.funcaoINSS import calcularINSS

# Tela que recebe as informações necessárias para o cálculo
def inputINSS(janela, telaInicial):
    # Definição das variáveis e seus tipos
    salario = DoubleVar()
    segurado = StringVar()
    pensao = DoubleVar()
    dependentes = IntVar()
    modalidade = StringVar()

    for widget in janela.winfo_children():
        widget.destroy()

    framePrincipal = Frame(janela, background="#202020")
    framePrincipal.pack(fill="both", expand=True)

    frame = criadorDeFrames(framePrincipal, 8)

    # Título
    Label(frame[0], text="Simulador de INSS", font=("Segoe UI", 16, "bold"), bg="#202020", fg="#FFFFFF",).grid(column=1, row=0, pady=10)

    # Salário
    Label(frame[1], text="Salário: ", anchor="w", width=30, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 10, "bold")).grid(column=0, row=0)
    Entry(frame[1], textvariable=salario, width=40).grid(column=0, row=1)

    # Tipo de Segurado
    Label(frame[2], text="Segurado: ", anchor="w", width=30, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 10, "bold")).grid(column=0, row=0)
    comboSegurado = ttk.Combobox(frame[2], textvariable=segurado, values=tiposDeSegurado, width=37, state="readonly")
    comboSegurado.grid(column=0, row=1)

    # Pensão Alimentícia
    Label(frame[3], text="Pensão: ", anchor="w", width=30, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 10, "bold")).grid(column=0, row=0)
    Entry(frame[3], textvariable=pensao, width=40).grid(column=0, row=1)

    # Dependentes
    Label(frame[4], text="Dependentes: ", anchor="w", width=30, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 10, "bold")).grid(column=0, row=0)
    Entry(frame[4], textvariable=dependentes, width=40).grid(column=0, row=1)

    # Modalidade
    Label(frame[5], text="Modalidade: ", anchor="w", width=35, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 9, "bold")).grid(column=0, row=0)
    ttk.Combobox(frame[5], textvariable=modalidade, values="", width=37).grid(column=0, row=1)
    comboSegurado.bind("<<ComboboxSelected>>", lambda event: verificarModalidades(frame[5], segurado, modalidade))

    # Botão de voltar e de calcular
    botaoINSS = Button(frame[7], text="Calcular INSS", height=1, width=12, bg="#3B3B3B", fg="#FFFFFF", activebackground="#323232", relief="flat", font=("Segoe UI", 9, "bold"), command=lambda: resultadoINSS(janela, telaInicial, salario, segurado, pensao, dependentes, modalidade))
    botaoVoltar = Button(frame[7], text="Voltar", height=1, width=12, bg="#3B3B3B", fg="#FFFFFF", activebackground="#323232", relief="flat", font=("Segoe UI", 9, "bold"), command=lambda: telaInicial())
    botaoINSS.grid(column=1, row=0, padx=5)
    botaoVoltar.grid(column=2, row=0, padx=5)

    # Evento que emite uma mensagem de erro, caso os campos necessários não estejam preenchidos
    botaoINSS.bind("<Button-1>", lambda event: verificarSeCamposForamPreenchidos(frame[6], salario, segurado, modalidade))

    # Hover do botão
    botaoINSS.bind("<Enter>", lambda event: hoverLigado(botaoINSS))
    botaoINSS.bind("<Leave>", lambda event: hoverDesligado(botaoINSS))

    botaoVoltar.bind("<Enter>", lambda event: hoverLigado(botaoVoltar))
    botaoVoltar.bind("<Leave>", lambda event: hoverDesligado(botaoVoltar))

# Tela que mostra os resultados do cálculo
def resultadoINSS(janela, telaInicial, salario, segurado, pensao, dependentes, modalidade):
    # Pega o valor de todas as variáveis
    salario = salario.get()
    segurado = segurado.get()
    pensao = pensao.get()
    dependentes  = dependentes.get()
    modalidade = modalidade.get()

    salario, contribuicaoDoINSS, aliquotaDoINSS, deducaoDoINSS, *_ = calcularINSS(salario, segurado, pensao, dependentes, modalidade)


    for widget in janela.winfo_children():
        widget.destroy()

    framePrincipal = Frame(janela, background="#202020")
    framePrincipal.pack(fill="both", expand=True)

    frame = criadorDeFrames(framePrincipal, 3)

    # Título
    Label(frame[0], text="Resultado do Cálculo do INSS", font=("Segoe UI", 16, "bold"), bg="#202020", fg="#FFFFFF").grid(column=1, row=0)

    # Salário
    Label(frame[1], text="Salário: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#3B3B3B", fg="#FFFFFF").grid(column=0, row=0)
    Label(frame[1], text=f"R$ {salario}", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#3B3B3B", fg="#FFFFFF").grid(column=1, row=0)

    # Tipo de Segurado
    Label(frame[1], text="Segurado: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#3B3B3B", fg="#FFFFFF").grid(column=0, row=1)
    Label(frame[1], text=f"{segurado}", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#3B3B3B", fg="#FFFFFF").grid(column=1, row=1)

    # Alíquota do INSS
    Label(frame[1], text="Alíquota: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#3B3B3B", fg="#FFFFFF").grid(column=0, row=2)
    Label(frame[1], text=f"{aliquotaDoINSS}%", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#3B3B3B", fg="#FFFFFF").grid(column=1, row=2)

    # Dedução do INSS
    Label(frame[1], text="Dedução: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#3B3B3B", fg="#FFFFFF").grid(column=0, row=3)
    Label(frame[1], text=f"R$ {deducaoDoINSS}", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#3B3B3B", fg="#FFFFFF").grid(column=1, row=3)

    # Contribuição do INSS
    Label(frame[1], text="Contribuição: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#3B3B3B", fg="#FFFFFF").grid(column=0, row=4)
    Label(frame[1], text=f"R$ {contribuicaoDoINSS}", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#3B3B3B", fg="#FFFFFF").grid(column=1, row=4)

    # Botão de voltar para a tela inicial
    botaoVoltar = Button(frame[2], text="Voltar", height=1, width=15, bg="#3B3B3B", fg="#FFFFFF", activebackground="#323232", relief="flat", font=("Segoe UI", 9, "bold"), command=lambda: telaInicial())
    botaoVoltar.grid(column=1, row=0, padx=52)
    
    # Hover do botão
    botaoVoltar.bind("<Enter>", lambda event: hoverLigado(botaoVoltar))
    botaoVoltar.bind("<Leave>", lambda event: hoverDesligado(botaoVoltar))