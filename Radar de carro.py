velocidade = int(input("Qual a velocidade do carro? "))
if velocidade <= 80:
    print("Sua velocidade está ok, dirija com segurança!")
else:
    print("O carro está a cima do limite de velocidade.")
    multa = (velocidade-80) *7
    print("A multa vai ser de R${:.2f}".format(multa))