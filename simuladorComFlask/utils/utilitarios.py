def formatarMoeda(valor):
    valorFormatado = f"{valor:,.2f}".replace(".", "X").replace(",", ".").replace("X", ",")
    
    return valorFormatado