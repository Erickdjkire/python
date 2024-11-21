#  Escriba un programa que pregunte cuántos números se van a introducir, 
# pida esos números, y diga al final cuántos han sido pares y cuántos impares.


bucle = "s"
while(bucle=="s"):
    try:
        print("\n\t PARES E IMPARES\n\t")
        ing = int(input("¿Cuantos números desea Ingresar? "))
        if ing <= 0:
            print(f"ERROR. usted ingresó {ing}")
        else:
            par = 0
            impar = 0
            lista = []
            pares = []
            impares = []
            for x in range(ing):
                ing2 = int(input(f"ingrese número: "))
                lista.append(ing2)
                if ing2 % 2 == 0:
                    par+=1
                    pares.append(ing2)
                else:
                    impar+=1   
                    impares.append(ing2)
            print(f"\n\tlos número(s) ingresado(s) son: {lista}.\n\t\n\t {par} número(s) son pare(s):{pares} \n\t{impar} número(s) son impare(s):{impares} \n\t")
        final = str(input("¿desea ingresar más números? s/n ")).lower()
        

        if final == "s":
            print(f"\n\tingresó '{final}'. Genial, Sigamos\n\t")

        if final == "n":
            print(f"\n\tingresó '{final}'. Programa Terminado, Muchas Gracias\n\t")
            bucle = "exit"

        if final != "n" and final != "s":
            print(f"\n\tingresó '{final}'. no es una opción Valida\n\t")
    except:
        print("ERROR:")