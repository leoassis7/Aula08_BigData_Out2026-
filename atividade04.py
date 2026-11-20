numeros = []

for i in range(3):
    numero = int(input('Insira um número: '))
    numeros.append(numero)

    conjunto = set(numeros)
    numeros = list(conjunto)

print(conjunto)
                
