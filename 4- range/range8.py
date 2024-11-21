
# Escriba un programa que pida dos números enteros y escriba la lista de números 
# consecutivos de uno a otro, en orden creciente o decreciente.

switch = "on"
while(switch == "on"):
    try:

        ing = int(input("ingrese un número entero: ".title()))
        ing2 = int(input("ingrese otro número entero: ".title()))

        if ing < ing2:
            print(list(range(ing,ing2+1,1)))

        elif ing > ing2:
            print(list(range(ing,ing2-1,-1)))


    except:
        print("ERROR:")