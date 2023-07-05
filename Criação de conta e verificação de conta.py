import time
#Criação de conta
print("\33[32mÓla, parece que você ainda não tem um cadastro no Babagi express!\33[m")
time.sleep(1.5)
print('\33[32mPara criar uma conta siga as seguintes instruções.\33[m')
time.sleep(1.5)
while True: # O while True é para que as informações ali ditas não sejam descartadas depois e sim salvas.
    email = input("Coloque seu email: ")
    ver = '@' in email # Aqui ele verifica se existi ou não '@' em email, se existir é True se não é False.
    if ver: # Quando temos um if mais uma variável é porque ela esta da seguinte forma: if ver == True. Porém essa forma foi simplificada para if ver: apenas.
        break # Esse break significa acabar ou fim ou quebrar mesmo, ali se ver for igual a True o comando if acaba, se for falso ele continua para as linhas if.
    time.sleep(1.5)
    print('\33[1;31mParece que esse email não existe. Tente novamente.\33[m')
    time.sleep(1)  
usuario = str(input("Coloque um nome de usuário: "))
while True: # Aqui novamente estamos dizendo que oque acontecer aqui dentro é para ficar salvo.
    senha = str(input("Crie uma senha: "))
    if len(senha) >= 8: # O comando "len(senha)" está contando quantas caracteres tem em senha, caso tenha menos que 8 vai falar que é muito curta.
        break
    time.sleep(1.5)
    print("\33[1;31mParece que essa senha é muito curta, tente novamente.\33[m")
time.sleep(1.5)
print("\33[1;32mSua conta foi criada com sucesso!")
time.sleep(2.5)

#Login no site 
print("\33[33mParece que você já tem uma conta!\33[m")
time.sleep(1)
print("\33[1;33mPara logar em sua conta siga as instruções!\33[m")
time.sleep(2)
vemail = str(input("Coloque seu email: "))
time.sleep(1)
vsenha = str(input("Coloque sua senha: "))
while vemail != email or vsenha != senha: # Aqui está sendo dito que caso vemail seja diferente de email OU vsenha seja diferente de senha execute as linhas abaixo.
    time.sleep(1.5)
    print("\33[1;31mParece que seu email ou sua senha estão incorretos.\33[m")
    vemail = input("Coloque seu email : ")
    vsenha = input("Coloque sua senha : ")
else: # Caso o while deixe de ser executado aparece isso.
    time.sleep(1)
    print("\33[1;32mEstá tudo certo!")
    print("\33[1;32mVocê pode prosseguir!\33[m")


