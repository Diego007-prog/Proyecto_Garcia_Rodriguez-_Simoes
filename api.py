import pip._vendor.requests as requests

from Departamento import Departamento
from Obra import Obra


######"""Funcion usadas hasta el momento"""


def api_departaments():

    """
    Obtiene la lista de departamentos del museo desde la API.

    Retorna:
        list: Una lista de objetos Departamento.
    """

    departamentos = []
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

    data = requests.get(url)

    response = data.json()

    for k in response["departments"]:
        departamento = Departamento(k["departmentId"], k["displayName"])
        departamentos.append(departamento)

    return departamentos


def api_buscar_obras_por_id(id):

    """
    Busca una obra por su ID en la API.

    Argumentos:
        id: El ID de la obra a buscar.

    Retorna:
        Obra: Un objeto Obra si se encuentra la obra, de lo contrario None.
    """
    r="https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(id)
    data = requests.get(r)

    try:
        obra = data.json()
    except requests.exceptions.JSONDecodeError:
        #print(f"respuesta inválida para ID {id}")
        return None
    
    if 'message' in obra:
        return None
    else:
        obra = Obra(obra["objectID"], obra["title"], obra["artistDisplayName"], obra["artistNationality"], obra["artistBeginDate"], obra["artistEndDate"], obra["classification"], obra["objectDate"], obra["primaryImageSmall"])
        return obra


def api_buscar_obras_por_departmento(id):

    """
    Busca las obras de un departamento específico

    Argumentos:
        id: El ID del departamento.

    Retorna:
        list: Una lista de IDs de obras.
    """

    r="https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=" + str(id) + "&q=*&hasImages=true"
    data = requests.get(r)

    listado_id = data.json()["objectIDs"]

    #print(listado_id)

    return listado_id


def api_buscar_obras_por_nombre(nombre):

    """
    Busca obras por el nombre de un artista.

    Argumentos:
        nombre: El nombre del artista a buscar.

    Retorna:
        list: Una lista de objetos Obra que coinciden con la búsqueda.
    """

    nombre_codificado = nombre.replace(" ", "%20").lower()
    #url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={nombre_codificado}&artistOrCulture=true&hasImages=true"
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre_codificado}"
    data = requests.get(url)
    listado_id = data.json()["objectIDs"]
    
    obras = []

    #si no se encuentran obras, devuelve None y lo indica
    if listado_id is None:
        print("No se encontraron obras para el nombre ingresado.")
    else:
        for id in listado_id:
            obra = api_buscar_obras_por_id(id)
            if obra != None:
                obra.show()
                obras.append(obra)

    return obras




def api_obras():

    """
    Busca todas las obras del museo y devuelve una lista de objetos de tipo Obra.
    
    Solo devuelve las primeras 100 obras para evitar tiempos de espera prolongados.

    Retorna:
        list: Una lista de objetos Obra.
    """

    obras = []
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

    data = requests.get(url)
    try:
        listado_id = data.json()
    except requests.exceptions.JSONDecodeError:
        return None

    #recorre la lista de ids y busca cada obra por id
    for i, id in enumerate(listado_id["objectIDs"]):
        if i >= 100: 
            break
        obra = api_buscar_obras_por_id(id)
        if obra is not None:
            obras.append(obra)

    return obras



######"""Fin funcion usadas hasta el momento"""









"""
api_departaments()
api_obras()
"""




        
    
