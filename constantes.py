import json

path = r"C:/Users/vilan/OneDrive/Escritorio/Juego-Examen-/settings.json"

with open(path, "r") as file:
    dic_settings = json.load(file)


ANCHO_VENTANA = dic_settings["ancho ventana"]
ALTO_VENTANA = dic_settings["alto ventana"]


GROUND_LEVEL = (ALTO_VENTANA*90)/100
FPS = dic_settings["fps"]

PATH_IMAGE = dic_settings["path_image"]
DIRECTION_L = 0
DIRECTION_R = 1
GROUND_COLLIDE_H = dic_settings["ground collide h"] #Â Aprox Gravedad/2 + 1
DEBUG = False