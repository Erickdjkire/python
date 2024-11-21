# Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.



while(True):
    try:

        numero = int(input("Ingrese un número entero mayor que cero: "))

        if numero > 0:
            y = 1
            for x in range(y,1000):

                if numero % x == 0:

                 print(x, end=", ")


        else:
            print("Número ingresado no es mayor que cero. intente nuevamente")
    except:
        print("Error: ")
