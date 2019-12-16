import time
import random

vida=100
poupar=0
esqueletoV = int(random.randint(12,18))
pythonV = 100
golemV = int(random.randint(25,40))

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

def a1():
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
  print('Mas ja era tarde pois ja haviam te pegado')
  e()
  t(4)
  print('Elas começam a te levar para o ninho delas')
  e()
  t(2)
  print('...')
  t(2.5)
  print('...')
  t(3)
  print('...')
  t(4)
  print('Quando você chega no ninho')
  e()
  t(2)
  print('Avista uma python enorme')
  e()
  t(2)
  print('Que provavelmente é o BOSS da dungeon')
  e()
  t(4)
  print('As python bebês te soltam')
  e()
  t(3)
  print('Você tenta correr mas ja é tarde ')
  e()
  t(3)
  print('Porque ela ja macou você como presa e ira te comer')
  e()
  t(5)
  print('Você tenta bater nela mas é inutil, pois ela é muito forte')
  e()
  t(5)
  print('Então ela te morde, arraca sua cabeça ')
  e()
  t(6.5)
  morte()
  print("A python BOSS comeu você")
  break

# def a2():

# def a2b():

def a3b():
  e()
  t(3)
  print('Você encontrou uma sala com um grande baú')
  e()
  t(4)
  print('Quando você abre o baú ')
  e()
  t(2)
  print('Você ve muito ouro e prata,')
  print('Joias e um item magico estranho')
  e()
  t(5)
  print('Quando você o aperta ele fez um brilho muito forte')
  e()
  t(4)
  print('O deixando cego')
  e()
  t(3)
  print('...')
  e()
  t(3)
  print('...')
  e()
  t(3)
  print('...')
  e()
  t(3)
  print('Quando a cegueira passa você percebe que ')
  e()
  t(8)
  print('Estava na frente de sua cidade')
  e()
  t(5)
  print('Você da um suspiro de alivio')
  e()
  t(3)
  print('E vai em direção a sua casa para descançar um pouco')
  e()
  e()
  t(6)
  fim()
  break



def monstro(nome_monstro, monstroV, nome, vida, espada, punho, poupar,qp,dano_monstro):
  while monstroV > 0 :
    print(f'{nome_monstro}--hp: {monstroV}')
    e()
    e()
    print(f'{nome}--hp: {vida}')
    e()
    print('1.Espada\n2.Punhos\n3.Chorar\n4.Poupar')
    e()
    esc = input('O que você ira fazer ? [e/pu/c/po] ')
    vida = vida - dano_monstro
    t(1)
    if vida <= 0: 
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
    elif poupar >= qp:
      print('O monstro entendeu seu lado e foi embora')
      break
    elif esc == 'c' and vida >= 100:
      print('Você não pode chorar no momento')
    if esc == 'e' or "pu":
      poupar = 0
  poupar = 0
  matou()
  v()

def portaE(f):
  print('Você entra na porta esquerda')
  e()
  t(2.5)
  print(f'{f}')
  e()
  t(3)
  esc = input('esquerda ou direita ? [e/d] ')

def portaD(f):
  print('Você entra na porta direita')
  e()
  t(2.5)
  print(f'{f}')
  e()
  t(3)
  esc = input('esquerda ou direita ? [e/d] ')


def bau():
  print('Você se aproxima do baú')
  e()
  t(2)
  print('Quando você vai abrir')
  e()
  t(3)

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
def luvas():
  print('''
                                                   
               /////////////*****                
            //(((((((((////////*****             
          //(((((((((((//////,,,,,,**            
         //((((((((((((//////*****,,,            
         /((((((((((((/////////*,,,*****         
         //((((((((((//////////,,,,******        
         ////((((((///////////*,,,,******        
         ////////////////////***,,*******        
         ///////////////////************         
         **///////////////**************         
          *////////////****************          
          ****************************           
           **************************            
           *************************             
            ***********************              
              ******************,                
              ,*****************,                
              /((/***************                
              /((#(((/////*/(****                
              /(&&&&&&&&%%%%%%(**                
              //&&&&&&&&%%%%%%/**                
              ////%&&&&%%%%%*****                
                ***************                  
  ''')
