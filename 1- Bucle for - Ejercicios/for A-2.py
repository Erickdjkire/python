# Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

# los divisores son todos los números naturales que dividen de forma exacta a otro número natural. 
# Ejemplo: “Los divisores del  '15' son: 1, 3, 5 y 15. (La división de '15' entre cualquiera de esos números es exacta)



encender  = "on"
while(encender =="on"):
    try:
        print("\nverificar divisores".upper())
        ingrese = int(input("ingrese número entero mayor a cero: \n\n\n".title()))
        if ingrese <= 0:
            print(f"ojo. '{ingrese}', no es mayor a cero".title())
        else:
            print(f"usted ingresó '{ingrese}', sus divisores son:".title())
            for x in range(1,ingrese+1):
                if ingrese % x == 0:
                    print(f"   {x}",end="")
            else:
                finalizar = str(input(f"\n\n¿desea ingresar y verificar más numeros? si/no :\n\n\t".title())).lower()
                if finalizar == "si":
                    print(f"\tgenial. usted ingresó '{finalizar}', seguimos!!\n\n".title())
                if finalizar == "no":
                    print(f"\tadios. usted ingresó '{finalizar},' hasta pronto.\n\n".title())
                    encender = "off"
                if finalizar != "si" and finalizar != "no":
                    print(f"\tusted ingresó '{finalizar}' y no se reconoce como instruccion. continuemos...\n\n".title())
    except:
        print("ERROR:")