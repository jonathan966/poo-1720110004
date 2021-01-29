class serie_de_tv():

    Temporadas = None
    inicio = None
    fin = None
    nombre_serie = None
    canal = None
    narrativa = None
    episodios = None
    actores = None 
    vestuario = None 
    categoria = None 

    def __inti__(self):
        print("clase serie de tv")



    def ver (self):
        print("Metodo ver")

    def comprar (self):
        print("Metodo comprar")
        
    def sintonizar (self):
        print("Metodo sintonizar")

    def descargar (self):
        print("Metodo descargar")

    def editar (self):
        print("Metodo editar")



suits = serie_de_tv() 
suits.temporadas = 8
suits.inicio= 2011
suits.fin =  2019
suits.nombre_serie= "suits"
suits.canal = "cadena usa"
suits.narrativa = "leyes"
suits.episodios = 134
suits.num_actores= 56
suits.vestuario = "formal"
suits.categoria = "drama"

print(suits.temporadas)
print(suits.inicio)
print(suits.fin)
print(suits.nombre_serie)
print(suits.canal)
print(suits.narrativa)
print(suits.episodios)
print(suits.num_actores)
print(suits.vestuario)
print(suits.categoria)

suits.ver()
suits.comprar()
suits.sintonizar()
suits.descargar()
suits.editar()