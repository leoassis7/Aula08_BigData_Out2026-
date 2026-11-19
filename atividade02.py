numeros = []
quantidade = len(numeros)
while True:
    numero = int(input('Insira um número: '))
    continuar = input(' Caso parar digite N. Ou insira enter: ').upper()
    numeros.append(numero)
    quantidade = len(numeros)
    print(f'Quantidade de números armazenados: {quantidade}')

    if continuar == 'N':
        print(f'Total {numeros}')
        break
