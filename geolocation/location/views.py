from django.shortcuts import render
import requests
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

'''
Tareas pendientes en este codigo:

0. Investigar como enviar los datos al front (SOLVED)

1. Filtros para tomar las coordenadas y/o codigo postal y extraer el pronostico de la api

2. Implementar las 3 apis pronostico, calidad aire y temperatura

3. Implementar secrets.jon para agregar credenciales, url quemadas
'''

# Function that captures data (Coordenates) from browser 
@csrf_exempt
def geoposition(request):
    
    if request.method == 'POST':
    # obtener el valor de la variable enviada desde JavaScript por ajax
        getlat = request.POST['sendlat']
        getlong = request.POST['sendlong']
        print(getlat)
        print(getlong)
    return render(request, 'geolocation.html')



# Brings data from pronostic API and proccess the current format
def index(request):


    # Geolocation
    res = requests.get('http://ip-api.com/json/')
    location_data_one   = res.text
    location_data       = json.loads(location_data_one)
    print(location_data)

    # Api pronostico simplificado
    #url_api_pronostico  =    'http://siata.gov.co:8089/pronosticoMunicipiosSimplificado/63882184869634ff91bcf727d3fa210ec6c210bf/'
    url_api_pronostico  =   'http://siata.gov.co:8089/pronosticoMunicipios/63882184869634ff91bcf727d3fa210ec6c210bf/?=format?json'

    api_pronostico = requests.get(url_api_pronostico)
    data_format_text = api_pronostico.text
    api_format_json = json.loads(data_format_text)
    #print(api_format_json)
    #print(type(api_format_json))



    # Postal code ZIP
    codigoMunicipioArray = {" Barbosa ": "05079",
                                "Barbosa": "05079",
                                "Girardota": "05308",
                                "Copacabana": "05212",
                                "Bello": "05088",
                                "Medellin Centro": "05001002",
                                "Santa Elena": "05001003",
                                "Medellin Occidente": "05001001",
                                "Itag": "05360",
                                "Envigado": "05266",
                                "Sabaneta": "05631",
                                "Caldas": "05129",
                                "Palmitas": "05001004",
                                "La Estrella": "05380"}


    # Those are the json that brings pronostic of rain probability
    pronosticoMunicipioArray = {" Barbosa ": "/var/www/data/siata_app/wrfbarbosa.json",
                                    "Barbosa": "/var/www/data/siata_app/wrfbarbosa.json",
                                    "Girardota": "/var/www/data/siata_app/wrfgirardota.json",
                                    "Copacabana": "/var/www/data/siata_app/wrfcopacabana.json",
                                    "Bello": "/var/www/data/siata_app/wrfbello.json",
                                    "Medellin Centro": "/var/www/data/siata_app/wrfmedCentro.json",
                                    "Santa Elena": "/var/www/data/siata_app/wrfmedOriente.json",
                                    "Medellin Occidente": "/var/www/data/siata_app/wrfmedOccidente.json",
                                    "Itag": "/var/www/data/siata_app/wrfitagui.json",
                                    "Envigado": "/var/www/data/siata_app/wrfenvigado.json",
                                    "Sabaneta": "/var/www/data/siata_app/wrfsabaneta.json",
                                    "Caldas": "/var/www/data/siata_app/wrfcaldas.json",
                                    "Palmitas": "/var/www/data/siata_app/wrfpalmitas.json",
                                    "La Estrella": "/var/www/data/siata_app/wrflaestrella.json"}
    

    
    return render(request, 'index.html', {'data': location_data})





