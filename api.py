import pip._vendor.requests as requests

from Departamento import Departamento

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

r="https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=1&q=*&hasImages=true"
data = requests.get(r)

listado_id = data.json()

print(listado_id)"""