import pip._vendor.requests as requests

from Departamento import Departamento
from Obra import Obra


######"""Funcion usadas hasta el momento"""

#Obtiene la lista de departamentos del museo con sus ids y nombres
def api_departaments():
    departamentos = []
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

    data = requests.get(url)

    response = data.json()

    for k in response["departments"]:
        departamento = Departamento(k["departmentId"], k["displayName"])
        departamentos.append(departamento)

    return departamentos

#busca las obras por id, devuelve un objeto Obra
def api_buscar_obras_por_id(id):
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

#busca las obras por departamento, devuelve una lista de ids de obras
def api_buscar_obras_por_departmento(id):
    r="https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=" + str(id) + "&q=*&hasImages=true"
    data = requests.get(r)

    listado_id = data.json()["objectIDs"]

    #print(listado_id)

    return listado_id

#busca las obras por nombre del artista, y muestra las obras encontradas
def api_buscar_obras_por_nombre(nombre):
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


######"""Fin funcion usadas hasta el momento"""







def api_obras():
    obras = []
    url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

    data = requests.get(url)

    listado_id = data.json()

    for k in listado_id["objectIDs"]:
        url2 = "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(k)
        #print(url2)

"""
api_departaments()
api_obras()
"""




        
    
