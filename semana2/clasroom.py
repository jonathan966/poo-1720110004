class Google_classroom(): 

    plataforma_educativa = None
    nombre = None
    disenno_pagina = None
    gratuito = None
    navegacion = None
    dominio = None
    aula_virtual = None
    organizacion = None 
    video_llamadas = None
    gestion_tareas = None


    def __init__(self):
        print("clase Google classroom")


    def calificar_tareas  (self):
        print("Metodo calificar tareas")  

    def enviar_comentarios  (self):
        print("Metodo enviar comentarios ")


    def iniciar_video_llamadas  (self):
        print("Metodo iniciar video llamadas ")     

    def annadir_materias  (self):
        print("Metodo añadir materias") 

    def compartir_recursos  (self):
        print("Metodo compartir recursos ")     



moodle = Google_classroom()
moodle.plataforma_educativa  = "aprendizaje"
moodle.nombre = "moodle"
moodle.disenno_pagina ="simple"
moodle.gratuito  = "si "
moodle.navegacion = "facil"
moodle.dominio = "propio"
moodle.aula_virual = "si"
moodle.oraganizacion = "limpia"
moodle.video_llamadas = "si"
moodle.gestion_tareas = "tablon"

print(moodle.plataforma_educativa)
print(moodle.nombre)
print(moodle.disenno_pagina)
print(moodle.gratuito)
print(moodle.navegacion)
print(moodle.dominio)
print(moodle.aula_virtual)
print(moodle.organizacion)
print(moodle.video_llamadas)
print(moodle.gestion_tareas)

moodle.calificar_tareas()
moodle.enviar_comentarios()
moodle.iniciar_video_llamadas()
moodle.annadir_materias()
moodle.compartir_recursos()