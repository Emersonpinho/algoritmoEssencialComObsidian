def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

print(mdc(48, 18))  # Saída: 6
