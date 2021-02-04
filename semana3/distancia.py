import math

class Puntos():

    def _init_(self):
        pass

    def distancia(self,x_1,y_1,x_2,y_2):
        resultado = math.sqrt((x_2-x_1)**2+(y_2-y_1)**2)
        print(round(resultado,2))

objeto_puntos = Puntos()
objeto_puntos.distancia(7.88,3.17,4.78,4.99)