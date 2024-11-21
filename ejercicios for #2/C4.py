# Escriba un programa que pida un número entero mayor que cero y calcule su factorial.

encender = "on"
while(encender == "on"):
    try:
        print("\tcalcule su factorial".upper())
        ing =int(input("ingrese un número entero mayor a cero: ".title()))
        if ing<=0:
            print(f"ERROR: usted ingresó '{ing}' ".title())

        else:
            a = 1
            for x in range(a,ing+1):
               a*=x
            print(f"\n\nel factorial de {ing} es: \n\t\t!{ing}: {a}\n\n".title())

            h = str(input("desea seguir ingresando números  si/no: \n".title())).lower()
            if h == "si":
                print(f"genial. usted ingresó '{h}', seguimos!!")

            if h == "no":
                print(f"adios. usted ingresó '{h}', hasta pronto".title())
                encender = "off"

            if h != "si" and h != "no":
                print(f"verifique dato ingresado ('{h}'), seguimos...)".title())



    except:
        print("ERROR:")





