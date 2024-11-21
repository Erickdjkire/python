# Escriba un programa que pregunte una y otra vez si desea continuar con el programa, 
# siempre que se conteste exactamente sí (en minúsculas y con tilde).

encender = "sí"
while (encender == "sí"):
    try:
        print("\n\tCONTUNIAR CON BUCLE WHILE\n")
        resp = str(input(" Responda 'sí' (en minusculas y tílde) si Desea Continuar Con El Programa."))
        if resp == "sí":
           encender == "sí"
        if resp != "sí":
            print(f"Usted Ingresó '{resp}', Adios.")
            encender = "no"
    except:
        print("ERROR:")
