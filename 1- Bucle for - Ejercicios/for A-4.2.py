# Escriba un programa que pregunte cuántos números se van a introducir, 
# pida esos números, y muestre un mensaje cada vez que un número no sea mayor que el anterior.

switch = "on"
while(switch == "on"):
    try:
        ing = int(input("\n\n¿cuantos números desea ingresar? : ")) 
        if ing <= 0:
            print(f"error. ingresó {ing}")

        else:

            num = int(input(f"1/{ing} ingrese un número: "))
            for x in range(1,ing):
                num2 = int(input(f"{x+1}/{ing} ingrese un número mayor a {num}: "))
                if num2 < num:
                
                    print(f"ojo. {num2} no es mayor a {num}")
                num = num2

            
            fin = str(input("¿desea seguir ingresando números? si/no: ")).lower()
            if fin == "si":
                print(f"genial. usted ingresó '{fin}'. seguimos!!\n".title())

            if fin == "no":
                print(f"adios, usted ingresó '{fin}'. hasta luego.\n".title())
                switch = "off"

            elif fin != "si" and fin != "no":
                print(f"\tverifique. usted ingresó ('{fin}'). continuemos...\n".title())




    except:
        print("ERROR:")