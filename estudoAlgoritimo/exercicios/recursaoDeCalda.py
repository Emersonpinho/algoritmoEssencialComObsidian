def fat_tail_recursive(x, accumulator=1):
    if x == 1:
        return accumulator
    else:
        return fat_tail_recursive(x - 1, x * accumulator)

print(fat_tail_recursive(5))


# ISSO NÃO FUNCIONA NO PYTHON3, MESMO QUE RODE SEM ERROS O PYTHON ARMAZENA OS VALORES