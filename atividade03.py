notas = []
contador = 0

while contador <= 3:
    contador += 1
    
    nota = float( input('Insira uma Nota: '))
    notas.append(nota)

print(f'Boletin de Notas: {sorted(notas)}')

