texto = "Não Gosto de Python"
print(texto[5:]) #Aqui ele me diz a frase começando pelo caractere "5"

texto = "Não Gosto de Python"
print(texto[10]) #Essa código me mostra qual é o caractere "10"

texto = "Não Gosto de Python"
print(texto[:11]) #Ele vai mostra o texto do caractere "0" até o caractere "11"

texto = "Não Gosto de Python"
print(texto[2:14]) #Desta forma ele vai mostrar o texto do caractere "2" até o "14"

texto = "Não Gosto de Python"
print(texto[::2]) #Aqui ele mostra o texto pulando uma letra

texto = "Não Gosto de Python"
print(texto[2:16:3]) #Ele vai mostrar o código do caractere "2" até o caractere "16" pulando de 2 em 2 caracteres

texto = "Não Gosto de Python"
print(texto[10::2]) #Nessa linha de código ele mostra o texto começando do caractere "10" até o último caractere pulando de uma em uma letra



texto = "Não Gosto de Python"
print(texto.upper) #Aqui ele vai colocar todo o texto em letra maiúscula

texto = "Não Gosto de Python"
print(texto.upper[:15:2]) #Aqui ele vai mostrar o texto do primeiro caractere até o caractere 15 pulando uma em uma letra tudo maiúsculo

texto = "Não Gosto de Python"
print(texto.lower) #Ele vai mostrar todo o texto em minúsculo, ou seja as letras que estavam em maiúscolo vão estar em minúsculo




texto = "Não Gosto de Python"
print(texto.count("o")) #Nesse código ele conta quantos "o" tem na string "texto", que no caso é "4"

texto = "Não Gosto de Python"
print(texto.count("O")) #A letra "O" é diferente da letra "o" em quanto existem 4 "o" existem 0 "O"

texto = "Não Gosto de Python"
print(texto.upper().count("O")) #Para contar quantos "o" minúsculos e quantos "O" maiúsculo extitem se usa esse código, que simplesmente
#Coloca todo o texto em maiúsculo e depois vê quantos "o" maiúsculo existem no texto ou frase



texto = "Não Gosto de Python"
print(len(texto)) #Aqui ele vai mostrar quantas caracteres existem no texto (19)

texto = "   Não Gosto de Python   "
print(len(texto)) #Ele vai mostrar quantas caracteres existem no texto, contando com os espaços ou seja de 19 foi para 25 caracteres

texto = "               Não Gosto de Python             "
print(len(texto.strip())) #O comando "strip" remove os espaços indesejados, ou seja esse texto deveria ter mais de 30 caracteres, pórem
#O comando "strip" removeu os espaços indesejados e deixou o texto com 19 caracteres

texto = "   Não Gosto de Python   "
print(len(texto.rstrip())) #Esse comando faz a mesma coisa do de cima, porém ele só remove os da direita pois o "r" é de right
#Então essa frase vai ter 22 caracteres

texto = "   Não Gosto de Python   "
print(len(texto.lstrip())) #Esse comando faz a mesma coisa do de cima, porém ele só remove os da esquerda pois o "l" é de left
#Então essa frase vai ter 22 caracteres




texto = "Não Gosto de Python"
print(texto.replace("Não, Eu")) #Nesse comando ele troca a palavra "Não" por "Eu" então a frase: "Não Gosto de Python"
#Vai ficar "Eu Gosto de Python"

texto = "Não Gosto de Python"
texto.replace("Não", "Eu")
print(texto) #Aqui ele vai aparecer "Não Gosto de Python" porque o ".replace" se for usado da forma mostrada no comando de cima, o texto
#Só vai mudar aquela hora, se quiser mudar o texto permaanentemente, vai ser necessário o seguinte comando:

texto = "Não Gosto de Python"
texto = texto.replace("Não","Eu")
print(texto) # Aqui sim ele vai mudar a variável permanentemente



texto = "Não Gosto de Python"
print(texto("Gosto" in texto)) #O comando "in" mostra se tem ou não a palavra escrita na variável, no caso eu perguntei se existe a palavra "Gosto"
#em "texto" como o "in" só diz se é True ou False, ele vai mostrar True já que existi a palavra "Gosto" em "texto"



texto = "Não Gosto de Python"
print(texto.find("Python")) # O comando find mostra qual posição está a primeira letra da palavra pedida, ou seja 13

texto = "Não Gosto de Python"
print(texto.find("Preto")) # Se a palavra pedida não existir vai aparecer "-1"

texto = "Não Gosto de Python"
print(texto.lower.find("python")) # A palavra "python" com o "P" minúsculo não existi, porém com o comando "lower" eu joguei toda
# A variável texto em minúscula e ai sim o find procurou a palavra, no caso vai aparecer 13 já que a palavra foi encontrada



texto = "Não Gosto de Python"
print(texto.split()) # "split" separa o texto em partes, aqui vai aparecer: ['Não', 'Gosto', 'de', 'Python']

texto = "Não Gosto de Python"
dividido = texto.split # Se eu quiser eu posso colocar "print(dividido)" e vai aparecer: ['Não', 'Gosto', 'de', 'Python']
# Mas se eu quiser eu posso colocar print(texto) e vai aparecer: "Não Gosto de Python"

texto = "Não Gosto de Python"
dividido = texto.split
print(dividido[0]) # Aqui ele vai mostrar o primeiro item de dividido que no caso é "Não"

texto = "Não Gosto de Python"
dividido = texto.split
print(dividido[3]) # Aqui ele vai mostrar o terceiro item de dividido que no caso é "Python"

texto = "Não Gosto de Python"
dividido = texto.split
print(dividido[2][1]) # Ele vai mostrar o segundo item que é "de" e vai mostrar a letra número 1, que é o "e" ou seja
# Vai aparecer no terminal somente "e"











