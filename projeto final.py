import time
import random

vida=100
poupar=0
monstroV = int(random.randint(12,18))

def matou():
  print('Você matou o monstro!!!')

def e():
  print(' ')

def t(p1):
  time.sleep(p1)

def v():
  print(f'Você esta com {vida} de vida')

def errado():
    print('Essa opção não existe, escolha uma opção valida!!!')

def monstro(nome_monstro, monstroV, nome, vida, espada, punho, poupar):
  while monstroV > 0 :
    print(f'{nome_monstro}--hp: {monstroV}')
    e()
    e()
    print(f'{nome}--hp: {vida}')
    e()
    print('1.Espada\n2.Punhos\n3.Chorar\n4.Poupar')
    e()
    esc = input('O que você ira fazer ? [e/pu/c/po] ')
    vida = vida - random.randint(4,8)
    t(1)
    if vida <= 0: 
      print('Você morreu!!!')
      break
    elif esc == "e":
      monstroV = monstroV - espada
      print(f'Você deu {espada} de dano ')
    elif esc == 'pu':
      monstroV = int(monstroV - punho)
      print(f'Você deu {punho} de dano ')
    elif esc == 'c' and vida < 100:
      curado = random.randint(8,12)
      vida = vida + curado
      print(f'Você se curou {curado} de vida ')
    elif esc == 'po':
      print('Nos não precisamos lutar')
      poupar = poupar + random.randint(1,3)
    elif poupar >= 12:
      print('O monstro entendeu seu lado e foi embora')
      break
    elif esc == 'c' and vida >= 100:
      print('Você não pode chorar no momento')
    if esc == 'e' or "pu":
      poupar = 0
  poupar = 0
  matou()
  v()


def espada ():
    print("""
    
                                           
                               &&&&&&& 
                             &&**///&& 
                          &&&**//***&& 
                        &&***//**&&&   
                      &&**///**&&      
                   %&&**//***&&        
      &&&&       &&/**//**&&&          
      &&%%&&&  &&***//**&&             
      &&%%&&&  &&***//**&&             
        &&(((&&**//***&&               
        &&(((&&//**#&&                 
          &&&((&&&&                    
        %%###&&((%%&&&                 
      %%((&&&  &&&&%%%&&               
 &&&&#&&         &&&&&               
 &&(((&&                               
 &&%%%&&                               
 &&&&&&&                          
    
    """)

def morte():
  print('''
               @@@@@@@@@@@@@@@@@@@               
             @@@                 @@@             
           @@                       @@           
         @@        Game   Over        @&         
         @                             @         
        @@ @#                       #@ %@        
        @  @                         @  @        
        @@ @@                       *@  @        
         @  @                       @% @%        
         @@ @  @@@@@@@     @@@@@@@  @ @@         
           @@ @@@@@@@@     @@@@@@@@ @@           
  #@@@     @@  @@@@@@       @@@@@@  %@     @@@@  
  @  @@    @%   @@@*   @ @    @@@    @    @&  @  
 @@    @@@ #@         @@ @@         @@ @@@    @@ 
@         #@@@@@@    ,@@ @@%    @@@@@@          @
  %,  @@@     @@@@@   #   %   @@@@@     @@@  %%  
          @@@  @ @@@         @@@ @  @@@          
              @@ @  @@  @  @* ,@ @@              
             @@@, @ @@  @  @% @  @@@             
         @@@*  %@    .@@@@@.    @@   @@@         
   @          @@@@@           #@@@@          @%  
    @@    @@@      @@@@@@@@@@@      @@@    @@*   
     @%  @                             @#  @     
     @@@@                               @@@@     
   ''')

def manopla():
  print('''

  ''')



print('''

  ____                         _           _                       _____                                                _____       _   _                 
 |  _ \                       (_)         | |                     |  __ \                                       ___    |  __ \     | | | |                
 | |_) | ___ _ __ ___   __   ___ _ __   __| | ___     __ _  ___   | |  | |_   _ _ __   __ _  ___  ___  _ __    ( _ )   | |__) |   _| |_| |__   ___  _ __  
 |  _ < / _ \ '_ ` _ \  \ \ / / | '_ \ / _` |/ _ \   / _` |/ _ \  | |  | | | | | '_ \ / _` |/ _ \/ _ \| '_ \   / _ \/\ |  ___/ | | | __| '_ \ / _ \| '_ \ 
 | |_) |  __/ | | | | |  \ V /| | | | | (_| | (_) | | (_| | (_) | | |__| | |_| | | | | (_| |  __/ (_) | | | | | (_>  < | |   | |_| | |_| | | | (_) | | | |
 |____/ \___|_| |_| |_|   \_/ |_|_| |_|\__,_|\___/   \__,_|\___/  |_____/ \__,_|_| |_|\__, |\___|\___/|_| |_|  \___/\/ |_|    \__, |\__|_| |_|\___/|_| |_|
                                                                                       __/ |                                   __/ |                      
                                                                                      |___/                                   |___/                       

''')

print('Este sera um jogo de rpg com escolhas, dependendo da sua escolha \nvocê pode morrer ou prosseguir ate seu final e ver o que ira acontecer')
e()
esc = str(input('Você deseja começar o jogo?[s/n] '))

