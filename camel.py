import random

print('Bem-vindo ao Camel!')
print('Sobreviva ao deserto e escape do dono do camelo.')
print('Você roubou um camelo para atravessar o grande deserto de Mobi.')
print('O dono do camelo o quer de volta e está te perseguindo!')
print('Sobreviva ao deserto e escape do dono do camelo.')

km = 0
sd = 0 #sede
cç = 0 #cansaço
kmdn = -20 #km dono
cantil = 3

kmt = km - kmdn

while sd or cç >= 0 :
	print('A. Beber água do cantil.')
	print('B. Avançar com velocidade moderada.')
	print('C. Avançar com velocidade máxima.')
	print('D. Parar para dencansar à noite.')
	print('E. Checar o status.')
	print('Q. Sair.')
	escolha1 = str(input('Qual sua escolha? '))
	if escolha1 == "q":#Q. Sair.
		print('você saiu')
		break

	elif escolha1 == 'e':#E. Checar o status.
		print(f'Quilômetros percorridos: {km}')
		print(f'água no cantil: {cantil}')
		print(f'{kmt}km de distancia do dono')

	elif escolha1 == 'd':#D. Parar para dencansar à noite.
		cç = 0
		print('Seu camelo esta revigorado')
		andou = random.randint(7,14)
		print(f"Você andou {andou}km")
		km = km + andou
	elif escolha1 == 'c':#C. Avançar com velocidade máxima.
		km = km + random.randint(10, 20)
		cç = cç + random.randint(1, 3)
		sd = sd + 1

		print()
		










	


	

		
