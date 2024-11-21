# Escriba un programa que pida un número entero mayor que 1 y que escriba si el número es un número primo o no.
# numero primo es:
# un numero natural
# mayor que 1
# divisible solo por si mismo y 1

print("\n\tVERIFICADOR DE NÚMERO PRIMO\n")
              # inicio bucle general del programa
bucle = "si"
while(bucle=="si"):
    try: # excepcion de error en caso de introducir datos falsos o erroneos.
        ingreso = int(input("Favor: Ingrese Número a verificar: ".title()).replace(".","").replace(",","")) # ingrese datos además reemplaza comas y puntos
        a = 0 # a comienza en 0
        contador = 0 # contador en cero

              # inicio bucle de funcion
        while (a < ingreso): #bucle while recorerá desde a (0) hasta número ingresado
            a+=1 # cada vez que pasa por while, a aunmenta un número. asi llegará hasta el ingresado y parará.
            if ingreso > 1: # se ejecuta si el número ingresado es mayor que 1
                if ingreso % a == 0: # se ejecuta si el numero ingresado dividido por cada numero es igual a 0  
                    contador = contador + 1 # cada vez que se ejecute lo anterior contador sumará 1
                    if contador == 2: # se ejecuta solo si contador es igual a 2
                        if a == ingreso: # se ejecita si el numero de salida es igual al ingresado.
                            print(f"Felicidades, {ingreso} es Número PRIMO.") # imprime si se ejecuta la condicion anterior.
                        else:
                            print(f" Lamentablemente, {ingreso} no es Número primo") # si el número ingresado no cumple la condicion se imprimirá el mensaje.

                                       # finalizar programa
                        insertar = str(input("\n¿desea ingresar más números? si/no: \n"))
                        if insertar == "si":
                            print(f"\n\t Usted ingresó '{insertar}' Genial, Seguimos")
                        if insertar == "no":
                            print(f"\n\t Adios, Usted ingresó '{insertar}'. Hasta Pronto")
                            bucle ="off"
                        if insertar != "si" and insertar != "no":
                            print(f"\n\t No entiendo, Usted ingresó '{insertar}'. Seguimos!!")
    except:
        print("ERROR:verifique datos Ingresados") #excepcion de errores, el programas no se caerá.







        

