# Escriba un programa que pida dos números enteros y escriba la suma 
# de todos los enteros desde el primer número hasta el segundo.

while(True):
    try:
        pide_1 = int(input("ingrese un número entero: "))
        pide_2 = int(input("ingrese otro número entero: "))
        suma = 0
        for x in range(pide_1,pide_2+1):
            print(f"{x}")
            suma+=x
        print(f"\n\testos son los números entre {pide_1} y {pide_2}")
        print(f"\n\tla suma final de los digitos es: {suma}\n\t")
    except:
        print("code ERROR:")