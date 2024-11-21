
# Escriba un programa que pida un número entero mayor que 1 
# y que escriba si el número es un número primo o no.

while (True):
    try:
        ing = int(input("ingrese número entero mayor que 1: "))
        if ing < 1:
            print("número errado.")

        else:
            contador = 0
            for x in range(1,ing+1):
                
                if ing % x == 0:
                    contador = contador + 1
            if contador == 2:
                print(f" {ing} es número Primo")

            else:
                print(f" {ing} no es número Primo")

                

    except:
        print("ERROR:")

