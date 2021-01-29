class Vacaciones():

    suspension_labores = None
    descanso = None
    ocio = None
    turismo = None
    estacion_anno = None
    dias = None
    se_acumulan = None
    se_dividen = None 
    relajante = None 
    region = None 

    def __inti__(self):
        print("clase vacaciones")



    def disfrutar (self):
        print("Metodo disfrutar")

    def descansar (self):
        print("Metodo descansar")
        
    def desestresar (self):
        print("Metodo desestresar")

    def jugar (self):
        print("Metodo jugar")

    def viajar (self):
        print("Metodo viajar")



dia_libre =Vacaciones() 
dia_libre.suspension_labores = "relativa" 
dia_libre.descanso = "duracion corta"
dia_libre.ocio =  "activo"
dia_libre.turismo = "viajar a otros lados"
dia_libre.estacion_anno = "verano"
dia_libre.dias = 6
dia_libre.se_acumulan = "SI"
dia_libre.se_dividen = "acuerdo en comun"
dia_libre.relajante = "SI"
dia_libre.region = "América Latina"

print(dia_libre.suspension_labores)
print(dia_libre.descanso)
print(dia_libre.ocio)
print(dia_libre.turismo)
print(dia_libre.estacion_anno)
print(dia_libre.dias)
print(dia_libre.se_acumulan)
print(dia_libre.se_dividen)
print(dia_libre.relajante)
print(dia_libre.region)

dia_libre.disfrutar()
dia_libre.descansar()
dia_libre.desestresar()
dia_libre.jugar()
dia_libre.viajar()