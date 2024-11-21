# Escriba un programa que pida dos números enteros y escriba qué números son pares 
# y cuáles impares desde el primero hasta el segundo.

encender = "on"
while(encender=="on"):
    try:
        print("\n\tverificar números pares\n".upper())
        ing1 = int(input("ingrese un númnero entero: \n".title()))
        ing2 = int(input(f"ingrese otro número entero mayor a {ing1}: \n".title()))
        if ing1 > ing2:
            print(f"verifique datos. {ing2} es menor que {ing1}.".title())
        else:
            for x in range(ing1, ing2+1):
                if x % 2 == 0:
                    print(f"el número: {x}, es par".title())
                else:
                    print(f"el número: {x}, no es par".title())
            fin = str(input("\n\t¿desea seguir ingresando números? si/no:\t\n".title())).lower()
            if fin == "si":
                print(f"genial. usted ingresó: '{fin}', vamos!!".title())
            if fin == "no":
                print(f"adios. usted ingresó: '{fin}', hasta luego\n\n\n".title())
                encender = "off"
            if fin != "si" and fin != "no":
                print(f"verifique dato ingresado. usted ingresó ('{fin}') continuamos...".title())
    except:
        print("ERROR:\n")