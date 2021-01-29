class Calculadora(): 

    modelo = None
    marca = None
    Color = None
    simbolos = None
    numeros = None
    teclas = None
    peso = None
    energia = None 
    tamanno = None
    cantidad_funciones = None

    def __init__(self):
        print("clase calculadora")


    def dividir (self):
        print("Metodo dividir")  

    def multiplicar (self):
        print("Metodo multiplicar")


    def restar (self):
        print("Metodo prestar restar")     

    def sumar (self):
        print("Metodo sumar") 

    def borrar (self):
        print("Metodo borrar")     



cientifica = Calculadora()
cientifica.modelo = "Comfortline"
cientifica.marca = "casio"
cientifica.color ="blanco con negro"
cientifica.simbolos = "ingenieria "
cientifica.numeros = "0-9"
cientifica.teclas= "plasticas"
cientifica.peso = "90 g"
cientifica.energia = "solar mas pilas"
cientifica.tamanno = "11.7 cm"
cientifica.cantidad_funciones = 552

print(cientifica.modelo)
print(cientifica.marca)
print(cientifica.color)
print(cientifica.simbolos)
print(cientifica.numeros)
print(cientifica.teclas)
print(cientifica.peso)
print(cientifica.energia)
print(cientifica.tamanno)
print(cientifica.cantidad_funciones)

cientifica.dividir()
cientifica.multiplicar()
cientifica.restar()
cientifica.sumar()
cientifica.borrar()