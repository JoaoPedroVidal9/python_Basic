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

#Exemplo2

mylist = [rd(0, 20) for i in range(10)]
print(mylist)
maior = mylist[0]

for i in range(len(mylist)):
    if mylist[i] > maior:
        maior = mylist[i]

print("O maior número da lista 2 é:", maior)

#Exemplo3:

uL = mylist[:]
mel = uL[0]
for i in uL[1:]:
    if i > mel:
        mel = i
print("O maior número da lista 3 é:", mel)

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

tp.sleep(1)