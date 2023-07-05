import random
um = str(input("Coloque o primeiro nome: "))
dois = str(input("Coloque o segundo nome: "))
tres = str(input("Coloque o terceiro nome: "))
quatro = str(input("Coloque o quarto nome: ")) 
lista = ([um, dois, tres, quatro])
random.shuffle(lista)
print("A sequência sorteada foi: {} ".format(lista))
