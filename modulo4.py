#importando uma função do python
import time

#criando uma função para somar
def soma():
    n1 = input("Digite o primeiro número da adição: ")
    n2 = input("Digite o segundo número da adição: ")
    print(n1+n2)

# soma()

#Função exclusiva de soma de dois números
def soma2(n1, n2):
    soma = n1 + n2 
    return soma

#mesmo que o de cima so que abreviado
def soma3(n1, n2):
    return n1 + n2

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite outro número: "))


# print(soma3(num1, num2))

#Chamada da função por argumentos
print(soma3(n2 = 12, n1 = 5))

#Função com parâmetros default (padrão)
def soma4(n1 = 0, n2 = 0):
    return n1 + n2

# print(soma4(50, 25))
# print(soma4())

#Função com apenas alguns valores default
def soma5(n1, n2 = 0):
    return n1 + n2

print(soma5(50, 25)) #Com 2 parametros
print(soma5) #Erro - 0 parametros
print(soma5(34)) #Com 1 parametros
print(soma5(n2= 51, n1 = 12)) #Com parametros invertidos

def soma6(n1, n2):
    if n1 == 1:
        return 1

print(soma6(1, 3)) #True
print(soma6(13, 3)) #None

print(soma6(1,2) + 10) #Mostra 11
print(soma6(2,1) + 10) #Mostra type not supported

