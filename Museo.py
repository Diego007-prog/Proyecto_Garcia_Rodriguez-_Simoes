#falta el Api
from Obra import Obra
from Departamento import Departamento
from Artista import Artista
from api import api_buscar_obras_por_departmento, api_buscar_obras_por_nombre, api_buscar_obras_por_id

from descargar_imagen import guardar_imagen_desde_url
from PIL import Image



class Museo :
    def __init__(self, departamentos):
        self.departamentos = departamentos

    def start (self):
        self.iniciar_objetos ()

        while True:
            menu = input ("Bienvenido al Catálogo del Museo metropolitano de Arte, por favor elija una opcion: \n 1-Ver lista de obras por Departamento \n 2-Ver lista de obras por Nacionalidad del autor \n 3-Ver lista de obras por nombre del autor \n 4-Finalizar programa \n>")

            if menu == "1":
                self.opcion_1()
            elif menu == "2":
                self.opcion_2()
            elif menu == "3":
                self.opcion_3()
            else:
                break

    def descargar_imgen(self, obra):
                
        # URL de la API
        api_url = obra.imagen_obra
        # Nombre deseado para el archivo (sin extensión, ya que se determinará automáticamente)
        nombre_archivo_destino = obra.titulo

        # Llamar a la función para guardar la imagen
        nombre_archivo_guardado = guardar_imagen_desde_url(api_url, nombre_archivo_destino)

        # Mostrar la imagen si se guardó correctamente
        if nombre_archivo_guardado:
            try:
                img = Image.open(nombre_archivo_guardado)
                img.show()
            except IOError as e:
                print(f"Error al abrir la imagen: {e}")

    def opcion_1(self):
        #Muestra los departamentos de forma enumerada
        contador = 1
        for departamento in self.departamentos:
            print(f"{contador}. {departamento.nombre_departamento} (ID: {departamento.id_departamento})")
            contador += 1
        
        #Pide al usuario que seleccione un departamento
        opcion = input("Seleccione el numero del departamento que desea consultar: ")
        while not opcion.isdigit() or (int(opcion) < 1 or int(opcion) > len(self.departamentos)):
            opcion = input("Error. Por favor, ingrese un número válido: ")

        #Busca las obras del departamento seleccionado
        id = self.departamentos[int(opcion)-1].id_departamento
        listado_id = api_buscar_obras_por_departmento(id)

        obras = []
        #Muestra las obras del departamento seleccionado
        for id in listado_id:
            obra = api_buscar_obras_por_id(id)
            if obra != None:
                obras.append(obra)

        for obra in obras:
            obra.show()

        #selecciona una obra para descargar la imagen
        opcion = input("¿Desea ver la imagen de una obra? (s/n): ")
        if opcion.lower() == "s":
            id_obra = input("Ingrese el ID de la obra: ")
            while not id_obra.isdigit():
                id_obra = input("Error. Por favor, ingrese un ID valido, recuerde que debe ser un numero: ")


            for obra in obras:
                if int(obra.id_obra) == int(id_obra):
                    self.descargar_imgen(obra)

    def opcion_2(self):
        
        nacionalidades = ["Afghan", "Albanian", "Algerian", "American", "Andorran", "Angolan", "Anguillan", "Argentine", "Armenian", "Australian", "Austrian", "Azerbaijani", "Bahamian", "Bahraini", "Bangladeshi", "Barbadian", "Belarusian", "Belgian", "Belizean", "Beninese", "Bermudian", "Bhutanese", "Bolivian", "Botswanan", "Brazilian", "British", "British Virgin Islander", "Bruneian", "Bulgarian", "Burkinan", "Burmese", "Burundian", "Cambodian", "Cameroonian", "Canadian", "Cape Verdean", "Cayman Islander", "Central African", "Chadian", "Chilean", "Chinese", "Citizen of Antigua and Barbuda", "Citizen of Bosnia and Herzegovina", "Citizen of Guinea-Bissau", "Citizen of Kiribati", "Citizen of Seychelles", "Citizen of the Dominican Republic", "Citizen of Vanuatu", "Colombian", "Comoran", "Congolese (Congo)", "Congolese (DRC)", "Cook Islander", "Costa Rican", "Croatian", "Cuban", "Cymraes", "Cymro", "Cypriot", "Czech", "Danish", "Djiboutian", "Dominican", "Dutch", "East Timorese", "Ecuadorean", "Egyptian", "Emirati", "English", "Equatorial Guinean", "Eritrean", "Estonian", "Ethiopian", "Faroese", "Fijian", "Filipino", "Finnish", "French", "Gabonese", "Gambian", "Georgian", "German", "Ghanaian", "Gibraltarian", "Greek", "Greenlandic", "Grenadian", "Guamanian", "Guatemalan", "Guinean", "Guyanese", "Haitian", "Honduran", "Hong Konger", "Hungarian", "Icelandic", "Indian", "Indonesian", "Iranian", "Iraqi", "Irish", "Israeli", "Italian", "Ivorian", "Jamaican", "Japanese", "Jordanian", "Kazakh", "Kenyan", "Kittitian", "Kosovan", "Kuwaiti", "Kyrgyz", "Lao", "Latvian", "Lebanese", "Liberian", "Libyan", "Liechtenstein citizen", "Lithuanian", "Luxembourger", "Macanese", "Macedonian", "Malagasy", "Malawian", "Malaysian", "Maldivian", "Malian", "Maltese", "Marshallese", "Martiniquais", "Mauritanian", "Mauritian", "Mexican", "Micronesian", "Moldovan", "Monegasque", "Mongolian", "Montenegrin", "Montserratian", "Moroccan", "Mosotho", "Mozambican", "Namibian", "Nauruan", "Nepalese", "New Zealander", "Nicaraguan", "Nigerian", "Nigerien", "Niuean", "North Korean", "Northern Irish", "Norwegian", "Omani", "Pakistani", "Palauan", "Palestinian", "Panamanian", "Papua New Guinean", "Paraguayan", "Peruvian", "Pitcairn Islander", "Polish", "Portuguese", "Prydeinig", "Puerto Rican", "Qatari", "Romanian", "Russian", "Rwandan", "Salvadorean", "Sammarinese", "Samoan", "Sao Tomean", "Saudi Arabian", "Scottish", "Senegalese", "Serbian", "Sierra Leonean", "Singaporean", "Slovak", "Slovenian", "Solomon Islander", "Somali", "South African", "South Korean", "South Sudanese", "Spanish", "Sri Lankan", "St Helenian", "St Lucian", "Stateless", "Sudanese", "Surinamese", "Swazi", "Swedish", "Swiss", "Syrian", "Taiwanese", "Tajik", "Tanzanian", "Thai", "Togolese", "Tongan", "Trinidadian", "Tristanian", "Tunisian", "Turkish", "Turkmen", "Turks and Caicos Islander", "Tuvaluan", "Ugandan", "Ukrainian", "Uruguayan", "Uzbek", "Vatican citizen", "Venezuelan", "Vietnamese", "Vincentian", "Wallisian", "Welsh", "Yemeni", "Zambian", "Zimbabwean"]
        for i, nacionalidad in enumerate(nacionalidades):
            print(f"{i+1}. {nacionalidad}")

        opcion = input("Seleccione el numero de la nacionalidad que desea consultar: ")
        while not opcion.isdigit() or not int(opcion) in range(1, len(nacionalidades) + 1):
            opcion = input("Error. Por favor, ingrese un número válido: ")
        
        nacionalidad_seleccionada = nacionalidades[int(opcion) - 1]

    def opcion_3(self):
        #pide al usuario que ingrese el nombre del autor
        nombre = input("Ingrese el nombre del autor que desea consultar: ")

        #busca las obras del autor ingresado
        obras = api_buscar_obras_por_nombre(nombre)


        #selecciona una obra para descargar la imagen
        opcion = input("¿Desea ver la imagen de una obra? (s/n): ")
        if opcion.lower() == "s":
            id_obra = input("Ingrese el ID de la obra: ")
            while not id_obra.isdigit():
                id_obra = input("Error. Por favor, ingrese un ID valido, recuerde que debe ser un numero: ")


            for obra in obras:
                if int(obra.id_obra) == int(id_obra):
                    self.descargar_imgen(obra)



    def iniciar_objetos(self):
        pass    

