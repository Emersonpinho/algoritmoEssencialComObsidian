def pesquisa_binaria(lista, item):
    baixo = 0 
    alto = len(lista) - 1
    
    while baixo <= alto:
        meio = (baixo + alto) // 2  # Use divisão inteira
        chute = lista[int(meio)]  # Converta meio para inteiro

        if chute == item:
            return meio
        elif chute < item:
            baixo = meio + 1
        else:
            alto = meio - 1

    return None  # Retorne None se o item não for encontrado

minha_lista = [1, 3, 5, 7, 9]
print (pesquisa_binaria(minha_lista, 3)) # => 1
print (pesquisa_binaria(minha_lista, -1)) # => None