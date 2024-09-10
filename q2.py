def hasA(s):
    if "a" not in s.lower():
        return f"Não há 'a' em '{s}'."

    return f"A letra 'a' aparece {s.lower().count('a')} vezes em '{s}'" 


string = input("Informe a string: ")
resultado = hasA(string)
print(resultado)