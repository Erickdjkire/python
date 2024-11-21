# Escriba un tipo range() que sea equivalente a la lista mostrada: [1000, 1001, 1002, 1003]


#def main()
encender = "on"
while(encender =="on"):
    try:
        lista = []
        for x in range(1000,1004):
            lista.append(x)
        print(lista)
        encender = "off"
    except:
        print("ERROR:")