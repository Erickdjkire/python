# Escriba un programa que pida un número entero mayor que 1 y que escriba si el número es un número primo o no.
# ingresa % x == 0

bucle = "si"
while (bucle == "si"):
    try:
        print("\tVERIFICA NÚMERO PRIMO\n\n")

        ingresar = int(input("ingrese un número entre 2 y 10.000: ").replace(",","").replace(".",""))
        if ingresar <=1 or ingresar > 10000:
            print(f"ERROR. usted ingresó {ingresar} Intente Nuevamente.")

        else:
            acumulador = 0
            for x in range(1, ingresar+1):
                if ingresar % x == 0:
                    acumulador+=1
            if acumulador == 2:
                print(f"Felicidades. {ingresar} es un número primo")

            else:
                print(f"Lamentablemente. {ingresar} NO es un número primo")


            final = str(input("\n\t¿desea seguir ingresando números? si/no: ").lower())
            if final == "si":
                print(f"Genial. ingresaste {final}. Sigamos!!")

            if final == "no":
                print(f"\n\tHasta Pronto, Usted Ingresó {final}. ADIOS!!\n\t")
                bucle = "final"

            if final != "si" and final != "no":
                print(f"Usted Ingresó {final}. que no se reconoce. Seguimos!!")

    except:
        print("ERROR:")