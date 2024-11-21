# Escriba un programa que pida la anchura 
# y altura de un rectángulo y lo dibuje con caracteres producto (*):



anchura = int(input("Ancho del rectángulo: "))
altura = int(input("Alto del rectángulo: "))

for i in range(altura):
    for j in range(anchura):
        print("* ", end="")
    print()
