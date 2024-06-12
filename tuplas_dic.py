import time

tupla = tuple()

tupla = (1)

tupla = (2)

tupla = 1, 2, 3

print(tupla)

print(tupla[1])

# tupla[0] = 100 #Erro, não é possível alterar uma tupla

#Manipulando dicionários
dic = {"semMundial":"Palmeiras", "1Mundial":"Corinthians", "2Mundiais":"SãoPaulo"}

print(dic["semMundial"])

notas = {"mat":5, "lp":10, "ef":8}

print(notas["lp"])

print(dir(notas))

print(notas.values())

print(notas.keys())

print(len(notas))

for disciplina in notas.keys():
    print(disciplina)


time.sleep(3)