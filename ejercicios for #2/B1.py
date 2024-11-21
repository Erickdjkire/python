# Escriba un programa que pregunte cuántos números se van a introducir, 
# pida esos números y escriba cuántos negativos ha introducido.

bucle = "yes"
while(bucle=="yes"):
    try:
        print("\n\tNUMEROS POSITIVOS Y NEGATIVOS\n\t")
        ing = int(input("¿Cuantos números deseas Ingresar? "))
        if ing <= 0:
            print(f"ERROR. ingresaste {ing}")
        else:
            neg = 0
            pos = 0
            lista = []
            for x in range(ing):
                ing2 = int(input("ingrese número: "))
                lista.append(ing2)
                if ing2 < 0:
                    neg+=1
                else:
                    pos+=1
            print(f"ingresaste {neg} número(s) negativo(s) y {pos} número(s) positivo(s)")
            print(f"ingresaste {lista}")
        bucle = str(input("¿deseas ingresar más numeros? yes/no: ")).lower()
        if bucle != "yes":
            print(f"\n\tIngresó '{bucle}'. Muchas Gracias, Adios \n\t")
        else:
            print(f"\n\tIngresó '{bucle}'. Sigamos!!. \n\t")
    except:
        print("ERROR:")
