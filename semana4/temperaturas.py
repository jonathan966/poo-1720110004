'''
Nombre: Jonathan Granillo Robledo
Grupo: 21
Fecha:11/02/2021
Descripción: calcular el promedio de N temperaturas registradas en grados celcius, durante 1 día, y posteriormente imprimir el promedio en grados farenheit.
'''
class Bucles():
   
   def __inti__(self):
       pass

   def bucle(self,calculo=int(input("numero de temperaturas :"))):
       for variable in range(calculo):
        temp_1 = int(input("temperatura 1 en celcius :"))
        temp_2= int(input("temperatura 2 en celcius :"))
        temp_3=int(input("temperatura 2 en celcius :"))
        prom=(temp_1+temp_2+temp_3)/3
        promf=(prom*1.8)+32
        print("Promedio en Farenheit: ",promf,"farenheit")  
                   
    
objeto = Bucles()
objeto.bucle()




