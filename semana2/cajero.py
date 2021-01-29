class Cajero(): 

    pantalla = None
    software = None
    menu = None
    teclas = None
    ranura_dinero = None
    ranura_tarjeta = None
    peso = None
    botones_laterales = None 
    lector = None
    deposito_billetes = None

    def __init__(self):
        print("clase cajero")


    def sacar_dinero (self):
        print("Metodo sacar dinero")  

    def hacer_transacciones (self):
        print("Metodo hacer transacciones")


    def pagar_servicios (self):
        print("Metodo pagar servicios")     

    def cambiar_nip (self):
        print("Metodo cambiar nip") 

    def consultar_saldo (self):
        print("Metodo consultar saldo")     



cash= Cajero()
cash.pantalla = "touch"
cash.software = "windows"
cash.menu = "lista de accines"
cash.teclas ="numeros "
cash.ranura_dinero = 1
cash.ranura_tarjeta= 1
cash.peso = "1000 kg"
cash.botones_laterales = 8
cash.lector = "billetes"
cash.deposito_billetes = 1 

print(cash.pantalla)
print(cash.software)
print(cash.menu)
print(cash.teclas)
print(cash.ranura_dinero)
print(cash.ranura_tarjeta)
print(cash.peso)
print(cash.botones_laterales)
print(cash.lector)
print(cash.deposito_billetes)

cash.sacar_dinero()
cash.hacer_transacciones()
cash.pagar_servicios()
cash.cambiar_nip()
cash.consultar_saldo()