# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números, 
# y muestre un mensaje cada vez que un número no sea mayor que el primero.
switch = "on"
while (switch=="on"):
    try:
        print("\n\n\tmayor al primero".upper())
        ing = int(input("¿cuantos números desea ingresar? ".title()))
        if ing <= 0:
            print("IMPOSIBLE!!", f"usted ingresó {ing}.".lower())


        else:

            ing2 = int(input(f"{1}/{ing} ingrese un número: ".title()))
            for x in range(1,ing):
                ing3 = int(input(f"{x+1}/{ing} ingrese un  mayor a {ing2}: ".title()))
                if ing3 < ing2:
                    print(f"\terror. {ing3} no es menor que {ing2}".title())

            ingresar = str(input("¿desea seguir ingresando números? si/no: ".title()))
            if ingresar == "si":
                print(f"genial. usted ingreso '{ingresar}'. seguimos!!".title())
            if ingresar == "no":
                print(f"adios. usted ingresó '{ingresar}'. hasta pronto.\n\n".title())
                switch = "off"
            elif ingresar != "si" and ingresar != "no":
                print(f"\tverifique comando. usted ingresó '{ingresar}', continuamos...".title())

    except:
        print("ERROR:")