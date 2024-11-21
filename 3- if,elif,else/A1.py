# Escriba un programa que pida primero un número par y luego un número impar (positivos o negativos)
# En caso de que uno o los dos valores no sea correcto, se mostrará un único aviso.
encender ="on"
contador = 0
while(encender =="on"):
    try:
        print("\n\tPAR O IMPAR")
        
        ing1 = int(input("Ingrese un número par: ".title()))
        ing2 = int(input("ingrese un número impar: ".title()))
        
        if ing1 % 2 == 0:
           print(f"excelente. '{ing1}'. es par".title())
        else:
            contador +=1
            print(f"*****error. '{ing1}' no es par.".title())
            if contador == 1:
               print(f"\n\taviso. si tiene error nuevamente se terminará el programa.".title())


        if ing2 % 2 != 0:
           print(f"excelente. '{ing2}' es impar".title())

        else:
            contador +=1
            print(f"*****error. '{ing2}' no es impar.".title())
            if contador == 1:
               print(f"\n\taviso. si tiene error nuevamente se terminará el programa.".title())


        if contador == 2:
            encender = "off"
            print("\n\n\tusted ingresó el maximo de intento erroneos permitidos, hasta pronto.\n\n".title())


        


    except:
        print("ERROR:")