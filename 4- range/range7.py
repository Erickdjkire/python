# Escriba un programa que pida dos números enteros (el segundo mayor que el primero) 
# y escriba varias listas de números consecutivos, como indican los siguientes ejemplos:
"""
LISTAS ENTRE DOS NÚMEROS
Escriba un número entero: 5
Escriba otro número entero mayor que 5: 11
[5, 6, 7, 8, 9, 10, 11]
[10, 9, 8, 7, 6, 5]
[6, 7, 8, 9, 10, 11, 12]
[10, 9, 8, 7, 6]
[5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5]

LISTAS ENTRE DOS NÚMEROS
Escriba un número entero: -2
Escriba otro número entero mayor que -2: 3
[-2, -1, 0, 1, 2, 3]
[2, 1, 0, -1, -2]
[-1, 0, 1, 2, 3, 4]
[2, 1, 0, -1]
[-2, -1, 0, 1, 2, 3, 2, 1, 0, -1, -2]
"""

encender = "on"
while(encender == "on"):
    try:
        print("\n\n\tlistas concecutivas con range".upper())
        ing = int(input("ingrese un número entero: ".title()))
        ing2 = int(input(f"ingrese un número mayor a '{ing}': ".title()))
        if ing2 < ing:
            print(f"error. '{ing2}' no es mayor a '{ing}'. ".title())

        else:
            print(list(range(ing,ing2+1)))
            print(list(range(ing2-1,ing-1,-1)))
            print(list(range(ing+1,ing2+2)))
            print(list(range(ing2-1,ing,-1)))
            print(list(range(ing,ing2+1)) + list(range(ing2-1,ing-1,-1)))


        end = str(input("\n¿desea finalizar el programa? si/ no : ".title())).lower()
        if end == "si":
            print(f"\n\tadios, usted ingresó '{end}', hasta pronto.\n\n".title())
            encender = "off"

        elif end == "no":
            print(f"genial. usted ingresó '{end}'. seguimos!!".title())

        else:
            print(f"no se reconoce a '({end})' como instrucción. continuamos...".title())
            



    except:
        print("ERROR:")
