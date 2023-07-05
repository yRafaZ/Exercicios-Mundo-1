r1 = float(input("Coloque o tamanho da reta número um: "))
r2 = float(input("Coloque o tamanho da reta número dois: "))
r3 = float(input("Coloque o tamanho da reta número três: "))
if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print("Não é posivel formar um triângulo com essas três retas.")
else:
    print("É possivel formar um triângulo com essas três retas.")