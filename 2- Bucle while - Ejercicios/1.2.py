# Escriba un programa que pregunte una y otra vez si desea terminar el programa, 
# salvo si se contesta exactamente SI (en mayúsculas y sin tilde).

encender = "on"
while(encender =="on"):
    try:
        print("\n\t RESPUESTA WHILE\n")
        diga = str(input("digite 'SI' (con mayusculas) para terminar el programa: "))
        if diga == "SI":
            print(f"\tusted ingresó '{diga}'. hasta pronto\n")
            encender = "off"
    except:
        print("ERROR:")
