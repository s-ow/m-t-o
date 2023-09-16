from utils.librairies import *

def search(recherche):
    request = requests.get(f"{url}?appid={token}&q={recherche}&lang=fr&units=metric")
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
                "coucher": datetime.datetime.fromtimestamp(request["sys"]["sunset"]).strftime("%H:%M"),
                "lever": datetime.datetime.fromtimestamp(request["sys"]["sunrise"]).strftime("%H:%M")
            }
        }

        print(f"""
Ville :
\t {ville["nom"]}, {ville["pays"]}
\t {ville["coords"]}

Météo :
\t {meteo["description"]}
\t {meteo["température"]["normale"]}°C ({meteo["température"]["ressentie"]}°C ressentie)
\t Min/Max : {meteo["température"]["min"]}°C ~ {meteo["température"]["max"]}°C
\t Vent : {meteo["vent"]["vitesse"]} m/s // {meteo["vent"]["vitesse"] * 3.6} km/h
\t {meteo["humidité"]}% d'humidité

Autres :
\r\r Visibilité : {meteo["visibilité"]}m
\r\r Pression : {meteo["pression"]}
\r\r Soleil :
\t Lever : {meteo["soleil"]["lever"]}
\t Coucher : {meteo["soleil"]["coucher"]}
""")

        input(f"\n{c}[{r}>{c}]{r} Appuyez sur ENTREE : ")

    except KeyError as e:
      print


"""

 __    __     ______     ______   ______     ______    
/\ "-./  \   /\  ___\   /\__  _\ /\  ___\   /\  __ \   
\ \ \-./\ \  \ \  __\   \/_/\ \/ \ \  __\   \ \ \/\ \  
 \ \_\ \ \_\  \ \_____\    \ \_\  \ \_____\  \ \_____\ 
  \/_/  \/_/   \/_____/     \/_/   \/_____/   \/_____/ 
                                                       

"""

v = "1.0.0"
dev = "s-ow"
git = "https://github.com/s-ow/meteo"

# COULEURS

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
r = Fore.RESET

# FONCTIONS ===========================================================================

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def menu():
    Write.Print("                               __    __     ______     ______   ______     ______    \n", Colors.blue_to_cyan, interval=0.000)
    Write.Print("                              /\ \"-./  \   /\  ___\   /\__  _\ /\  ___\   /\  __ \   \n", Colors.blue_to_cyan, interval=0.000)
    Write.Print("                              \ \ \-./\ \  \ \  __\   \/_/\ \/ \ \  __\   \ \ \/\ \  \n", Colors.blue_to_cyan, interval=0.000)
    Write.Print("                               \ \_\ \ \_\  \ \_____\    \ \_\  \ \_____\  \ \_____\ \n", Colors.blue_to_cyan, interval=0.000)
    Write.Print("                                \/_/  \/_/   \/_____/     \/_/   \/_____/   \/_____/ \n", Colors.blue_to_cyan, interval=0.000)
    Write.Print(f"[Dev]:{dev}                                                                     \n", Colors.blue_to_cyan, interval=0.000)
    Write.Print(f"[Version]:{v}                                                                   \n", Colors.blue_to_cyan, interval=0.000)
    Write.Print(f"[Github]:{git}                                                                   \n", Colors.blue_to_cyan, interval=0.000)
    print("")