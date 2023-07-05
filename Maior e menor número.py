um = float(input("Coloque o primeiro valor:"))
dois = float(input("Coloque o segundo valor:"))
tres = float(input("Coloque o terceiro valor:"))
maior = 0
menor = 0
if um>dois and um>tres:
    maior = um
if dois>um and dois>tres:
    maior = dois
if tres>um and tres>dois:
    maior = tres

if um<dois and um<tres:
    menor = um
if dois<um and dois<tres:
    menor = dois
if tres<um and tres<dois:
    menor = tres


print("O maior número é: {}".format(maior))
print("O menor número é: {}".format(menor))
