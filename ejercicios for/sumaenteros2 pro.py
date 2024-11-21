# Escriba un programa que pida dos números enteros y escriba la suma 
# de todos los enteros desde el primer número hasta el segundo.

def main():
    while(True):
        try:
            pide_1 = int(input("ingrese un número entero: "))
            pide_2 = int(input("ingrese otro número entero: "))
            suma = 0
            print(f"\n\tla suma desde {pide_1} hasta {pide_2} es:")
            for x in range(pide_1,pide_2+1):
                suma+=x
                print(f"{x}+", end=" ")
            print(f"= {suma}\n\n")
        except:
            print("code ERROR:")
if __name__ == "__main__":
    main()