import time
largest_number = -99999999
counter = 0

number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

#Esse continue dentro do while jamais será executado

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Insira um número ou digite -1 para finalizar o programa: "))

if counter:
    print("O maior número é",  largest_number)
else:
    print("Você não tem inseriu qualquer número.")


time.sleep(2)