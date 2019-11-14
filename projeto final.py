import time
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
esqueleto1 = 17

print(""" 

 _                            _           _                           _                                               _____       _   _                 
 | |                          (_)         | |                         | |                                      ___    |  __ \     | | | |                
 | |__   ___ _ __ ___   __   ___ _ __   __| | ___     __ _  ___     __| |_   _ _ __   __ _  ___  ___  _ __    ( _ )   | |__) |   _| |_| |__   ___  _ __  
 | '_ \ / _ \ '_ ` _ \  \ \ / / | '_ \ / _` |/ _ \   / _` |/ _ \   / _` | | | | '_ \ / _` |/ _ \/ _ \| '_ \   / _ \/\ |  ___/ | | | __| '_ \ / _ \| '_ \ 
 | |_) |  __/ | | | | |  \ V /| | | | | (_| | (_) | | (_| | (_) | | (_| | |_| | | | | (_| |  __/ (_) | | | | | (_>  < | |   | |_| | |_| | | | (_) | | | |
 |_.__/ \___|_| |_| |_|   \_/ |_|_| |_|\__,_|\___/   \__,_|\___/   \__,_|\__,_|_| |_|\__, |\___|\___/|_| |_|  \___/\/ |_|    \__, |\__|_| |_|\___/|_| |_|
                                                                                      __/ |                                   __/ |                      
                                                                                     |___/                                   |___/                       

""")
print('Este sera um jogo de rpg com escolhas, dependendo da sua escolha \nvocê pode morrer ou prosseguir ate seu final e ver o que ira acontecer')
print(' ')
esc = str(input('você deseja começar o jogo?[s/n] '))

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
        e()
        print('Um monstro começa a chegar perto.\nVocê se levanta e se prepara para luta!')
        e()
        t(3)
        while esqueleto1 > 0 :
          print(f'Esqueleto--hp:{esqueleto1}')
          e()
          print('1.Espada\n2.Punhos\n3.Chorar')
          e()
          esc = input('O que você ira fazer ? [e/p/c]')
          if esc == "e":
            esqueleto1 = esqueleto1 - espada
            print(f'Você deu {espada} de dano ')
          elif esc == 'p':
            esqueleto1 = esqueleto1 - punho


          

    elif esc == "n":
      e()
      print('Você vai em direção a cidade, mas acaba caindo em um buraco.')
      esc = str(input('Você se segura na borda, você ira soltar a borda ou continuar se segurando? [segurar/soltar]'))
      
      if esc == "segurar":#morte
        e()
        morte()
        print('Você fica segurando por alguns segundos, mas você fica cançado e solta, caindo de cabeça no chão e morrer')

      elif esc == "soltar":
        print('Você cai bruscamente ensima de um slime, o matando ,mas você continua inteiro')
        print('')

    else:
      print(errado())

  elif esc == 'n':
    e()
    print("Ja que você diz, aqui me dispeço")
    exit
  else:
      print(errado())
