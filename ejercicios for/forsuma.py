# Escriba un programa que pregunte cuantos números se van a introducir, 
# pida esos números (que puedan ser decimales) y calcule su suma.

while(True):
    try:
        ing = int(input("¿cuantos números desea ingresar? "))
        if ing <= 0:
            print(f"{ing} esto es imposible. ")

        else:
            suma = 0
            for x in range(1, ing+1):
                num = float(input("ingrese número entero o decimal: "))
                suma+=num

        print(f"la suma de todos los digitos es {suma} ")

    except:
        print("Code Error")
