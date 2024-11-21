# Escriba un programa que pida dos números enteros y escriba qué números son pares 
# y cuáles impares desde el primero hasta el segundo.

while(True):
    try:
        entero_1 = int(input("ingresa un número entero: "))
        entero_2 = int(input(f"ingresa un número entero mayor a {entero_1}: "))
        if entero_1 < entero_2:
            par = 0
            impar = 0
            for x in range(entero_1,entero_2+1):
                if x % 2 == 0:
                    print(x, "es par")
                    par+=1
                if x % 2 != 0:
                    print(x, "no es par")
                    impar+=1
            print(f"\thay {par} pares")
            print(f"\thay {impar} impares")
        else: 
            print(f"el número ingresado {entero_2} no es mayor que {entero_1}, intenta nuevamente.")
    except:
        print(f"ERROR. intente Nuevamente:")
             