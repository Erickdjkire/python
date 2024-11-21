# Escriba un programa que pida un número entero mayor que cero y calcule su factorial.
# EL FACTORIAL ES LA MULTIPLICACION DE TODOS LOS NUM ENTEROS POSITIVOS HASTA EL.

bucle = "s"
while(bucle == "s"):
    try:
        num = int(input("ingrese un número positivo mayor que cero: "))
        if num <= 0:
            print(f"ERROR: usted ingresó {num}")
        else:
            a = 1
            for x in range(1, num+1):
                a = a * x
            print(f"El factorial de {num} es {a}")
        bucle = str(input("desea ingresar otro número s/n: ")).lower()
    except:
        print("ERROR:")