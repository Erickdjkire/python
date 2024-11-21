# Escriba un programa que pregunte cuántos números se van a introducir, 
# pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el primero.

bucle = "yes"
while (bucle=="yes"):
    try:
        ing = int(input("¿cuantos números desea ingresar? "))
        if ing <=0:
            print(f"Error, Usted ingresó {ing}")
        else:
            a = 1
            ing1 = int(input(f"ingrese un número: "))
            for x in range(a,ing):
                a+=1
                ing2 = int(input(f"ingrese un número mayor que {ing1}: "))
                if ing2 < ing1:
                    print(f"ojo. {ing2} no es mayor que {ing1}")
        bucle = str(input("¿deseas seguir ingresando números? yes/no: ")).lower()
        if bucle != "yes":
            print(f"ingresaste '{bucle}', Muchas Gracias, Adios.")
    except:
        print("ERROR:")
