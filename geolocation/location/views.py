from django.shortcuts import render
import requests
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

'''
Tareas pendientes en este codigo:

1. Filtros para tomar las coordenadas y/o codigo postal y extraer el pronostico de la api

2. Implementar las 3 apis pronostico, calidad aire y temperatura

3. Implementar secrets.jon para agregar credenciales, url quemadas

4. Investigar como enviar los datos al front

'''

def index(request):


    # Geolocation
    res = requests.get('http://ip-api.com/json/')
    location_data_one   = res.text
    location_data       = json.loads(location_data_one)
    #print(location_data)

    # Api pronostico simplificado
    url_api_pronostico = 'http://siata.gov.co:8089/pronosticoMunicipiosSimplificado/63882184869634ff91bcf727d3fa210ec6c210bf/'

    api_pronostico = requests.get(url_api_pronostico)
    data_format_text = api_pronostico.text
    api_format_json = json.loads(data_format_text)
    #print(api_format_json)
    print(type(api_format_json))
    
    ##### pruebas

    return render(request, 'index.html', {'data': location_data})

@csrf_exempt
def geoposition(request):
    
    if request.method == 'POST':
    # obtener el valor de la variable enviada desde JavaScript
        getlat = request.POST['sendlat']
        getlong = request.POST['sendlong']
        print(getlat)
        print(getlong)
    return render(request, 'geolocation.html')


