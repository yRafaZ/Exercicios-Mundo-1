# lista dos produtos disponíveis
produtos = ["produto 1", "produto 2", "produto 3"]

# preços dos produtos
precos = [10.00, 20.00, 30.00]

# exibir os produtos e seus preços para o cliente
print("Produtos disponíveis:")
for i in range(len(produtos)):
    print(f"{i + 1} - {produtos[i]} - R${precos[i]:.2f}")

# perguntar ao cliente qual produto ele deseja comprar
produto_escolhido = int(input("Digite o número do produto que você deseja comprar: "))

# verificar se o produto escolhido é válido
while produto_escolhido < 1 or produto_escolhido > len(produtos):
    produto_escolhido = int(input("Por favor, digite um número de produto válido: "))

# obter o preço do produto escolhido
preco_produto_escolhido = precos[produto_escolhido - 1]

# perguntar ao cliente qual forma de pagamento ele deseja usar
forma_de_pagamento = input("Digite a forma de pagamento (dinheiro, cartão ou parcelado): ")

# verificar se a forma de pagamento é válida
while forma_de_pagamento not in ["dinheiro", "cartão", "parcelado"]:
    forma_de_pagamento = input("Por favor, digite uma forma de pagamento válida: ")

# calcular o preço final do produto, levando em conta a forma de pagamento
if forma_de_pagamento == "dinheiro":
    preco_final = preco_produto_escolhido * 0.9
elif forma_de_pagamento == "cartão":
    preco_final = preco_produto_escolhido * 0.95
else:
    preco_final = preco_produto_escolhido

# exibir o preço final para o cliente
print(f"O preço final do produto escolhido é R${preco_final:.2f}.")