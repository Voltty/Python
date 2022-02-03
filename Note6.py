##########exercicio1##########


palavra = str(input('Coloque uma paravra: '))
for i in palavra:
	print(i)

##########exercicio2##########
palavra2 = str(input("Coloque outra palavra: "))
nova_palavra = ''

for letra in palavra2:
	nova_palavra = nova_palavra + letra

	print(nova_palavra)



##########exercicio3##########
palavra3 = str(input("Coloque outra palavra: "))
nova_palavra = ''
contador = 0

for letra in palavra3:
	nova_palavra = nova_palavra + letra
	contador = contador + 1
	if contador%2 == 0:
		print(nova_palavra.upper())
	elif contador%2 != 0:
		print(nova_palavra)

##########exercicio4##########
palavra5 = str(input("Coloque outra palavra: "))
nova_palavra = ''

for letra1 in palavra5:
	nova_palavra = nova_palavra + letra1
	nova_palavra
 
print(nova_palavra)

	

##########exercicio5##########
palavra4 = str(input("Coloque outra palavra: "))
np=""
for letra in palavra4:
	if letra == "a":
		letra = "4"
	if letra == "e":
		letra = "3"
	if letra == "l":
		letra = "1"
	if letra == "t":
		letra = "7"
	print(letra)


##########exercicio6##########
palavra = input("escolha uma palavra para ver se ela é um palindromo: ")
print(palavra[::-1])


##########exercicio7##########
palavra = input("escolha uma palavra para ver se ela é um palindromo: ")
arvalap = palavra[::-1]

if palavra == arvalap:
	print('Essa palavra é um palimdromo!! ')
else:
	print('Ela n é um palimdromo!! ')








