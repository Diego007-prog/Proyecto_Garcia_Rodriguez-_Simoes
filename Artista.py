class Artista: 
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, fecha_muerte):
        self.nombre=nombre
        self.nacionalidad=nacionalidad
        self.fecha_nacimiento=fecha_nacimiento
        self.fecha_muerte=fecha_muerte

    def show (self):
        print (f"El nombre del artista es: {self.nombre}")
        print (f"Nacionalidad: {self.nacionalidad}")
        print (f"Fecha de Nacimiento: {self.fecha_nacimiento}")
        print (f"Fecha de defuncion: {self.fecha_muerte}")