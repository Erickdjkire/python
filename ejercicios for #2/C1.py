# Escriba un programa que pregunte cuantos números se van a introducir, 
# pida esos números (que puedan ser decimales) y calcule su suma.
encender = "on"
while(encender =="on"):
    try:
        lista = []
        sumador = 0
        print("\n\tSUMA DE NÚMEROS\n")
        ingresa_num = int(input("  cuantos números desea ingresar: ".title()))
        for x in range(1,ingresa_num+1):
            ingrese = float(input(f"{x} / {ingresa_num} - ingrese su número: ".title()).replace(",",".").replace(" ",""))
            lista.append(ingrese)
            sumador+=ingrese
        print(f"\nusted ingresó {lista}\n la suma total de digitos es: {sumador}\n".title().replace(","," - "))
        seguir = str(input("¿desea seguir ingresando números? si/no: ")).lower()
        if seguir == "si":
            print(f"Genial, Usted ingresó '{seguir}', Sigamos!!".title())
        if seguir == "no":
            print(f"hasta pronto. Usted INgresó '{seguir}',Muchas Gracias.".title())
            encender = "off"
        if seguir != "si" and seguir != "no":
           print(f"\nVerificar datos. Usted ingresó '{seguir}', seguimos!!".title())
    except:
        print("ERROR: ")
