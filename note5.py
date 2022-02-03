import math

def imprima():
	resultado = 15 + 30
	print(resultado)

imprima()

def texto(frase):
	print('ola mundo')

texto('ola para alguem')


def f(x):
	resul = x *2
	return resul

print(f(5))

if f(5) == 7:
	print('verdadeiro')


def soma(x,y):
	return x + y

n_1 = int(input("primeiro numero: "))
n_2 = int(input("segundo numero: "))

print(soma(n_1, n_2))

def conta1():
	return 2+2

def conta2():
	n = conta1() + 5
	return n

print(conta1())
print(conta2())

def sem1(p1, p2):
	media = (p1+p2) /2
	return media

def sem2(p1, p2):
	media = (p1+4*p2) /2
	return media

def ano(a1, a2, a3, a4):
	return (sem1(a1, a2) + sem2(a3, a4)) / 2

n1 = float(input("Primeira nota: "))
n2 = float(input("segunda nota: "))
n3 = float(input("terceira nota: "))
n4 = float(input("quarta nota: "))

print(sem1(n1, n2))
print(sem2(n3, n4))
print(ano(n1, n2, n3, n4))

#########exercicio#1##########

def dobro(x):
	x2 = x * 2
	print(x2)

x = int(input("escolha um numero: "))

dobro(x)

#########exercicio#2##########

def raio(r):
	C = 2*(math.pi)*r
	return C

r = int(input("raio: "))

print(math.ceil(raio(r)))

#########exercicio#3##########

def soma(y,z):
	so = y + z
	print(so)
def subi(y,z):
	su = y - z
	print(su)
def mult(y,z):
    m = y * z
    print(m)
def divi(y,z):
	d = y / z
	print(d)

z = int(input(":"))
y = int(input(":"))

soma(y,z)
subi(y,z)
mult(y,z)
divi(y,z)

#########exercicio#4##########

def nome(n):
	print(f"ola {n} !!")

n = input("seu nome : ")
nome(n)

#########exercicio#5##########

def comprimento():

h= #horario
n= #nome
