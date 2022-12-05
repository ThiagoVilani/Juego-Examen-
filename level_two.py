import pygame
from pygame.locals import *
from constantes import *
from player import Player
from plataforma import *
from enemigo import *
from rewards import *
from gui_play_screen import *
from tramps import *
from gui_game_over import *
import json

with open(r"C:\Users\vilan\OneDrive\Escritorio\Juego-Examen-\level_two.json") as archivo:
        datita = json.load(archivo)
        dic_level = datita.copy()

dic_rewards = dic_level["rewards"]
plataformas = dic_level["platforms_list"]
dic_button = dic_level["pause_button"]
dic_tramps = dic_level["tramps"]
dic_player = dic_level["player"]
dic_score_table = dic_level["score_table"]
dic_life_bar = dic_level["life_bar"]
dic_enemys = dic_level["enemy"]

def create_level_two(difficulty):
    #La ruta de la imagen del fondo tiene que venir por json
    imagen_fondo = pygame.image.load(r"{0}".format(dic_level["background_image_path"])).convert()
    imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
    plataform_list = create_platforms_json(plataformas)
    rewards_list = create_rewards_json(dic_rewards["image_path"], int(dic_rewards["width"]), int(dic_rewards["height"]), int(dic_rewards["vertical_speed"]), int(dic_rewards["float_update_rate"]), int(dic_rewards["update_rate"]), plataform_list)
    #pause_button = Pause_button(dic_button["path_pause_icon"], dic_button["path_play_icon"], int(dic_button["x"]), int(dic_button["y"]), int(dic_button["width"]), int(dic_button["height"]))
    lista_trampas = create_tramps_json(plataform_list, dic_tramps["path_image"], int(dic_tramps["height"]), int(dic_tramps["width"]))
    player_1 = Player(dic_player, dic_life_bar, dic_score_table, difficulty)
    enemys_list = create_enemys_json(plataform_list, dic_enemys, difficulty)
    return imagen_fondo, rewards_list, plataform_list, lista_trampas, player_1, enemys_list

        ########### ALL PERFECT BUT hay que tocar algunos temas del enemigo #############