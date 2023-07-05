produto = float(input("Qual o valor do produto? "))
desconto = float(input("Qual o valor do desconto? "))
menos = produto*desconto/100
print("O produto custava R${} com o desconto ele vai custar R${}".format(produto, produto-menos ))