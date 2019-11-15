import time
import random

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

def matou():
  print('Você matou o monstro!!!')

def e():
  print(' ')

def t(p1):
  time.sleep(p1)

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

def errado():
    print('Essa opção não existe, escolha uma opção valida!!!')


espada = 8
punho = 4
vida = 100
##########MONSTROS#############
esqueleto1 = random.randint(10,18)


print('Este sera um jogo de rpg com escolhas, dependendo da sua escolha \nvocê pode morrer ou prosseguir ate seu final e ver o que ira acontecer')
e()
esc = str(input('você deseja começar o jogo?[s/n] '))
nome = input('Qual seria seu nome: ')

while vida > 0 :
  if esc == 's':
    e()
    print('Então vamos embarca em uma jornada inesquecivel .')
    print('..................................................')
    print('Você é um jovem explorador que em sua mochila tem uma espada, em sua busca por uma nova aventura acaba se deparando com a entrada de uma dungeon subterranea.')
    esc = str(input('Você deseja entrar na dungeon? [s/n] '))

    if esc == "s":
      e()
      print("você desce as escadas, começa a ouvir uns barulho estranhos ")
      esc = str(input('Você ira para esquerda , para a direita ou sentar e chorar? [d/e/c] '))

      if esc == 'd':
        print('Você começa a andar em direção a direita.\nAparentimente n tem nada na sala')

      elif esc == 'e':
        print('')

      if esc == 'c':
        e()
        print('Você começa a pensar na sua vida enquanto chora.')
        t(1)
        print('...')
        t(1.75)
        print('...')
        t(1.75)
        print('...')
        t(1.75)
        e()
        print('Um monstro começa a chegar perto.\nVocê se levanta e se prepara para luta!')
        e()
        t(3)
        if 0 == 0:

          while esqueleto1 > 0 :
            print(f'Esqueleto--hp: {esqueleto1}')
            e()
            e()
            print(f'{nome}--hp: {vida}')
            e()
            print('1.Espada\n2.Punhos\n3.Chorar')
            e()
            esc = input('O que você ira fazer ? [e/p/c] ')
            vida = vida - random.randint(4,8)
            if vida <= 0: 
              print('Você morreu!!!')
              exit
            if esc == "e":
              esqueleto1 = esqueleto1 - espada
              print(f'Você deu {espada} de dano ')
            if esc == 'p':
              esqueleto1 = esqueleto1 - punho
              print(f'Você deu {punho} de dano ')
            if esc == 'c' and vida < 100:
              curado = random.randint(8,12)
              vida = vida + curado
              print(f'Você se curou {curado} de vida ')
            elif esc == 'c':
              print('Você não pode chorar no momento')
        print('Você matou o monstro!!!')

    elif esc == "n":
      e()
      print('Você vai em direção a cidade, mas acaba caindo em um buraco.')
      esc = str(input('Você se segura na borda, você ira soltar a borda ou continuar se segurando? [segurar/soltar]'))
      
      if esc == "segurar":#morte
        e()
        morte()
        print('Você fica segurando por alguns segundos, mas você fica cançado e solta, caindo de cabeça no chão e morrer')

      elif esc == "soltar":
        print('Você cai bruscamente encima de um slime, o matando ,mas você continua inteiro')
        print('Você se levanta e vai em direção a porta\nvocê ve um slime.') 
        esc = input('Você pode tentar virar amigo ou mata-lo. [a/m]')

        if esc == 'a':
          print('Você se aproxima dele calmamente')

        elif esc == 'm':
          print('Você tenta bater nele com sua espada,\n mas infelizmente quando encosta nele ela se derrete,\nlogo em seguida ele pula em você fazendo você virar so os osso.')
          e()
          morte()
          



    else:
      print(errado())

  elif esc == 'n':
    e()
    print("Ja que você diz, aqui me dispeço")
    exit
  else:
      print(errado())





