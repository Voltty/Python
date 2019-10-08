import random

print('=========='*8)
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
d = 5
fim = 'fim'
vazio = ''


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

    if escolha1 == 'q' :#Q. Sair.
        print('Você saiu do jogo!!!')
        break

    elif escolha1 == 'e' :#E. Checar o status.
        print(f'Quilômetros percorridos: {km}')
        print('.')
        print(f'Água no cantil: {cantil}')
        print('.')
        print(f'{kmt}km de distancia do dono.')
        print('.')

    elif escolha1 == 'd' :#D. Parar para dencansar à noite.
        cs = 0
        print('Seu camelo esta revigorado.')
        andou_d = random.randint(7, 14)
        kmdn = kmdn + andou_d
        print('.')

    elif escolha1 == 'c' :#C. Avançar com velocidade máxima.
        andou = random.randint(10, 20)
        km = km + andou
        cs = cs + random.randint(1, 3)
        sd = sd + 1
        andou_d = random.randint(7, 14)
        kmdn = kmdn + andou_d
        print(f'Você andou {andou}km.')
        print('.')

    elif escolha1 == 'b':#B. Avançar com velocidade moderada.
        andou = random.randint(5, 12)
        km = km + andou
        andou_d = random.randint(7, 14)
        kmdn = kmdn + andou_d
        sd = sd + 1
        cs = cs + 1
        print(f"Você andou {andou}km.")
        print('.')

    elif escolha1 == 'a':#A. Beber água do cantil.
        if cantil >= 1:
            
            cantil = cantil - 1
            sd = 0
            print('Você esta hidratado.')
            print('.')

        else:
            print('Você não tem agua no cantil.')
            print('.')

    if km >= 200:#ganhar
        print('================')
        print('Você ganhou!!!')
        print('================')
        print('Meus parabens!!!')
        print('================')
        break

    if escolha1 == 'b' or 'c':#chance de oasis
        sorte = random.randint(1,20)
        if sorte == 10:
            print('Você achou um oasis!')
            print('.')
            sd = 0 
            cs = 0
            print('Sua sede e cansaço foram restaurados!!')
            sorte == 0

        if sorte == 15:
            preço_agua = random.randint(1,5)
            comprar = str(input(f'Você achou uma pessoa vendendo um cantil com água, vendendo por {preço_agua}. Você quer comprar? s/n'))
            if comprar == "s" and d >= preço_agua:
                print('Pegue essa água')
                d = d - preço_agua
                cantil = cantil + 3
                print('.')
                print('Agora você deixa o vendedor e volta para a fuga')





    if sd > 4:#aviso
        print('Você esta com sede!!')
        print('.')

    if cs > 5:#aviso
        print("Seu camelo esta cansado!!")
        print('.')

    if kmt <= 15:#aviso
         print('O dono se aproxima!!!')
         print('.')

    if sd > 6:#perder
        print(f'{vazio:=^20}')
        print('Você morreu de sede!')
        print(f'{fim:=^20}')
        break

    if cs > 8:#perder
        print(f'{vazio:=^20}')
        print('Seu camelo morreu de cansaço!')
        print(f'{fim:=^20}')
        break

    if kmt <= 0:#perder
        print(f'{vazio:=^20}')
        print('O dono te pegou!')
        print(f'{fim:=^20}')
        break
