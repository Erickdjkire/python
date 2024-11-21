#Escriba un programa que pida la anchura y altura 
#de un rectángulo y el caracter a utilizar en el dibujo:


anchura = int(input("ingrese el ancho: "))
altura = int(input("ingrese la altura: "))
caracter = str(input("ingrese el caracter a duplicar: "))

for x in range(anchura):
    for y in range(altura):
        print(str(caracter), end="")
    print()