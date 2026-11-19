produtos = []

for i in range(3):
    produto = input('Informe o nome do produto: ')
    produtos.append(produto) #adiciona na lista de produtos
    print(produtos) # Neste caso ele irá apresentar a cada adição da lista

    #Acesso ao elemento

n = int(input('Digite a posição do elemento a acessar: '))
print(produtos[n-1])

#print(produtos) #Se colocar fora do for ele informarar somente no final.

#alterando uma lista
produtos[n-1] = input(f'Informe o nome do outro elemento na posição {n}: ')
print(produtos)

#Removendo  da Lista
produto_a_remover = input('\nDigite o nome do produto a remover: ')

if produto_a_remover in produtos:

   produtos.remove(produto_a_remover)
print(produtos)
