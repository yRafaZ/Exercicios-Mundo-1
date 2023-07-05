# Criação de conta
print("\33[32mÓla, parece que você ainda não tem um cadastro no Babagi express!\33[m")

while True:
    email = str(input("Coloque seu Email: "))
    ver = "@" in email
    if ver:
        break
    print("\33[31mParece que esse email não existe, tente novamente.\33[m")

usuario = str(input("Coloque um nome de usuário: "))
senha = str(input("Crie uma senha: "))

# Login no site 
print("\33[33mParece que você já tem uma conta!\33[m")
vemail = str(input("Coloque seu email: "))
vsenha = str(input("Coloque sua senha: "))
while vemail != email or vsenha != senha:
    print("\33[1;31mParece que seu email ou sua senha estão incorretos.\33[m")
    vemail = input("Coloque seu email: ")
    vsenha = input("Coloque sua senha: ")
else:
    print("\33[1;32mEstá tudo certo!")
