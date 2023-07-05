dis = float(input("Quantos Km de distância vão ser em sua viagem? "))
if dis >= 200:
    dis = dis*0.45
    print("O valor de sua viagem com o desconto dos 200 kilômetros foi de {} reais.".format(dis))
else:
    dis = dis*0.50
    print("O valor de sua viagem é de R${}".format(dis))