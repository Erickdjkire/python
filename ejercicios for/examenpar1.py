# Escriba un programa que pregunte cuántos números se van a introducir, 
# pida esos números, y diga al final cuántos han sido pares y cuántos impares.

while(True):
    try:
        num = int(input("¿cuantos números va a ingresar? "))
        if num <= 0:
            print("IMPOSIBLE: ")
        else:
            a = 0
            b = 0
            lo = []
            par = []
            impar = []
            for x in range(num):
                ing = int(input("ingrese un Número: "))
                lo.append(ing)
                if ing % 2 == 0:
                    a+=1
                    print(f"{ing} es par")
                    par.append(ing)
                else:
                    b+=1
                    print(f"{ing} es impar")
                    impar.append(ing)
            print(f"los números son '{lo}'\nha introducido {a} números pares ({par}) y {b} números impares {impar}")
            print(f"\n\tterminado!!\n\t")  
    except:
        print("Error:")