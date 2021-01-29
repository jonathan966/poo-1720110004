class Avion():

    numero_serie = None
    numero_llantas = None
    tamaño = None
    Color = None
    velocidad = None
    turbinas = None
    asientos = None
    alerones = None 
    peso = None 
    precio = None 

    def __inti__(self):
        print("clase Avion")



    def volar (self):
        print("Metodo volar")

    def aterrizar (self):
        print("Metodo aterrizar")
        
    def transportar (self):
        print("Metodo transportar")

    def despegar (self):
        print("Metodo despegar")

    def encender (self):
        print("Metodo encender")



avioneta = Avion() 
avioneta.numero_serie = 15421
avioneta.nuemero_llantas= 12
avioneta.tamanno =  "70,67 metros"
avioneta.color = "blanco"
avioneta.velocidad = "13.480 kilómetros."
avioneta.turbinas = "si"
avioneta.asientos = 586
avioneta.alerones = 2
avioneta.peso = "162 400 kg"
avioneta.precio = "260.000 dollars"

print(avioneta.numero_serie)
print(avioneta.nuemero_llantas)
print(avioneta.tamanno)
print(avioneta.color)
print(avioneta.velocidad)
print(avioneta.turbinas)
print(avioneta.asientos)
print(avioneta.alerones)
print(avioneta.peso)
print(avioneta.precio)

avioneta.volar()
avioneta.aterrizar()
avioneta.transportar()
avioneta.despegar()
avioneta.encender()



