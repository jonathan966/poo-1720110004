class Coche(): 

    modelo = None
    num_serie = None
    precio = None
    motor = None
    potencia = None
    deposito_combustible = None
    peso = None
    velocidad = None 
    num_llantas = None
    color = None 

    def __init__(self):
        print("clase coche")

    def prender(self):
        print("Metodo prender")  

    def apagar(self):
        print("Metodo cambiar apagar")

    def acelerar(self):
        print("Metodo prestar acelerar")     

    def frenar(self):
        print("Metodo Frenar") 

    def girar(self):
        print("Metodo girar")     


jetta = Coche()
jetta.modelo = "Comfortline"
jetta.num_serie = 154215842
jetta.precio ="410.200 MXN"
jetta.motor = "1.4 L "
jetta.potencia = "150 CV"
jetta.deposito_combustible = "50 L"
jetta.peso = "1.393 kg"
jetta.velocidad = "194.12 km/h"
jetta.num_llantas = 4
jetta.color = "Azul"

print(jetta.modelo)
print(jetta.num_serie)
print(jetta.precio)
print(jetta.motor)
print(jetta.potencia)
print(jetta.deposito_combustible)
print(jetta.peso)
print(jetta.velocidad)
print(jetta.num_llantas)
print(jetta.color)

jetta.prender()
jetta.apagar()
jetta.acelerar()
jetta.frenar()
jetta.girar()