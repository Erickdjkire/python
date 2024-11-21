# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números,
#  y muestre un mensaje cada vez que un número no sea mayor que el anterior.

bucle = "si"
while(bucle == "si"):
    try:
        ing = int(input("¿Cuantos números deseas ingresar? "))
        if ing <= 0:
            print(f"ERROR. ingresaste {ing} ")
        else:
            x = 0
            los = int(input("ingresa un número: "))
            for x in range(ing):
                ing2 = int(input(f"ingresa un número mayor que {los}: "))
                
                if ing2 <= los:
                    print(f"\tEy!! {ing2} no es mayor que {los}.")
                los = ing2
        bucle = str(input("¿deseas seguír ingresando números? si/ no: ")).lower()
        if bucle != "si":
            print(f"\n\tingresaste '{bucle}', Programa finalizado. Muchas Gracias\n\t")
    except:
        print("ERROR:")