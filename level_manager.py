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


class Level_manager():
    def __init__(self):
        self.lvl_unlocked = 1
        self.lvl_playing = None
       
    def import_json(self, lvl):
        path_lvl = None
        if lvl == 1:
            path_lvl = "C:/Users/vilan/OneDrive/Escritorio/Juego-Examen-/level_one.json"
            self.lvl_playing = 1
        elif lvl == 2 and self.lvl_unlocked > 1:
            path_lvl = "C:/Users/vilan/OneDrive/Escritorio/Juego-Examen-/level_two.json"
            self.lvl_playing = 2
        elif lvl == 3 and self.lvl_unlocked > 2:
            path_lvl = "C:/Users/vilan/OneDrive/Escritorio/Juego-Examen-/level_three.json"
            self.lvl_playing = 3

        if path_lvl != None:
            with open(r"{0}".format(path_lvl)) as archivo:
                datita = json.load(archivo)
                dic_level = datita.copy()
                return dic_level 
    
    def create_level(self, difficulty:str, lvl):
        dic_level = self.import_json(lvl)
        if dic_level != None:
            imagen_fondo = pygame.image.load(r"{0}".format(dic_level["background_image_path"])).convert()
            imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
            plataform_list = create_platforms_json(dic_level["platforms_list"])
            rewards_list = create_rewards_json(dic_level["rewards"]["image_path"], int(dic_level["rewards"]["width"]), int(dic_level["rewards"]["height"]), int(dic_level["rewards"]["vertical_speed"]), int(dic_level["rewards"]["float_update_rate"]), int(dic_level["rewards"]["update_rate"]), plataform_list)
            lista_trampas = create_tramps_json(plataform_list, dic_level["tramps"]["path_image"], int(dic_level["tramps"]["height"]), int(dic_level["tramps"]["width"]))
            player_1 = Player(dic_level["player"], dic_level["life_bar"], dic_level["score_table"], difficulty)
            enemys_list = create_enemys_json(plataform_list, dic_level["enemy"], difficulty)
            return imagen_fondo, rewards_list, plataform_list, lista_trampas, player_1, enemys_list




    #  self.lvl_unlocked = 1
    #  self.dic_lvl = self.import_json()
    #  self.imagen_fondo = pygame.image.load(r"{0}".format(self.dic_lvl["background_image_path"])).convert()
    #  self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
    #  self.plataform_list = create_platforms_json(self.dic_lvl["platforms_list"])
    #  self.rewards_list = create_rewards_json(self.dic_lvl["rewards"]["image_path"], int(self.dic_lvl["rewards"]["width"]), int(self.dic_lvl["rewards"]["height"]), int(self.dic_lvl["rewards"]["vertical_speed"]), int(self.dic_lvl["rewards"]["float_update_rate"]), int(self.dic_lvl["rewards"]["update_rate"]), self.plataform_list)
    #  self.lista_trampas = create_tramps_json(self.plataform_list, self.dic_lvl["tramps"]["path_image"], int(self.dic_lvl["tramps"]["height"]), int(self.dic_lvl["tramps"]["width"]))
    #  self.player_1 = Player(self.dic_lvl["player"], self.dic_lvl["life_bar"], self.dic_lvl["score_table"], difficulty)
    #  self.enemy_list = create_enemys_json(self.plataform_list, self.dic_lvl["enemy"], difficulty)
