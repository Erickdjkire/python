# Escriba un programa que pida dos números enteros y escriba la suma 
# de todos los enteros desde el primer número hasta el segundo.

encender = "on"
while(encender=="on"):
    try:
        uno = int(input(f"ingrese un numero entero: ".title()).replace(",","").replace(".",""))
        dos = int(input(f"ingrese un numero entero mayor que el anterior: ".title()).replace(",","").replace(".",""))
        if dos < uno:
            print(f"ojo. {dos} no es mayor que {uno}".title())
        else:
            lista = []
            suma=0
            for y in range(uno,dos+1):
             lista.append(y)
             suma+=y
            print(lista)
            print("\tla suma de los siguitos son:",suma)
            fin = str(input("\n\t¿desea ingresar más números? si/ no: \n")).lower()
            if fin == "si":
                print(f"Genial, usted ingresó '{fin}', Vamos!!\n".title())
            if fin =="no":
                print(f"usted ingresó '{fin}', hasta luego\n".title())
                encender = "off"
            if fin !="si" and fin != "no":
                print(f"comando invalido, ingresó '{fin}', seguidos...".title())
    except:
        print("ERROR: ")