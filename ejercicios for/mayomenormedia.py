# Escriba un programa que pregunte cuántos números se van a introducir, 
# pida esos números, y escriba el mayor, el menor y la media aritmética.

bucle = "s"
while (bucle == "s"):
    try:
        a = 0
        a=0
        
        num = int(input("¿cuantos números desea ingresar? "))
        if num <= 0:
            print("Estas en un error")
        else:
            lista = []
            for x in range(a,num):
                ing = int(input("ingrese número: "))
                lista.append(ing)
                a += ing  
            print(f"\n\tlos números fueron {lista} \n\tel número mayor es: {max(lista)}\n\tel menor es: {min(lista)}\n\tla suma de los números es {a} \n\tla media es {a/num}")
            bucle = str(input("desea continuar s/n: "))
    except:
        print("Error")