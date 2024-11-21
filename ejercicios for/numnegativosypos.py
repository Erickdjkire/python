# Escriba un programa que pregunte cuántos números se van a introducir, 
# pida esos números y escriba cuántos negativos ha introducido.



while(True):
   try:
      cuantos = int(input("¿cuantos números vas a introducir? "))
      if cuantos <= 0:
          print("Imposible.")
      else:
          x = 0
          a = 0
          b = 0
          c = 0

          for x in range(cuantos):
           ingrese = int(input("ingrese número "))
           if ingrese < 0:
              a+=1

           if ingrese > 0:
              b+=1
              
           if ingrese == 0:
              c+=1
              
          print(f"usted ha ingresado: \n\t{a} números negativos\n\t{b} positivos\n\t{c} ceros")
   except:
      print("error:")

    

        
    
