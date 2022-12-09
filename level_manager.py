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
       
    def import_json(self):
        if self.lvl_unlocked == 1:
            path_lvl = "C:\Users\vilan\OneDrive\Escritorio\Juego-Examen-\level_one.json"
        elif self.lvl_unlocked == 2:
            path_lvl = "C:\Users\vilan\OneDrive\Escritorio\Juego-Examen-\level_two.json"
        elif self.lvl_unlocked == 3:
            path_lvl = "C:\Users\vilan\OneDrive\Escritorio\Juego-Examen-\level_three.json"

        with open(r"{0}".format(path_lvl)) as archivo:
            datita = json.load(archivo)
            dic_level = datita.copy()
            return dic_level 
    
    def create_level_one(self, difficulty:str):
        dic_level = self.import_json()
        imagen_fondo = pygame.image.load(r"{0}".format(dic_level["background_image_path"])).convert()
        imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
        plataform_list = create_platforms_json(plataformas)
        rewards_list = create_rewards_json(dic_rewards["image_path"], int(dic_rewards["width"]), int(dic_rewards["height"]), int(dic_rewards["vertical_speed"]), int(dic_rewards["float_update_rate"]), int(dic_rewards["update_rate"]), plataform_list)
        lista_trampas = create_tramps_json(plataform_list, dic_tramps["path_image"], int(dic_tramps["height"]), int(dic_tramps["width"]))
        player_1 = Player(dic_player, dic_life_bar, dic_score_table, difficulty)
        enemys_list = create_enemys_json(plataform_list, dic_enemys, difficulty)
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