def fim():
  print('''
  ______ _                 _             _                    
 |  ____(_)               | |           | |                   
 | |__   _ _ __ ___     __| | ___       | | ___   __ _  ___   
 |  __| | | '_ ` _ \   / _` |/ _ \  _   | |/ _ \ / _` |/ _ \  
 | |    | | | | | | | | (_| |  __/ | |__| | (_) | (_| | (_) | 
 |_|    |_|_| |_| |_|  \__,_|\___|  \____/ \___/ \__, |\___/  
                                                  __/ |       
                                                 |___/        
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
    t(3)
    print('Você é um jovem explorador que em sua mochila tem uma espada um pouco velha,')
    e()
    t(4)
    print('Em sua busca por uma nova aventura acaba se deparando com a entrada de uma dungeon subterranea.')
    e()
    t(5.4)
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
        if esc == "c":#a1
          a1()
          a1b()
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
            print('Quando você o pressiona')
            e()
            t(2)
            print('Cai um golem do teto')
            e()
            t(2)
            print('Você ja preparado para a luta avança')
            e()
            t(4)
            monstro('Golem', golemV, nome, vida, 4, 8, poupar,10000,random.randint(8,12))
            e()
            e(4)
            print('O golem explode so deixando uma espada muito forte no chão')
            e()
            t(3.6)
            print('Você pega a espada ')
            e()
            t(2)
            espada()
            print('\033[;1m"Dano de espada aumentado para 12"')
          if esc == 'p': #a1#morte
            a1()
      if esc == 'e':
        e()
        print('Você começa a andar para a esqueda')
        e()
        t(1.75)
        print('Acaba se deparando com uma sala com dois caminhos')
        e()
        t(3)
        print('O caminho da direita que aparenta ser um caminho reto')
        e()
        t(2.5)
        print('E o caminho da esquerda que parece ser um longo caminho')
        esc = input('Você vai seguir por qual caminho? [e/d] ')
        if esc == 'd':#a1#morte
          a1()
        if esc == 'e':
         portaE('E ja se depara com outras portas.')
          if esc == 'e':
            portaE('Pelo que parece tem mais duas portas.')
            if esc == 'd':
              portaD('E ja se depara com outras portas.'))
              if esc == 'd':
                portaD('Pelo que parece tem mais duas portas')
                if esc == "e":#a3b#FimP
                  a3b()
                  print()
                if esc == 'd':#a1#morte
                  a1()
              if esc == 'e':#a1#morte
                a1()
            if esc == 'e': #a1#morte
            a1()
          if esc == 'd':#a1#morte
            a1()
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
          monstro('Esqueleto', esqueletoV, nome, vida, 8, 4, poupar,12,random.randint(4,8))
          e()
          t(1)
          print('Agora você ja pode prosseguir para proxima sala')
          e()
          t(5)
          print('Quando chega na proxima sala você ve dois baus ')
          e()
          t(2)
          esc = input('Você vai abrir o bau numero 1 ou 2? [1/2]')
          if esc == 1 :#morte
            bau()
            print('Sua mão é comido pelo baú')
            e()
            t(1)
            print('Que na verdade era um monstro')
            e()
            t(2)
            print('Mas desapareceu depois ')
            e()
            t(6)
            morte()
            print('Você ficou deitado sangrando ate morrer')
            break
          elif esc == 2:
            bau()
            print('Você abre o baú e acha')
            e()
            t(2)
            print(luvas)
            e()
            print('Um par de luvas')
            e()
            t(1)
            print('Você as equipa')
            e()
            t(1)
            print('\033[;1m"Dano do socos aumentado de 4 para 12"')
            e()
            t(5)
            print('O outro baú desaparece ')


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
      if esc == "soltar":
        e()
        print('Você cai bruscamente encima de um slime,')
        e()
        t(1.5)
        print('O matando ,')
        e()
        t(3)
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
          t(3)
          print('Ele fica bem assustado por ser bem menor que você ')
          e()
          t(3)
          print('Mas mesmo assim parece gostar de você.')
          e()
          t(6)
          print('Você então prossegue para proxima sala, acompanhado do slime')
          e()
          t(4)
          print('Você percebe que tinha monstros no final do corredor,mas')
          e()
          t(5)
          print('O slime tambem estava quase la, indo enfrentar os monstros')
          e()
          t(4)
          print('Então você sai correndo para protege-lo')
          e()
          t(6)
          print('Quando você chega la, o slime')
          e()
          t(5)
          print('Tinha afugentado os monstros')
          e()
          t(3)
          print('Você aliviado, ve que na sala tem duas portas, uma da diretia e uma na esquerda')
          e()
          t(5)
          esc = input('Você ira pela esquerda ou pela direita? [e/d]')
          if esc == 'd' :
            e()
            t(1)
            print('Você segue pela direita')
            e()
            t(3)
            print('E acha um baú que continha')
            e()
            t(3)
            print(luvas)
            print('Um par de luvas')
            e()
            t(3)
            print('continuando para a proxima sala')
            e()
            t(3.7)
            print('Você ve algo que parece ser uma parede vermelha')
            e()
            t(4.2)
            print('Mas quando se aproxima aquela parede se mexe e era')
            e()
            t(6)
            print('Um golem de fogo enorme')
            e()
            t(4)
            print('Você coloca suas luvas e se prepara para a luta')
            e()
            monstro('Golem de fogo', 400, nome, vida, 4, 16, poupar,100, random.randint(8,16))
            e()
            print('Você ve que de onde o golem veio tinha um buraco e decide entrar nele')
            e()
            t(4.5)
            print('Quando você ve')
            a3b()

          if esc == 'e' :
            a1()
        elif esc == 'm':#morte
          e()
          print('Você tenta bater nele com sua espada, mas')
          e()
          t(1.75)
          print('Infelizmente quando encosta nele ela se derrete,')
          e()
          t(3)
          print('Ele pula em você')
          e()
          t(3.5)
          print('A carne de seu corpo inteiro é derretida pelo slime ')
          e()
          t(6)
          morte()
  elif esc == 'n':
    e()
    print("Ja que você diz, aqui me dispeço")
    e()
    t(2)
    print('Adios :)')
    break
if vida <= 0 :
  print('Seu HP chegou 0')
  e()
  t(2.3)
  morte()
