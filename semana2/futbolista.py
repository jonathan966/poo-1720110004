class Futbolista():

    nombre = None
    disiplina = None
    coordinacion = None
    velocidad = None
    tecnica = None
    num_jugador = None
    equipo = None
    vestuario= None 
    liga = None 
    goles = None 

    def __inti__(self):
        print("clase Futbolista")



    def entrenar (self):
        print("Metodo entrenar")

    def patear (self):
        print("Metodo patear")
        
    def festejar (self):
        print("Metodo festejar")

    def fintear (self):
        print("Metodo fintear")

    def correr (self):
        print("Metodo correr")



messi = Futbolista() 
messi.nombre = "lionel"
messi.disiplina = "constante"
messi.coordinacion = "motriz"
messi.velocidad = "32,5 Km/h"
messi.tecnica = "drible"
messi.num_jugador = 10
messi.equipo = "Barcelona"
messi.vestuario = "deportivo"
messi.division = "primera"
messi.goles = 720

print(messi.nombre)
print(messi.disiplina)
print(messi.coordinacion)
print(messi.velocidad)
print(messi.tecnica)
print(messi.num_jugador)
print(messi.equipo)
print(messi.vestuario)
print(messi.division)
print(messi.goles)

messi.entrenar()
messi.patear()
messi.festejar()
messi.fintear()
messi.correr()