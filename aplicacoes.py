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







tp.sleep(1)