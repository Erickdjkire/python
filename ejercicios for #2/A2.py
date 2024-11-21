# Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
# los divisores son todos los números naturales que dividen de forma exacta a otro número natural. 
# Ejemplo: “Los divisores del  '15' son: 1, 3, 5 y 15. (La división de '15' entre cualquiera de esos números es exacta)

bucle = "s"
while(bucle=="s"):
    try:
        ing = int(input("ingrese un número mayor que cero: "))
        if ing <= 0:
            print(f"Error, Usted ingresó {ing}")
        else:
            lista = []
            a = 1
            for x in range(a,ing+1):
               if ing % 1 == 0 and ing % x == 0:   
                   lista.append(x)         
            print(f"los divisores de {ing} son: {lista}")
        bucle = str(input("¿desea ingresar más números? s/n: ")).lower()
        if bucle != "s":
            print("Muchas gracias, Adios")
    except:
        print("ERROR:")
