import time

def hi_everybody(lista):
    for name in lista:
        print("Oi", name)

hi_everybody(["Tina", "Gabi", "Jão"])

def criar_lista(n):
    lista = []
    for i in range(n):
        lista.append(i)
    return lista
 
print(criar_lista(10))

def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list
 
foo = [1, 2, 3, 4, 5]
print(list_updater(foo))

global a
a = 1
def fun():
    a = 2
    print(a)
 
fun()
print(a)



time.sleep(3)