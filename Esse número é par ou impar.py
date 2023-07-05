num = int(input("Coloque o seu número: "))
resultado = num % 2 # Aqui ele simplismente está fazendo o seguinte: Depois de dividir esse número (num) por 2, sobra certo número.
                    # Por exemplo, 69 é um número impar, quando dividido por 2 sem usar vírgula da 34 e sobra 1, ou seja,
                    # Se eu colocar em "num" 69 e colocar para imprimir "resultado" vai aparecer 1, já que é a sobra
                    # De tal número dividido por 2 sem usar vírgula. 
if resultado == 1:
    print("O número {} é impar!".format(num))
else:
    print("O número {} é par".format(num))
