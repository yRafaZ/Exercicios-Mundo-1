from datetime import date
ano = int(input("Que ano quer analizar? (Se quiser analizar o ano atual digite 0.)"))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 and ano % 400:
    print("O ano {} é um ano bissexto!".format(ano))
else:
    print("O ano {} não é um ano bissexto.".format(ano))