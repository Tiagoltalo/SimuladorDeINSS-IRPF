from tkinter import *
from tkinter import ttk
from simuladorComTkinter.app.src.utilitarios import tiposDeSegurado, verificarModalidades, criadorDeFrames, hoverLigado, hoverDesligado, verificarSeCamposForamPreenchidos
from src.funcaoIRPF import calcularIRPF

# Tela que recebe as informações necessárias para o cálculo
def inputIRPF(janela, telaInicial):
    # Definição das variáveis e seus tipos
    salario = DoubleVar()
    segurado = StringVar()
    pensao = DoubleVar()
    dependentes = DoubleVar()
    modalidade = StringVar()

    for widget in janela.winfo_children():
        widget.destroy()

    framePrincipal = Frame(janela, background="#202020")
    framePrincipal.pack(fill="both", expand=True)

    frame = criadorDeFrames(framePrincipal, 8)

    # Título
    Label(frame[0], text="Simulador de IRPF", bg="#202020", fg="#FFFFFF", font=("Segoe UI", 16, "bold")).grid(column=1, row=0, pady=10)

    # Salário
    Label(frame[1], text="Salário: ", anchor="w", width=30, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 10, "bold")).grid(column=0, row=0)
    Entry(frame[1], textvariable=salario, width=40).grid(column=0, row=1)

    # Tipo de Segurado
    Label(frame[2], text="Tipo de Segurado: ", anchor="w", width=30, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 10, "bold")).grid(column=0, row=0)
    comboSegurado = ttk.Combobox(frame[2], textvariable=segurado, values=tiposDeSegurado, width=37, state="readonly")
    comboSegurado.grid(column=0, row=1)

    # Pensão Alimentícia
    Label(frame[3], text="Pensão: ", anchor="w", width=30, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 10, "bold")).grid(column=0, row=0)
    Entry(frame[3], textvariable=pensao, width=40).grid(column=0, row=1)

    # Dependente
    Label(frame[4], text="Dependentes: ", anchor="w", width=30, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 10, "bold")).grid(column=0, row=0)
    Entry(frame[4], textvariable=dependentes, width=40).grid(column=0, row=1)

    # Modalidades
    Label(frame[5], text="Modalidade: ", anchor="w", width=35, bg="#202020", fg="#FFFFFF", font=("Segoe UI", 9, "bold")).grid(column=0, row=0)
    ttk.Combobox(frame[5], textvariable=modalidade, values="", width=37).grid(column=0, row=1)
    comboSegurado.bind("<<ComboboxSelected>>", lambda event: verificarModalidades(frame[5], segurado, modalidade))

    # Botão de voltar e de calcular
    botaoIRPF = Button(frame[7], text="Calcular IRPF", height=1, width=12, bg="#3B3B3B", fg="#FFFFFF", activebackground="#323232", relief="flat", font=("Segoe UI", 9, "bold"), command=lambda: resultadoIRPF(janela, telaInicial, salario, segurado, pensao, dependentes, modalidade))
    botaoVoltar = Button(frame[7], text="Voltar", height=1, width=12, bg="#3B3B3B", fg="#FFFFFF", activebackground="#323232", relief="flat", font=("Segoe UI", 9, "bold"), command=lambda: telaInicial())
    botaoIRPF.grid(column=1, row=0, padx=5)
    botaoVoltar.grid(column=2, row=0, padx=5)

    # Evento que emite uma mensagem de erro, caso os campos necessários não estejam preenchidos
    botaoIRPF.bind("<Button-1>", lambda event: verificarSeCamposForamPreenchidos(frame[6], salario, segurado, modalidade))

    # Hover do botão
    botaoIRPF.bind("<Enter>", lambda event: hoverLigado(botaoIRPF))
    botaoIRPF.bind("<Leave>", lambda event: hoverDesligado(botaoIRPF))

    botaoVoltar.bind("<Enter>", lambda event: hoverLigado(botaoVoltar))
    botaoVoltar.bind("<Leave>", lambda event: hoverDesligado(botaoVoltar))

# Tela que mostra os resultados do cálculo
def resultadoIRPF(janela, telaInicial, salario, segurado, pensao, dependentes, modalidade):
    # Pega o valor de todas as variáveis
    salario = salario.get()
    segurado = segurado.get()
    pensao = pensao.get()
    dependentes = dependentes.get()
    modalidade = modalidade.get()

    impostoDeRenda, aliquotaDoIRPF, deducaoDoIRPF, baseDeCalculo, desconto, reducao = calcularIRPF(salario, segurado, pensao, dependentes, modalidade)

    for widget in janela.winfo_children():
        widget.destroy()

    framePrincipal = Frame(janela, background="#202020")
    framePrincipal.pack(expand=True)

    frame = criadorDeFrames(framePrincipal, 3)

    # Título
    Label(frame[0], text="Resultado do Cálculo do IRPF", bg="#202020", fg="#FFFFFF", font=("Segoe UI", 16, "bold")).grid(column=1, row=0, pady=30)

    # Base de Cálculo
    Label(frame[1], text="Base de Cálculo: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=0, row=0)
    Label(frame[1], text=f"R$ {baseDeCalculo}", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=1, row=0)

    # Alíquota do IRPF
    Label(frame[1], text="Alíquota: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=0, row=1)
    Label(frame[1], text=f"{aliquotaDoIRPF * 100}%", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=1, row=1)

    # Dedução do IRPF
    Label(frame[1], text="Dedução: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=0, row=2)
    Label(frame[1], text=f"R$ {deducaoDoIRPF}", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=1, row=2)

    # Segurado
    Label(frame[1], text="Segurado: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=0, row=3)
    Label(frame[1], text=f"{segurado}", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=1, row=3)

    # Pensão Alimentícia
    Label(frame[1], text="Pensão: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=0, row=4)
    Label(frame[1], text=f"R$ {pensao}", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=1, row=4)

    # Quantidade de Dependentes
    Label(frame[1], text="Dependentes: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=0, row=5)
    Label(frame[1], text=f"{dependentes}", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=1, row=5)

    # Desconto
    Label(frame[1], text="Desconto: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=0, row=6)
    Label(frame[1], text=f"R$ {desconto}", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=1, row=6)

    # Redução
    Label(frame[1], text="Redução: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=0, row=7)
    Label(frame[1], text=f"R$ {reducao}", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=1, row=7)

    # Imposto de Renda
    Label(frame[1], text="Imposto de Renda: ", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=0, row=8)
    Label(frame[1], text=f"R$ {impostoDeRenda}", width=18, bd=1, relief="solid", anchor="w", font=("Segoe UI", 10, "bold"), pady=8, padx=3, bg="#202020", fg="#FFFFFF").grid(column=1, row=8)

    # Botão de voltar para a tela inicial
    botaoVoltar = Button(frame[2], text="Voltar", height=1, width=15, bg="#3B3B3B", fg="#FFFFFF", activebackground="#323232", relief="flat", font=("Segoe UI", 9, "bold"), command=lambda: telaInicial())
    botaoVoltar.grid(column=1, row=0, padx=5, pady=30)
    
    # Hover do botão
    botaoVoltar.bind("<Enter>", lambda event: hoverLigado(botaoVoltar))
    botaoVoltar.bind("<Leave>", lambda event: hoverDesligado(botaoVoltar))