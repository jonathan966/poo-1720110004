class Bucle():

    def __init__(self):
        pass

    def bucleWhile(self):
        repetir = ""
        while repetir == "":
          print("Materia :",self.materia) 
          print("Número de alumnos :",self.num_alumnos)
          print("Nombre alumno 1 :",self.nombre_alumno) 
          print("Número de clases :",self.numero_clases) 
          print("Número de faltas :",self.num_faltas) 
          print("Número de retardos :",self.num_retardos) 
          print("Porcentaje de asistencias :",self.porcentaje_asistencias) 
          print("Resultado :",self.resultado) 
          repetir = input(" otra evaluacion? (s/n) ")

while_1 = Bucle()  
while_2 = Bucle()

while_1.materia = "Programación orientada a objetos"
while_2.materia = "Base de datos"

while_1.num_alumnos = "2"
while_2.num_alumnos = "2"

while_1.nombre_alumno = "Dejah"
while_2.nombre_alumno = "Jhon"

while_1.numero_clases = "10"
while_2.numero_clases = "10"

while_1.num_faltas = "2"
while_2.num_faltas = "2"

while_1.num_retardos = "2"
while_2.num_retardos = "3"

while_1.porcentaje_asistencias = 80
while_2.porcentaje_asistencias = 70

while_1.resultado ="aprobado"
while_2.resultado ="no aprobado"


while_1.bucleWhile()
while_2.bucleWhile()
       