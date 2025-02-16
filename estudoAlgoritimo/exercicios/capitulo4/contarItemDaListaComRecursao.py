def contar_lista(lista):
    if lista == []:
        return 0
    return 1 + contar_lista(lista[1: ])

print(contar_lista([1, 2]))