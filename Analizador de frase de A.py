frase = str(input("Digite a frase: ")).upper()
print("A letra A apareceu {} vezes na frase.".format(frase.count('A')))
print("A primeira letra A aparece na  posição {}.".format(frase.find('A')+1))
print("A última letra A aparece na  posição {}.".format(frase.rfind('A')+1))

