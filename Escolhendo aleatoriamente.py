import random
um = str(input("Coloque o primeiro nome:"))
dois = str(input("Coloque o segundo:"))
terceiro = str(input("Coloque o terceiro: "))
quarto = str(input("Coloque o último:"))
aleatorio = random.choice([um,dois,terceiro,quarto])
print("A pessoa escolhida foi: {}".format(aleatorio))
