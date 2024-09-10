def seqFibo(limit):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def isFiboNum(n):
    fib_sequence = seqFibo(n)
    if n in fib_sequence:
        return f"O número {n} pertence."
    else:
        return f"O número {n} NÃO pertence."

numero = int(input("Informe um número: "))
resultado = isFiboNum(numero)
print(resultado)
