from tkinter import *
from .janelaINSS import inputINSS
from .janelaIRPF import inputIRPF
from src.arquivoAuxiliar import criadorDeFrames, hoverLigado, hoverDesligado

def telaInicial():
    for widget in janela.winfo_children():
        widget.destroy()

    framePrincipal = Frame(janela, background="#202020", pady=30)
    framePrincipal.pack(fill="both", expand=True)

    frame = criadorDeFrames(framePrincipal, 3)

    # Título
    Label(frame[0],text="Simulador de IRPF e INSS", bg="#202020", fg="#FFFFFF", font=("Segoe UI", 16, "bold")).grid(column=0, row=1)

    # Botão de IRPF, INSS e de sair
    botaoIRPF = Button(frame[1], text="IRPF", width=35, height=2, bg="#3B3B3B", fg="#FFFFFF", activebackground="#323232", relief="flat", font=("Segoe UI", 9, "bold"), command=lambda: inputIRPF(janela, telaInicial))
    botaoINSS = Button(frame[1], text="INSS", width=35, height=2, bg="#3B3B3B", fg="#FFFFFF", activebackground="#323232", relief="flat", font=("Segoe UI", 9, "bold"), command=lambda: inputINSS(janela, telaInicial))
    botaoSair = Button(frame[1], text="Sair", width=35, height=2, bg="#3B3B3B", fg="#FFFFFF", activebackground="#323232", relief="flat", font=("Segoe UI", 9, "bold"), command=janela.destroy)

    # Eventos que dão o aspecto de hover nos botões
    botaoINSS.grid(column=0, row=0, pady=15)
    botaoINSS.bind("<Enter>", lambda event: hoverLigado(botaoINSS))
    botaoINSS.bind("<Leave>", lambda event: hoverDesligado(botaoINSS))

    botaoIRPF.grid(column=0, row=1, pady=15)
    botaoIRPF.bind("<Enter>", lambda event: hoverLigado(botaoIRPF))
    botaoIRPF.bind("<Leave>", lambda event: hoverDesligado(botaoIRPF))

    botaoSair.grid(column=0, row=2, pady=15)
    botaoSair.bind("<Enter>", lambda event: hoverLigado(botaoSair))
    botaoSair.bind("<Leave>", lambda event: hoverDesligado(botaoSair))

    janela.mainloop()

# Criação e configuração da janela
janela = Tk()
janela.title("Simulador de IRPF e INSS")
janela.geometry("400x500")
janela.configure(background="#202020")
# janela.iconbitmap(procurarArquivo("logoOffice.ico"))

telaInicial()