#Escriba un programa que permita crear una lista de palabras 
#(que puede ser vacía). Para ello, el programa tiene que pedir un número y 
#luego solicitar ese número de palabras para crear la lista. Por último, 
#el programa tiene que escribir la lista.


lista = []


numero = int(input("¿cuantos numeros de palabras ingresará? : "))

if numero < 1:
    print("no puede ser")

else:
    
    for i in range(numero):
        palabra = str(input("ingresará palabra: "))
        lista+=[palabra]

    print(f"la lista creada es {lista}")
