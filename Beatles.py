# etapa 1

beatles = []

print("Etapa 1:", beatles)

# etapa 2

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Etapa 2:", beatles)

# etapa 3

for i in range(2):
    beatles.append(input(f"Digite o {i + 1}° membro extra dos Beatles:"))

print("Etapa 3:", beatles)


# etapa 4

for i in range(2):
    del beatles[-1]

print("Etapa 4:", beatles)

# passo 5

beatles.insert(0, "Ringo Starr")

print("Etapa 5:", beatles)



# testando o tamanho da lista

print("Os fabulosos", len(beatles))

