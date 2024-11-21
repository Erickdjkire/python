
whilee = "si"
while whilee == "si":
    try:
        tiempo = str(input("¿afuera llueve? ")).lower()
        if tiempo == "si":
            lluvia = str(input("¿llueve muy fuerte? ")).lower()
            if lluvia == "si":
                print(f"ingresaste '{lluvia}' recuerda llevar: \nparaguas\nbotas\nropa abrigada")
            else:
                print(f"ingresaste '{lluvia}' disfruta la llovizna. recuerda llevar paraguas.")
        else:
            frio = str(input("hace frio afuera? ")).lower()
            if frio == "si":
                print ("debes abrigarte y llevar gorro")
            else:
                sol = str(input("¿hay mucho calor? ")).lower()
                if sol == "si":
                    print ("recuerda usar protector solar")
                else: 
                    print("entonces lleva ropa lijera y disfruta el día")
        respuesta = str(input(("¿deseas iniciar nuevamente? si/no: "))).lower()
        if respuesta == "no":
            print(f"usted ingresó '{respuesta}', Hasta pronto. Gracias.'")
            break
        if respuesta == "si":
            print(f"usted ingresó '{respuesta}', Genial, seguimos.'")
        if respuesta != "si" and respuesta != "no":
            print(f"\n\tno entiendo tu respuesta. ingresaste {respuesta}. por lo que seguiremos.\n\t")
    except:
        print("ERROR:")




    