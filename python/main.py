import requests
import json
import datetime

token = "82f265a6e71ff7c7c35e66b492ec1f3c"
url = "https://api.openweathermap.org/data/2.5/weather"

ville = input("ville : ")

request = requests.get(f"{url}?appid={token}&q={ville}&lang=fr&units=metric")
request = request.json()

try:
 ville = {
    "nom": request['name'],
    "pays": request['sys']["country"],
    "coords": str(request["coord"]["lat"]) + "," + str(request["coord"]["lon"])
}

 meteo = {
    "description": request["weather"][0]["description"],
    "icon": "http://openweathermap.org/img/w/" + request["weather"][0]["icon"] + ".png",
    "température": {
        "normale": request["main"]["temp"],
        "ressentie": request["main"]["feels_like"],
        "max": request["main"]["temp_max"],
        "min": request["main"]["temp_min"]
    },
    "humidité": request["main"]["humidity"],
    "pression": request["main"]["pressure"],
    "visibilité": request["visibility"],
    "vent": {
        "vitesse": round(request["wind"]["speed"])
    },
    "soleil": {
        "coucher": datetime.datetime.fromtimestamp(request["sys"]["sunset"] + request["timezone"]).strftime("%H:%M"),
        "lever": datetime.datetime.fromtimestamp(request["sys"]["sunrise"] + request["timezone"]).strftime("%H:%M")
    }
}
except KeyError as e:
  print(e)
  

print(ville["nom"])
print(ville["pays"])
print(ville["coords"])
print(meteo["description"])
print(meteo["icon"])
print(meteo["température"])
print(meteo["humidité"], "%")
print(meteo["pression"], "hPa")
print(meteo["visibilité"], "m")
print(meteo["vent"]["vitesse"], "m/s //", meteo["vent"]["vitesse"] * 3.6,"km/h")
print(meteo["soleil"])