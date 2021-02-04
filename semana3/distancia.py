from math import sqrt

class Calculadora():

    def _init_(self):
        pass

    def distancia(self,x_1,y_1,x_2,y_2):
        resultado = sqrt((x_2-x_1)**2+(y_2-y_1)**2)
        print(round(resultado,2))

objeto=Calculadora()
objeto.distancia(7.88,3.17,4.78,4.99)