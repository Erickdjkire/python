
ancho = int(input("ingrese el ancho: "))

for i in range(1, ancho + 1):
    for j in range(i):
        print("* ", end="")
    print()

for i in range(1, ancho):
    for j in range(ancho - i):
        print("* ", end="")
    print()
