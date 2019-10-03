import random

print('.\n.\n.')
print('Bem-vindo ao Camel!')
print('Sobreviva ao deserto e escape do dono do camelo.')
print('Você roubou um camelo para atravessar o grande deserto de Mobi.')
print('O dono do camelo o quer de volta e está te perseguindo!')
print('Sobreviva ao deserto e escape do dono do camelo.')
print('.\n.\n.')

km = 0
sd = 0 #sede
cs = 0 #cansaço
kmdn = -20 #km dono
cantil = 3



while sd or cs >= 0  :
    kmt = km - kmdn
    print('A. Beber água do cantil.')
    print('B. Avançar com velocidade moderada.')
    print('C. Avançar com velocidade máxima.')
    print('D. Parar para dencansar à noite.')
    print('E. Checar o status.')
    print('Q. Sair.')
    print('.\n.\n.')

    escolha1 = str(input('Qual sua escolha? '))
    print('.\n.\n.')

    if escolha1 == "q" :#Q. Sair.
        print('você saiu')
        break

    elif escolha1 == 'e' :#E. Checar o status.
        print(f'Quilômetros percorridos: {km}')
        print('.')
        print(f'água no cantil: {cantil}')
        print('.')
        print(f'{kmt}km de distancia do dono')
        print('.')

    elif escolha1 == 'd' :#D. Parar para dencansar à noite.
        cs = 0
        print('Seu camelo esta revigorado')
        print('.')
        andou_d = random.randint(7, 14)
        kmdn = kmdn + andou_d

    elif escolha1 == 'c' :#C. Avançar com velocidade máxima.
        andou = random.randint(10, 20)
        km = km + andou
        cs = cs + random.randint(1, 3)
        sd = sd + 1
        andou_d = random.randint(7, 14)
        kmdn = kmdn + andou_d
        print(f'Você andou {andou}km')
        print('.')

    elif escolha1 == 'b':#B. Avançar com velocidade moderada.
        andou = random.randint(5, 12)
        km = km + andou
        andou_d = random.randint(7, 14)
        kmdn = kmdn + andou_d
        sd = sd + 1
        cs = cs + 1
        print(f"Você andou {andou}km")
        print('.')
    elif escolha1 == 'a':#A. Beber água do cantil.

        if cantil >= 1:
            
            cantil = cantil - 1
            sd = 0
            print('Você esta hidratado')
            print('.')
        else:
            print('Você não tem agua no cantil')
            print('.')
            
    elif km >= 200:
        print('==========')
        print('Você ganhou!!!')
        print('==========')
        print('Meus parabens!!')
        print('==========')
        break

    if sd > 4:
        print('Você esta com sede')
        print('.')

    if cs > 5:
        print("Seu camelo esta cansado")
        print('.')

    if kmt <= 15:
         print('O dono se aproxima')
         print('.')
    
    elif sd > 6:
        print('==========')
        print('Você morreu de sede')
        print('==========')
        break

    elif cs > 8:
        print('==========')
        print('Seu camelo morreu')
        print('==========')
        break

    elif kmt == 0:
        print('==========')
        print('O dono te pegou')
        print('==========')
        break
    
    elif km >= 200:
        print('==========')
        print('Você ganhou!!!')
        print('==========')
        print('Meus parabens!!')
        print('==========')
        break
