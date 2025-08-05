from Museo import Museo
from api import api_departaments

def main():
    departamentos = api_departaments()
    #manejador_api = Api()
    museo = Museo (departamentos)
    museo.start()

main()
