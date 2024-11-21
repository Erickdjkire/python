# Escriba un programa que pida un número entero mayor que 1 y que escriba si el número es un número primo o no.
# ingresar % x == 0:  solo es valido para 2 sentencias.





for i in range(2, 150+1):
    cont = 0
    for j in range(2, i + 1):
        if i % j == 0 and i != j:
            cont += 1
    if cont == 0:
        print(i, "es primo")
         



