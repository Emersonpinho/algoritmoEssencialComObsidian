def minha_lista(lista):
    for item in lista:
        print(item)


from time import sleep

def imprime_item2(lista):
    for item in lista:
        sleep(2)
        print(item)

imprime_item2([1, "Emerson", "lindão", False, 3])