from utils.librairies import *
from utils.common import *


while True:
    clear()
    menu()
    ville = input(f"[{c}>{r}] Ville : ")

    search(ville)