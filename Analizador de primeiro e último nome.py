texto = str(input("Coloque seu nome: "))
nome = texto.split()
ultimo = nome[len(nome)-1]
print("O seu primeiro nome é: {}".format(nome[0]))
print("O seu último nome é: {}".format(ultimo))