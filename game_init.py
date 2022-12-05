from pygame.locals import *
from constantes import *
from gui_main_screen import *
from gui_play_screen import *
from gui_game_over import *
from level_one import *
from level_two import *
from level_three import *
from ranking import *
from sounds import *

with open(r"C:/Users/vilan/OneDrive/Escritorio/Juego-Examen-/game_init.json") as archivo:
        datita = json.load(archivo)
        dic_level = datita["game_settings"].copy()

def game_init(flags):
    screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
    ranking_table = Ranking_table()
    pause_button = Pause_button(dic_button["path_pause_icon"], dic_button["path_play_icon"], int(dic_button["x"]), int(dic_button["y"]), int(dic_button["width"]), int(dic_button["height"]))
    pause_screen = Pause_screen(dic_level["pause_screen"]) 
    btm_button = Btm_button()
    main_screen = Main_screen(dic_level["main_screen"])
    sounds = Sounds(dic_level["sounds"])
    clocky = Clock()
    return ranking_table, pause_button, pause_screen, btm_button, main_screen, sounds, screen, clocky