# Mejore el programa anterior haciendo que el programa escriba la suma realizada

print("\tSuma de digitos".upper())
encender = "on"
while(encender == "on"):
    try:
        ing = int(input("ingrese número entero: ".title()).replace(",","").replace(".",""))
        ing2 = int(input(f"ingrese un número entero mayor que '{ing}' : ".title()).replace(",","").replace(".",""))
        if ing2 < ing:
            print(f"verifique. usted ingresó {ing} pero luego {ing2} que no es mayor.")
        else:
            lista = []
            suma = 0
            for x in range(ing, ing2+1):
                lista.append(x)
                a = str(lista).replace("[","").replace("]","")
                b = a.replace(","," +").replace("'","")
                suma+=x
            print(f"\n{b}")
            print(f"\tla suma de ellos es {suma}")
            ingreso = str(input("¿desea ingresar más números? si/no: ".title())).lower()
            if ingreso == "si":
                print(f"Genial. ingresó '{ingreso}', Seguimos!!".title())
            if ingreso == "no":
                encender = "off"
                print(f"\n\thasta luego. usted ingresó '{ingreso}',nos vemos.\n\n\n ".title())
            if ingreso != "si" and ingreso != "no":
                print(f"respuesta no valida. usted ingresó '{ingreso}', continuamos...".title())
    except:
        print("*****ERROR*****")