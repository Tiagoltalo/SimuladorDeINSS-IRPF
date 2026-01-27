from decimal import Decimal

def formatarMoeda(valor):
    valor = Decimal(valor)
    
    valorFormatado = f"{valor:,.2f}".replace(".", "X").replace(",", ".").replace("X", ",")
    
    return valorFormatado