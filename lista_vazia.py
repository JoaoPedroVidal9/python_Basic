import time

#lista vazia 1 ---------------------------------------------------------
my_list = [] #Criando uma lista Vazia

#dando valores de indice mais 1 para cada posição
for i in range(5):
    my_list.append(i + 1)

#mostra a lista
print(my_list)


#lista vazia 2 --------------------------------------------------------
my_list2 = []

#inserindo valores de indice mais 1 no início da lista
for i in range(5):
    my_list2.insert(0, i + 1)

#mostra a lista 2
print(my_list2)

#lista vazia 3 --------------------------------------------------------
my_list3 = [10, 1, 8, 3, 5]

total = 0

#somando todos os valores na lista em total
for i in range(len(my_list3)):
    total += my_list3[i] #total = total + my_list3[i]

#mostra a soma total
print(total)

#Teste extra ----------------------------------------------------------
total = 0

for i in my_list3:
    total += i

print(total)

#Reordenando a lista manualmente
# my_list3[0], my_list3[4] = my_list3[4], my_list3[0]
# my_list3[1], my_list3[3] = my_list3[3], my_list3[1]

#Reordenando a lista com for(para qualquer tamanho)
for i in range(len(my_list3) // 2): #len(my_list3) pode ser posto em uma variável anteriormente
    my_list3[i], my_list3[len(my_list3) - i - 1] = my_list3[len(my_list3) - i - 1], my_list3[i]

print(my_list3)

time.sleep(3)