
def main():
    respuesta = "si"
    while respuesta == "si":
        los = input("¿Desea continuar el programa? si o no : ").lower()


        if los == "si":
            print("¡Genial. Seguimos!")

        if los == "no":
            print("¡Hasta la vista!")
            respuesta = "no"
            
        if los != "si" and los != "no":
            print("ingresa la opcion correcta")


if __name__ == "__main__":
    main()
