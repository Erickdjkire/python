# pregunta cuantos datos vas a ingresar, guardalos en una lista y al final muestralos
respuesta = "si"
while (respuesta == "si"):
    try:
        my_array = []
        num = int(input("¿cuantos datos vas a ingresar? " ))
        for x in range(num):
            ing = str(input("ingresa dato: "))
            my_array.append(ing)

        print(f"\ttus datos son:\t\n{my_array}\t\n")

        respuesta = str(input("¿deseas continuar? escribe si: "))


    except:
        print("ERROR: ")