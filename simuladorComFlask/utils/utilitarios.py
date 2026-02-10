from re import sub

def formatarParaMoeda(valor):
    valorFormatado = f"{valor:,.2f}".replace(".", "X").replace(",", ".").replace("X", ",")
    
    return valorFormatado

def tornarTextoBruto(valor):
    valor = sub(r"\D", "", valor)
    
    return valor