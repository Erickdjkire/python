#Resuelva de nuevo el ejercicio "if ... elif ... else ... 6" 
#de manera que el cálculo lo realice una función que reciba un parámetro (el año) y 
#devuelva True o False según que el año sea o no bisiesto.

print("COMPROBADOR DE AÑOS BISIESTOS")
fecha = int(input("Escriba un año y le diré si es bisiesto: "))

if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
    print(f"{fecha}, es año biciesto.")
else:
       print(f"{fecha},  no es año biciesto.")

