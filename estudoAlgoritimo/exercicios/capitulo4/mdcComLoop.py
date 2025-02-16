def mdc_iterativo(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(mdc_iterativo(48, 18))  # Saída: 6
