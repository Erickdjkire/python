# Escriba un programa que pida un número entero y 
# escriba una lista de números consecutivos del 0 al valor dado.

encendido = "on"
while(encendido == "on"):
    try:

        print("\n\n\tlista range\n".upper())

        ing = int(input("ingrese un número entero: ".title()))
        lista = []
        if ing >= 0:
            for x in range(0,ing+1):

                lista.append(x)
            print(lista)
        else:
            for x in range(0,ing-1,-1):
                lista.append(x)
            print(lista)

        ending = str(input("¿desea ingresar más números? si/no: ")).lower()
        if ending == "si":
            print(f"genial. usted ingresó '{ending}'. seguimos!!".title())
        elif ending == "no":
            print(f"adios. usted ingresó '{ending}'. hasta luego".title())
            encendido = "off"

        elif ending != "si" and ending != "no":
            print(f"'({ending})'. no se reconoce como instruccion. seguimos...".title())




        
    except:
        print("ERROR:")