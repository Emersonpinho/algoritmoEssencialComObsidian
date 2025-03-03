from collections import deque

fila_de_pesquisa = deque()
fila_de_pesquisa += grafo["Você"]

while fila_de_pesquisa:
    pessoa = fila_de_pesquisa.poplefh()
    if pessoa_e_vendedor(pessoa):
        print(f"{pessoa} é um vendedor de manga")
        return True 
    else:
        fila_de_pesquisa += grafo[pessoa]
        return False