class Obra:
    def __init__(self, id_obra, titulo, nombre_artista, nacionalidad_artista, fecha_nacimiento_artista, fecha_muerte_artista, tipo, ano_creacion, imagen_obra):
        self.id_obra=id_obra
        self.titulo=titulo
        self.nombre_artista=nombre_artista
        self.nacionalidad_artista=nacionalidad_artista
        self.fecha_nacimiento_artista=fecha_nacimiento_artista
        self.fecha_muerte_artista=fecha_muerte_artista
        self.tipo=tipo
        self.ano_creacion=ano_creacion
        self.imagen_obra=imagen_obra

    def show (self):
        print (f"Id de la obra: {self.id_obra}")
        print (f"Titulo: {self.titulo}")
        print (f"Nombre del artista: {self.nombre_artista}")
        print (f"Nacionalidad del artista: {self.nacionalidad_artista}")
        print (f"Fecha de nacimiento del artista: {self.fecha_nacimiento_artista}")
        print (f"Fecha de muerte del artista: {self.fecha_muerte_artista}")
        print (f"Tipo: {self.tipo}")
        print (f"Año de creación: {self.ano_creacion}")
        print (f"Imagen de la obra: {self.imagen_obra}")
        print("\n")

         