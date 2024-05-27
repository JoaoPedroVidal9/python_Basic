import time

numeros = [111, 7, 2, 1]

#4
print(len(numeros))

numeros.append (52)

#5
print(len(numeros))

#[111, 7, 2, 1, 52]
print(numeros)

numeros.insert (0, 222)

#6
print(len (numeros))

#[222, 111, 7, 2, 1, 52]
print(numeros)

#[222, 111, 7, 2, 1, 12, 52]
numeros.insert(-1, 12)
print(numeros)

#[222, 18, 111, 7, 2, 1, 12, 52]
numeros.insert(1, 18)
print(numeros)

#[222, 18, 111, 7, 2, 1, 20, 12, 52]
numeros.insert(-2, 20)
print(numeros)

time.sleep(2)