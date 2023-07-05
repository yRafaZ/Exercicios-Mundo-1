import random
num = random.randint(1,5)
print('Pensei em um número de 1 a 5, tente adivinhar qual número eu pensei!')
escolha = int(input(""))
if escolha == num:
    print('Parabéns! O número {} foi realmente o que escolhi!'.format(num))
else:
    print("Você errou. O número que eu tinha pensado era {}.".format(num))
