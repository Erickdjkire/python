#scriba un programa conversor de centímetros a kens y shakus, unidades japonesas de longitud.


bucle = "s"
while (bucle=="s"):
    try:
        ing = int(input("ingrese los centimetros a conevertir: "))
        if ing <= 0:
            print(f"ERROR. usted ingreso {ing}.")

        else:
            ken = 0.0047206329
            shakus = 0.033
            print(f"usted ingresó {ing}\n\ten ken sería: {ken*ing}\n\t en shakus sería: {shakus*ing}")
            


        bucle = str(input("¿desea seguír convirtiendo s/n ?")).lower()
    except:
        print("ERROR: ")