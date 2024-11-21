# Escriba un programa que pida dos números enteros y escriba qué números son pares y 
# cuáles impares desde el primero hasta el segundo.

bucle = "s"
while (bucle == "s"):
    try:
        ing = int(input("ingrese número entero mayor que cero: "))
        ing2 = int(input(f"ingrese otro número entero mayor que {ing}: "))
        if ing <= 0 or ing2 <= ing:
            print(f"Error. usted ingresó {ing}, {ing2}")
        else:
            mi = []
            par = []
            impar = []
            for x in range(ing,ing2+1):
                mi.append(x)
                if x % 2 == 0:
                    print(f" {x} es par")
                    par.append(x)
                else:
                    print(f" {x} es impar")
                    impar.append(x)
            print("\n\tlos numeros desde el ",ing ,"al", ing2,"son: ",mi,"\n\tlos numeros pares son",par,"\n\tlos numeros impares son",impar)
            final = str(input(f"¿desea ingresar más números? s/n: ")).lower()
            if final == "s":
                print(f"Genial. Sigamos: ")
            if final == "n":
                print(f"Ingreso '{final}', Programa terminado, Muchas Gracias.")
                bucle = "fin"
            if final != "s" and final != "n":
                print(f"Error, Usted Ingreso '{final}', Intente Nuevamente: ")
    except:
        print("ERROR:")