pa = float(input("Coloque o comprimento do cateto oposto: "))
pb = float(input("Coloque o comprimento do cateto adjacente: "))
resultado = (pa ** 2 + pb ** 2) #Cateto oposto ao cubo, cateto adjacente ao cubo, oposto + adjacente
final = resultado ** 0.5  #Calculando a raiz quadrada elevando a meio 
print("O comprimento do cateto oposto é {} e do adjacente é {:.2f}, e a hipotenusa é {}".format(pa,pb,final)) 


'''
A hipotenusa é o cateto oposto vezes o cubo mais o adjacente ao cubo, ai a raiz quadrada disso é a
hipotenusa
'''

#Esse codigo é a mesma coisa do de cima, porém ele usa o comando "math" de matematica que facilita os calculos.
import math
pa = float(input("Coloque o comprimento do cateto oposto: "))
pb = float(input("Coloque o comprimento do cateto adjacente: "))
resultado = math.hypot(pa, pb)
print("O comprimento do cateto oposto é {} e do adjacente é {}, e a hipotenusa é {:.2f}".format(pa,pb,resultado)) 