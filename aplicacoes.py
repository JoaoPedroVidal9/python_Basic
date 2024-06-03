import time as tp
from random import randint as rd

#Encontrar o maior valor na lista - exemplo 1
lista = [rd(0, 20) for i in range(10)]
print(lista)
mNum = lista[0]

for i in lista:
    if i > mNum:
        mNum = i

print("O maior número da lista é:", mNum)
print("---------------------------------------------")
#Exemplo2

mylist = [rd(0, 20) for i in range(10)]
print(mylist)
maior = mylist[0]

for i in range(len(mylist)):
    if mylist[i] > maior:
        maior = mylist[i]

print("O maior número da lista 2 é:", maior)
print("---------------------------------------------")
#Exemplo3:

uL = mylist[:]
mel = uL[0]
for i in uL[1:]:
    if i > mel:
        mel = i
print("O maior número da lista 3 é:", mel)
print("---------------------------------------------")
#Encontrar a localização de um determinado elemento dentro de uma lista
frutas = ["abacaxi", "maçã", "pêra", "mamão", "uva", "melancia"]
elemento = "melancia"
achado = False

for i in range(len(frutas)):
    achado = frutas[i] == elemento
    if achado:
        break

if achado:
    print("Achou! Índice", i)
else:
    print("nem...")

print("---------------------------------------------")
#Conferidor de jogos de loteria:
sorteados = [5, 11, 9, 42, 3, 49]
apostados = [3, 7, 11, 42, 34, 49]
acertos = 0

for num in sorteados:
    if num in apostados:
        acertos += 1

print(acertos)
print("---------------------------------------------")

#Remoção de números repetidos em uma lista
lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

print("Lista original:", lista)

#lista de apoio
vistos = []

#Iterar pela lista original de trás pra frente
for i in range(len(lista) -1, -1, -1):
    #Se o número já está na lista vistos, removê-lo da lista original
    if lista[i] in vistos:
        del lista[i]
    #Senão, adciona ao final da lista vistos
    else:
        vistos.append(lista[i])
    print("Teste:", i)

#Exibo a lista modificada
print("Lista modificada:", lista)
print("---------------------------------------------")
#Listas avançadas
#2D - Listas Aninhadas Bidimensionais
tabela = [[":(", ":)", ":|", ";-;"], [";-;", ":|", ":)", ":("], [":|", ":)", ";-;", ":("]]

print(tabela[2][2])
print("---------------------------------------------")
#3D - Listas Aninhadas Tridimensionais

cubo = [[[":(", "y", "z"], 
         [":)", "y", "z"],
         [":|", "y", "z"]],
        [["amor", "ódio", "caridade"],
         ["paz", "esperança", "férias"],
         ["tina", "prior", "eve"]],
        [["restinga", "patrocínio", "rifaina"],
         ["amazonense", "fluminense", "santos"],
         ["pizza", "lasanha", "pastel"]]]

print(cubo)
print(cubo[1])
print(cubo[1][2])
print(cubo[1][2][2])

tp.sleep(1)