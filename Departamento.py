class Departamento: 
    def __init__(self, id_departamento, nombre_departamento):
        self.id_departamento = id_departamento
        self.nombre_departamento = nombre_departamento

    def show (self):
        print (f"El ID del departamento es: {self.id_departamento}")
        print (f"Nombre: {self.nombre_departamento}")

        