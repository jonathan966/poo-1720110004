class Estudiante():

    matricula = None
    nombre = None
    apellidos = None
    edad= None 
    grado = None 
    grupo = None
    numero_de_lista = None 
    ser_pensante = None
    tipo_de_escuela = None
    sistema_academico = None
    
    def __init__(self):
     print("clase estudiante")  

    
    def hacer_tareas(self):
      print("Metodo Hacer tareas")

    def crear_proyectos(self):
     print("Metodo crear proyectos")  

    def obtener_conocimientos(self):
     print("Metodo obtener conocimientos") 

    def entregar_trabajos(self):
        print("Metodo Entregar trabajos") 

    def tomar_clases(self):
        print("Metodo Tomar clases") 


universitario = Estudiante()
universitario.matricula = 1072011004 
universitario.nombre = "Jonathan" 
universitario.apellidos = "Granillo Robledo" 
universitario.edad = 19
universitario.grado = "segundo semestre" 
universitario.grupo = 21
universitario.numero_de_lista = 10
universitario.ser_pensante = "si" 
universitario.tipo_de_escuela = "Publica" 
universitario.sistema_academico = "Sep" 

print(universitario.matricula)
print(universitario.nombre)
print(universitario.apellidos)
print(universitario.edad)
print(universitario.grado)
print(universitario.grupo)
print(universitario.numero_de_lista)
print(universitario.ser_pensante)
print(universitario.tipo_de_escuela)
print(universitario.sistema_academico)


universitario.hacer_tareas()
universitario.crear_proyectos()
universitario.obtener_conocimientos()
universitario.entregar_trabajos()
universitario.tomar_clases()