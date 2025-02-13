def sauda(nome):
    print("olá " + nome + "!")
    sauda2(nome)
    print("preparando para dizer tchau...")
    tchau()

def sauda2(nome):
    print(f"como vai {nome}?")

def tchau():
    print("ok, tchau!")

sauda("Emerson")