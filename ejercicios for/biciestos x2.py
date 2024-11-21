#Escriba un programa que pida dos años y escriba cuántos años 
#bisiestos hay entre esas dos fechas (incluidos los dos años):

print("COMPROBADOR DE AÑOS BISIESTOS")
fecha1 = int(input("Escriba un año: "))
fecha2 = int(input(f"Escriba otro año despues de {fecha1}: "))


if fecha1 < fecha2:
    if fecha1 - fecha2 :
        print(f"de {fecha1} a {fecha2} hay {fecha2 - fecha1} años")
        if fecha1 % 4 == 0:
            print(f"{fecha1} posee año biciestos")
        if fecha2 % 4 == 0:
            print(f"{fecha2} posee año biciestos")
        if fecha1 - fecha2 // 4:
            print(f"hay {(fecha2 - fecha1) // 4} años biciestos más")





else:
    print(f"usted ingresó {fecha2} que es menor a {fecha1}")
