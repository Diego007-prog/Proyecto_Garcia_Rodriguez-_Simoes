#falta el Api
from Obra import Obra
from Departamento import Departamento
from Artista import Artista



class Museo :
    def __init__(self, api):
        self.api = api

    def start (self):
        self.iniciar_objetos ()

        while True:
            menu = input ("Bienvenido al Catálogo del Museo metropolitano de Arte, por favor elija una opcion: \n 1-Ver lista de obras por Departamento \n 2-Ver lista de obras por Nacionalidad del autor \n 3-Ver lista de obras por nombre del autor \n 4-Finalizar programa ")

            if menu == "1":
                pass


            elif menu == "2":
                pass

            elif menu == "3":
                pass

            else:
                break


    def iniciar_objetos(self):
        pass    

