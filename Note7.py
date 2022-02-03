def pergunta():
	r1 = input("seu numero tem a letra 'o' no nome ? [s/n] ")
	return r1

def pergunta2():
	r2 = input('Ele é mutiplo de 2 ? [s/n] ')
	return r2

def pergunta3():
	r3 = input("o numero tem  no total 4 letras ? [s/n] ")
	return r3

def pergunta4():
	r4 = input('O dobro do seu numero é maior que 10 ? [s/n] ')
	return r4

print("escolha um numero de 1 a 10 e guarde para você ")
input("aperte ENTER quando estiver pronto ")

if pergunta() == 's':
	if pergunta2() == 's':
		if pergunta3() == 's':
			if pergunta4() == 's':
				print('Seu numero é 8. ')
			else:
				print('Seu numero é 2. ')
		else:
			print('seu numero é 4. ')
	else:
		if pergunta3 == 's':
			print('Seu numero é 9. ')
		else: 
			print('Seu numero é 5. ')
else:
	if pergunta2 == 's':
		if pergunta3 == 's':
			if pergunta4 == 's':
				print('Seu numero é 6. ')
			else:
				print('Seu numero é 3. ')
		else:
			print('seu numero é 10')		
	else:
		if pergunta3 == 's':
			print('Seu numero é 7. ')
		else:
			print('Seu numero é 1. ')
