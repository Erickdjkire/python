# Escriba un programa que pregunte cuántos números se van a introducir, 
# pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.

switch = "on"
while(switch == "on"):
    try:
        print("\n\tVerificar número no mayor al anterior".upper())
        preg = int(input("\n¿cuantos números va a ingresar? :".title()))
        if preg <= 0:
            print(f"verifique datos. '{preg}' es menor a 1".title())
        else:
            numeros = int(input(f"1/{preg} ingrese un número:"))
            for x in range(1+1,preg+1):
                ing = int(input(f"{x}/{preg} escriba un número no mayor a {numeros}: ".title()))
                if ing < numeros:
                    print(f"efectivamente. {ing} no es mayor a {numeros}.")
                numeros = ing
            fin = str(input("¿desea seguir ingresando números? si/no: ")).lower()
            if fin == "si":
                print(f"genial. usted ingresó '{fin}', seguimos!! \n".title())
            elif fin == "no":
                print(f"adios. usted ingresó '{fin}', hasta luego.'\n".title())
                switch = "off"
            else:
                print(f"\n\tno se comprende '({fin})' como comando. seguimos....\n".title())
    except:
        print("ERROR:")
