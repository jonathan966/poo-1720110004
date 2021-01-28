class Banco(): 

    clientes = None
    tarjeta = None
    app = None
    apartado_ahorro = None
    Sucursal = None
    aparatado_prestamo = None
    cajeros_automaticos = None
    trasnferencias = None 
    seguros = None
    personal = None 

    def __init__(self):
        print("clase banco")


    def guardar_dinero(self):
        print("Metodo guardar dinero")  

    def cambiar_dinero(self):
        print("Metodo cambiar dinero")


    def prestar_dinero(self):
        print("Metodo prestar dinero")     

    def transferir_dinero(self):
        print("Metodo trasferir dinero") 

    def vender_seguros(self):
        print("Metodo vender seguros")     



bbva = Banco()
bbva.clientes = "Numero de cliente"
bbva.tarjeta = "Numero de tarjeta"
bbva.app ="Movil"
bbva.apartado_ahorro = "Educación Superior"
bbva.sucursal = "Urbana"
bbva.apartado_prestamo = "Hipotecarios"
bbva.cajeros_automaticos = "full"
bbva.transferencias = "Nacionales "
bbva.seguros = "De vida "
bbva.personal = "Ejecutivos"

print(bbva.clientes)
print(bbva.tarjeta)
print(bbva.app)
print(bbva.apartado_ahorro)
print(bbva.sucursal)
print(bbva.apartado_prestamo)
print(bbva.cajeros_automaticos)
print(bbva.transferencias)
print(bbva.seguros)
print(bbva.personal)

bbva.guardar_dinero()
bbva.cambiar_dinero()
bbva.prestar_dinero()
bbva.transferir_dinero()
bbva.vender_seguros()