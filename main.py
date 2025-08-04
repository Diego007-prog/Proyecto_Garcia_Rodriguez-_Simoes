from Museo import Museo
from Api import Api

def main():
    manejador_api = Api()
    museo = Museo (manejador_api)
    museo.start()

main()
