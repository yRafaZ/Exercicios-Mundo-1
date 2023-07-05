salario = float(input("Qual é o salário recebido mensalmente:"))
aumento = float(input("Em porcentagem qual foi o aumento do salário?: "))
novo = salario + (salario*aumento/100)
print("O salário recebido mensalmente após o aumento é de R${}".format(novo))
