# Escriba un programa que pida un número entero mayor que cero y 
# escriba varias listas de números consecutivos, como indican los ejemplos siguientes:
""" LISTAS A PARTIR DE VALOR
Escriba un número entero mayor que 0: 0
¡Le he pedido un número entero mayor que 0!
LISTAS A PARTIR DE VALOR
Escriba un número entero mayor que 0: 5
[0, 1, 2, 3, 4, 5]
[5, 4, 3, 2, 1, 0]
[1, 2, 3, 4]
[4, 3, 2, 1]
[0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]"""

encendido = "on"
while(encendido == "on"):
    try:
        

        print("\n\n\tnúmero entero en listas\n".upper())
        ing = int(input("ingrese un número entero mayor a cero: ".title()))
        lista = []
        if ing <= 0:
            print(f"error. ingresó ('{ing}') debe escribir un número mayor a cero.".title())
     
        else:
            for x in range(0,ing+1):

                lista.append(x)
            for y in range(ing-1,-1,-1):
                lista.extend([y])

            print(list(range(0,ing+1)))
            print(list(range(ing,-1,-1)))
            print(list(range(1,ing)))
            print(list(range(ing-1,0,-1)))
            print(lista)
            print(list(range(ing)) + list(range(ing, -1, -1)))

        seguir = str(input("¿desea seguir con el programa? si/no: ")).lower()
        if seguir == "si":
            print(f"genial. usted ingresó '{seguir}'. seguimos".title())
        elif seguir == "no":
            print(f"adios. usted ingresó '{seguir}'. hasta luego.\n\n".title())
            encendido = "off"

        elif seguir != "si" and seguir != "no":
            print(f"no se reconoce a '({seguir})'como instrucción. . continuamos...".title())
            


    except:
        print("ERROR:")