while vida > 0 :
  if esc == 's':
    e()
    nome = input('Qual seria seu nome: ')
    e()
    print('Então vamos embarca em uma jornada inesquecivel .')
    e()
    t(2)
    print('Você é um jovem explorador que em sua mochila tem uma espada um pouco velha,')
    e()
    t(2.6)
    print('Em sua busca por uma nova aventura acaba se deparando com a entrada de uma dungeon subterranea.')
    e()
    t(3.5)
    esc = str(input('Você deseja entrar na dungeon? [s/n] '))

    if esc == "s":
      e()
      print("Você desce as escadas, começa a ouvir uns barulho estranhos. ")
      e()
      t(2.5)
      print('Chegandao em uma sala bem grande, cheia de poeira e ossos pelo chão.')
      e()
      t(2.5)
      print('Você ve alguns caminhos que podera seguir para chegar ao fim da dungeon.')
      e()
      t(3)
      esc = str(input('Você ira para esquerda , para a direita ou sentar e chorar? [d/e/c] '))

      if esc == 'd':
        e()
        print(f'Você começa a andar em direção a direita.')
        t(2)
        print('Quando chega aparentimente não tem nada na sala.')
        t(2.5)
        esc = input('Você pode continuar para proxima sala ou ficar olhando a sala. [c/f] ')
        if esc == "c":
          e()
          print("Você prossegue para proxima sala,")
          e()
          t(1)
          print("Sentindo que alguma coisa foi deixada para traz.")
          e()
          t(3)
          print('')
        elif esc == "f":
          e()
          print('Você fica olhando cada canto da sala,')
          t(2)
          print('você começa a pensar por que você decidiu ficar olhando se não havia nada')
          t(2)
          esc = input('Você ira prosseguir para proxima sala ou ira ficar olhando novamente? [p/f] ')
          if esc == 'f':
            e()
            print('Você fica la olhando para cada canto da sala ate que...')
            e()
            t(3)
            print('Você percebe uma parte estranha no rodapé da sala')
            e()
            t(2)
            print('Percebe que é possivel afundalo')
            e()
            t()
          elif esc == 'p':
            e()
            print("Você prossegue para proxima sala,")
            e()
            t(1)
            print("Sentindo que alguma coisa foi deixada para traz.")
            e()
            t(4)
            print('Seguindo para proxima sala você ve uma borboleta com um desenho de caveira nas asas, mas a ignora.')
            e()
            t(4)
            print("Chegando na proxima sala você se depara com algumas cobras")
            e()
            t(2)
            print('Que você se lembra de ter aprendido que eram pythons bebês')
            e()
            t(2)
            print('E não são nem um pouco amigaveis')
            e()
            t(1)
            print('Mas ja era tarde pois ja haviam te certado')
            e()
            t()

      if esc == 'e':
        print('voce foi par')

      if esc == 'c':
        e()
        print('Voce começa a deitar no chão lentamente,')
        e()
        t(2)
        print('começando a pensar na sua vida enquanto chora.')
        t(1.75)
        print('...')
        t(1.75)
        print('...')
        t(1.75)
        print('...')
        t(1.75)
        e()
        print('Um monstro começa a chegar perto.')
        e()
        t(1.75)
        print('Você se levanta e se prepara para luta!')
        e()
        t(2.5)
        if 0 == 0:#batalha
          monstro('Esqueleto', monstroV, nome, vida, 8, 4, poupar)

    elif esc == "n":
      e()
      print('Você vai em direção a cidade,')
      e()
      t(1.5)
      print('Mas acaba caindo em um buraco.')
      e()
      t(1.5)
      esc = str(input('Você se segura na borda, você ira soltar a borda ou continuar se segurando? [segurar/soltar] '))
      if esc == "segurar":#morte
        e()
        print('Você fica segurando por alguns segundos,')
        e()
        t(3)
        print('Mas você fica cansado e solta,')
        e()
        t(3)
        print("Caindo de cabeça no chão e acaba morrendo.")
        e()
        t(3.55)
        morte()
        break
      elif esc == "soltar":
        e()
        print('Você cai bruscamente encima de um slime,')
        e()
        t(1.5)
        print('O matando ,')
        e()
        t(1)
        print('Mas você continua inteiro.')
        e()
        t(2)
        print('Você se levanta e vai em direção a porta,') 
        e()
        t(2)
        print('Você ve um slime.')
        e()
        t(2)
        esc = input('Você pode tentar virar amigo ou mata-lo. [a/m] ')
        if esc == 'a':
          e()
          print('Você se aproxima dele calmamente')
          e()
          t(2)
          print('Ele fica bem assustado por ser bem menor que você ')
          e()
          t(2)
          print('Mas mesmo assim parece gostar de você.')
          e()
          t(5)
          print('Você então procegue')
        elif esc == 'm':
          e()
          print('Você tenta bater nele com sua espada,')
          e()
          t(1.75)
          print('mas infelizmente quando encosta nele ela se derrete,')
          e()
          t(1.75)
          print('logo em seguida ele pula em você fazendo você virar so os osso.')
          e()
          t(3)
          e()
          morte()
  elif esc == 'n':
    e()
    print("Ja que você diz, aqui me dispeço")
    break

if vida <= 0 :
  print('Seu HP chegou 0')
  e()
  t(2.3)
  morte()
