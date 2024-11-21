# Escriba un tipo range() que sea equivalente a la lista mostrada: 
#  [-250, -200, -150, -100]


encender = "on"
while(encender == "on"):
    try:
        
        print("\n\tTipo range".upper())
        lista = []
        for x in range(-250,-50,50):
            lista.append(x)
        print(f"{lista} \n\n\n", end="")
        encender = "off"
    except:
        print("ERROR:")