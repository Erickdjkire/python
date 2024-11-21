# Escriba un programa que pida primero un número par (positivo o negativo) y si el valor no es correcto, muestre un aviso. 
# Si el valor es correcto, pedirá un número impar (positivo o negativo) y si el valor no es correcto, mostrará un aviso.

encender = "on"
while (encender == "on"):
    try:
        print("\n\tPAR E IMPAR CICLO\n AYUDA:\nlos números pares son números divisibles al 2. dejando sobrante 0\n\n")

        ing = int(input("ingrese número par: ".title()))
        

        if ing % 2 !=0:
            print(f"***** incorrecto. porque '{ing}' no es par.".title())

        else:
            print(f"correcto. '{ing}'. es par")
            ing2 = int(input("ingrese un número impar: ".title()))
            if ing2 % 2 == 0:
                print(f"***** incorrecto. porque '{ing2}' no es impar".title())

            else:
                print(f"correcto. '{ing2}'. es impar.")


    except:
        print("ERROR:")