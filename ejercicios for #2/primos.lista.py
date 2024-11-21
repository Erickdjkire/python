
encendido = "on"
while(encendido=="on"):
    try:
        print("\n\tLista números primos".upper())
        
        b = int(input("ingrese número: "))
    
        

        if 0 > b:
            print("numero menor")

        else:
            for t in range(2,b+1):
                for u in range(2,t):
                    if t % u == 0:
                        #print(f"{t} no es número primo".title())
                        break

                else:
                    print(f"{t} es número primo".title())

            
            
                

    except:
        print("ERROR:")