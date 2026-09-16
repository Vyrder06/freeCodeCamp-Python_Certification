def number_pattern(n):
    if not(isinstance(n, int)) or isinstance(n,  bool):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."
    resultado = []
    for number_index in range(1, n +1):
        resultado.append(str(number_index))
    return " ".join(resultado)

print(number_pattern(4))