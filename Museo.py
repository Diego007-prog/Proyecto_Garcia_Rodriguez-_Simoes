#falta el Api
from Obra import Obra
from Departamento import Departamento
from Artista import Artista



class Museo :
    def __init__(self, departamentos):
        self.departamentos = departamentos

    def start (self):
        self.iniciar_objetos ()

        while True:
            menu = input ("Bienvenido al Catálogo del Museo metropolitano de Arte, por favor elija una opcion: \n 1-Ver lista de obras por Departamento \n 2-Ver lista de obras por Nacionalidad del autor \n 3-Ver lista de obras por nombre del autor \n 4-Finalizar programa \n>")

            if menu == "1":
                contador = 1
                for departamento in self.departamentos:
                    print(f"{contador}. {departamento.nombre_departamento} (ID: {departamento.id_departamento})")
                    contador += 1
                
                opcion = input("Seleccione el numero del departamento que desea consultar: ")
                while not opcion.isdigit() or (int(opcion) < 1 or int(opcion) > len(self.departamentos)):
                    opcion = input("Error. Por favor, ingrese un número válido: ")
                    


            elif menu == "2":
                pass

            elif menu == "3":
                pass

            else:
                break


    def iniciar_objetos(self):
        pass    

