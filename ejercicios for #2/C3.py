#Escriba un programa que pregunte cuántos números se van a introducir, 
#pida esos números, y escriba el mayor, el menor y la media aritmética.

# * Se recuerda que la media aritmética de un conjunto de valores es 
# la suma de esos valores dividida por la cantidad de valores.


encender = "on"
while(encender=="on"):
    try:
        print("\n\tmedia aritmética".upper())
        ing = int(input("¿cuantos números desea ingresar? ".title()))
        a = 0
        numeros = 0
        acumulador = []
        while(a<ing):
            a+=1
            ingrese = float(input(f"{a}/{ing} ingrese número: ").title().replace(",","").replace(".",""))
            acumulador.append(ingrese)
            s = str(acumulador).replace("[","").replace("]","")
            numeros+=ingrese
            media = numeros//ing
            maximo = max(acumulador)
            minimo = min(acumulador)
        print(f"\n\tel número mayor ingresado es: '{maximo}'\n\tel número menor ingresado es: '{minimo}'".title())
        print(f"la media de los números ingresados es: '{media}'".title())
        print(f"\tlos números ingresados son: {s}".title())
        final= str(input("\n\n¿desea seguir ingresando números? si/no:\n\n".title())).lower()
        if final == "si":
            print(f"\tGenial, usted ingresó '{final}', Seguimos!!".title())
        if final == "no":
            print(f"\tAdios, usted ingresó '{final}', hasta pronto.".title())
            encender = "off"
        if final != "si" and final != "no":
            print(f"\tVerifique, usted ingresó '{final}', Seguiremos...".title())
    except:
        print("ERROR, verifique información")