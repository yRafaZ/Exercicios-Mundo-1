import math
angulo = float(input("Digite o ângulo desejado: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O seno do ângulo de {} é {:.2f} o cosseno é {:.2f} e o tangente é {:.2f}".format(angulo,seno,cosseno,tangente))
