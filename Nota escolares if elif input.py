nota1 = float(input("Coloque sua nota do primeiro bimestre aqui:"))
nota2 = float(input("Agora do segundo:"))
nota3 = float(input("Do terceiro:"))
nota4 = float(input("Por fim o do quarto:"))
soma = nota1 + nota2 + nota3 + nota4
media = soma/4
if(media >= 7):
    print(f"Sua média foi de {media} pontos, parabéns você passou.")
elif (media < 7):
     print(f"Sua média foi de {media} pontos, parece que você não passou.")