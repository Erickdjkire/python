# Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

switch = "on"
while(switch == "on"):
    try:
        print("negativos introducidos".upper())

        ing = int(input("¿cuantos números desea ingresar? : ".title()))
        negativo = 0
        for x in range(ing):
            ingrese = int(input(f"{x+1}/{ing} ingrese un número : "))
            if ingrese < 0:
                negativo += 1 
                print(f"Usted ingresó {ingrese}, lleva {negativo} números negativos ingresados.".title())
        print(f"\t en total '{negativo}' número(s) negativo(s) fueron ingresados.".title())
        fin = str(input("¿desea seguir ingresando números? si/no : ".title()))
        if fin == "si":
            print(f"genial. ingresó '{fin}'. seguimos!!\n")
        elif fin == "no":
            print(f"adios. usted ingresó '{fin}'. hasta pronto.\n")
            switch = "off"

        else:
            print(f"\n\tno se reconoce '({fin})' como instrucción. continuamos...\n")
            



    except:
        print("ERROR:")