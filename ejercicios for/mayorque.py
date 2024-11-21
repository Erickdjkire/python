# Escriba un programa que pregunte cuántos números se van a introducir, 
# pida esos números, y muestre un mensaje cada vez que un número no sea 
# mayor que el primero.
def main():
    while(True):
        try:



            cuantos = int(input("¿cuantos números vas a introducir? "))
            primero = int(input("ingresa número: "))
            for a in range (cuantos-1):
                numero = int(input(f"Escriba un número más grande que {primero}: "))
                if numero <= primero:
                    print(f"¡{numero} no es mayor que {primero}!")
                else:
                    print(f"sí. {numero} es mayor que {primero}!")
        except:
            print("Error: ")

if __name__ == "__main__":
    main()