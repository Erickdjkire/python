# Escriba un programa que pregunte una y otra vez si desea terminar el programa, 
# siempre que se conteste exactamente N (en mayúsculas).

encender = "on"
while(encender == "on"):
    try:
        print("\n\tBUCLE WHILE")
        ing = str(input("¿desea seguir con el programa?".title()+"'N' (en mayusculas) "+"para salir: ".title()))
        if ing =="N":
            print(f"Adios. usted ingresó".title()+"'N'"+", hasta luego\n\n".title())
            encender = "off"
        else:
            print(f"usted ingresó '{ing}', seguimos!!".title())
    except:
        print("ERROR:")