import math

D_E =int(input('Dano Elemental: ')) 
Es = int(input('quantidade de estrelas:  '))
af = str(input('afiação: '))
dano_1 = D_E / 10
Q_Es = 0
seila = 0

print(dano_1)

if Es == 1:
    Q_Es =  0.20
elif Es == 2:
    Q_Es = 0.40
elif Es == 3:
    Q_Es = 0.60
elif Es == 4:
    Q_Es = 0.80
elif Es == 5:
    Q_Es = 1.00

print(Q_Es)

if af == 'vermelha' or "verm":
    dano_f = (0.25*dano_1)*Q_Es
if af == 'laranja' or "lar":
    dano_f = (0.50*dano_1)*Q_Es
if af == 'amarela' or "ama":
    dano_f = (0.75*dano_1)*Q_Es
if af == 'verde' or "ver":
    dano_f = (1*dano_1)*Q_Es
if af == 'azul' or "az":
    dano_f = (1.0625*dano_1)*Q_Es
if af == 'branca' or "br":
    dano_f = (1.125*dano_1)*Q_Es
print (math.floor(dano_f))






