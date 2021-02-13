'''
Nombre: Jonathan Granillo Robledo
Grupo: 21
Fecha:11/02/2021
Descripción: se solicitara al usuario el número de cálculos que quiere realizar y posteriormente lea el número de días y calcule el número de segundos que tiene.
'''
class Bucles():
    
   def __inti__(self):
       pass

   def bucle(self,calculo=int(input("numero de calculos :"))):
       for variable in range(calculo):
         dias = int(input("ingresa el numero de dias :"))
         segundos=dias*86400
         print("los segundos son:",segundos)

objeto = Bucles()
objeto.bucle()



         
    
    
