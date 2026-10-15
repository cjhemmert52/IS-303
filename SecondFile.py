def is_odd(numero):
    odd = True
    if numero % 2 == 0:
        odd = False
    elif numero % 2 != 0:
        odd = True
    return odd