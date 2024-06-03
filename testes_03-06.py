import time as tp

# #Biblioteca para retornar um número inteiro aleatório 
# from random import randint as rd

# # sort = rd(-100, 100) #Sorteia um número de -100 a 100

# #Criando uma lista de números inteiros aleatórios
# lista = [rd(1, 6) for i in range(1, 11)]

# lista2 = [x for x in range(1,11)]

# lista3 = ["Rolo compressor!!!" for f in range(1,4)]

# # print(lista)
# # print(lista2)
# # print(lista3)

# #criando lista par
# # par = [i for i in range(10) if i % 2 == 0]
# # impar = [i for i in range(10) if i % 2 == 1]

# # print(par)
# # print(impar)

# #Povoando uma lista com input
# #listaU = [int(input("Digite um número: ")) for p in range(5)]

# # print(listaU)

# #Utilizando o metodo split(cada palavra se torna um elemento da lista)
# # nome = "mickey mouse"
# # print(nome)
# # print(nome.split())

# #aplicando o split com o input
# # notas = [n for n in input("Notas: ").split()]
# # print(notas)

# #Exemplo com float:
# # notas2 = [float(n) for n in input("Notas: ").split(",")]
# # print(notas2)

# #Lista com tipos diferentes de dados
# listaM = [17, 70.5, "Sem Mundial", True]
# # print(listaM)

# #Manipulação / Fatiamento de listas
# veiculos1 = ['carro', 'bicicleta', 'motor']
# print('Veículos:', veiculos1)

# #Copiando todo o conteúdo de uma lista para outra
# veiculos2 =veiculos1[:]
# del veiculos1[2]
# print('Veículos:', veiculos1)
# print('Veículos 2:', veiculos2)

# #Copiando parte do conteúdo de uma lista
# veiculos3 = veiculos2[0:2]
# print(veiculos3)

# #Copiando parte do conteúdo, incluindo o último elemento
# veiculos4 = veiculos2[0:-1]
# print(veiculos4)

# veiculos5 = veiculos2[-1:1]
# print(veiculos5)

#Outras maneiras de fatiamento(omissão do start ou do end)
my_list = ["A", "B", "C", "D", "E", "F"]
print(my_list)
new_list = my_list[:3]
print(new_list)
new_list2 = my_list[3:]
print(new_list2)

#Apagando conteúdo de listas
del my_list[1:3]
print(my_list)
del my_list[:]
print(my_list)
del my_list

#Testando se alguns itens existem em uma lista ou não 
#Para isso, usamos palavras chave in e not in
naosei = ["A", "B", 18, 15]
print("A" in naosei)
print("C" not in naosei)
print(15 not in naosei)

tp.sleep(1)