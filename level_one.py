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

with open(r"C:\Users\vilan\OneDrive\Escritorio\Juego-Examen-\plataformas_level_one.json") as archivo:
        data = json.load(archivo)
        dic_plataformas = data.copy()
plataformas = dic_plataformas["platforms_list"]


def create_level_one():
    imagen_fondo = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images_completisimo\images\locations\set_bg_01\mountain/all.png").convert()
    imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
    rewards_list = create_rewards("C:/Users/vilan/OneDrive/Escritorio/images_completisimo/images/food/banana/banana__x1_iconic_png_1354829403")
    plataform_list = create_platforms_json(plataformas)
    pause_button = Pause_button((ANCHO_VENTANA-60), 10, 40, 40)
    lista_trampas = create_tramps(plataform_list)
    player_1 = Player(x=0,y=410,speed_walk=10,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)
    enemys_list = create_enemys_list(plataform_list)
    return imagen_fondo, rewards_list, plataform_list, pause_button, lista_trampas, player_1, enemys_list