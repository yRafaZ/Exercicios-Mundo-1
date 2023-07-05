sal = int(input("Coloque o sálario para o aumento: "))
aum = 0
if sal >= 5000:
    aum = sal * 10 / 100 + sal
else:
    aum = sal * 15 / 100 + sal
print("Agora o seu salário de {} vai para {} com o aumento!".format(sal,aum))
