import pip._vendor.requests as requests

from Departamento import Departamento
from Obra import Obra

def api_departaments():
    departamentos = []
    url = "https://collectionapi.metmuseum.org/public/collection/v1/departments"

    data = requests.get(url)

    response = data.json()

    for k in response["departments"]:
        departamento = Departamento(k["departmentId"], k["displayName"])
        departamentos.append(departamento)

    return departamentos


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

def api_buscar_obras_por_departmento(id):
    r="https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=" + str(id) + "&q=*&hasImages=true"
    data = requests.get(r)

    listado_id = data.json()["objectIDs"]

    #print(listado_id)

    return listado_id

def api_buscar_obras_por_id(id):
    r="https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(id)
    data = requests.get(r)

    try:
        obra = data.json()
    except requests.exceptions.JSONDecodeError:
        #print(f"respuesta inválida para ID {id}")
        return None
    obra = Obra(obra["objectID"], obra["title"], obra["artistDisplayName"], obra["artistNationality"], obra["artistBeginDate"], obra["artistEndDate"], obra["classification"], obra["objectDate"], obra["primaryImageSmall"])
    return obra


def api_buscar_obras_por_nombre(nombre):
    nombre_codificado = nombre.replace(" ", "%20").lower()
    #url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={nombre_codificado}&artistOrCulture=true&hasImages=true"
    url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre_codificado}"
    data = requests.get(url)
    listado_id = data.json()
    print(listado_id)
    return listado_id

