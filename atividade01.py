#informações : 10 vendas, armazenar, apresentar soma de vendas  e qtd de vendas

vendas = []
total = sum(vendas)


for i in range(3):
    venda = float(input('Informe o valor da venda: '))
    vendas.append(venda) #adiciona na lista de produtos
    total = sum(vendas)
        
  


print(f'Total de vendas: {total}')