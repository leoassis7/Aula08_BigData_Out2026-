#SETS "Conjuntos"
#coleção mutável
#não garante ordem
#não permite indice


#Criar sets vazio
dias = set()
dias.add('Segunda')
dias.add('Terça')
print(dias)


#Conjuntos inicializados
frutas ={'Maçã', 'Uva', 'Pera', 'Banana'}
print(frutas)

#Remover
frutas.remove('Maçã')
#frutas.discard('Maçã')
print(frutas)
print(len(frutas)) #contagem de frutas

#converter lista para sets
lista = ['5', '7', '4', '6']
conjunto_set = set(lista)
print(conjunto_set)


numeros = [5, 7, 4, 1, 4, 8, 13, 8, 10, 8]
conjunto = set(numeros) #converter lista para conjunto set
numeros = list(conjunto) #converter conjunto  para lista 
print(conjunto)
print(len(conjunto))




