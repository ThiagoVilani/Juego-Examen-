import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_main_screen import *
from gui_play_screen import *
from gui_game_over import *
from level_one import *
from level_two import *
from level_three import *

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()
game_over = None

###############################
with open(r"C:\Users\vilan\OneDrive\Escritorio\Juego-Examen-\level_one.json") as archivo:
        datita = json.load(archivo)
        dic_level = datita.copy()
###############################


pause_button = Pause_button(dic_button["path_pause_icon"], dic_button["path_play_icon"], int(dic_button["x"]), int(dic_button["y"]), int(dic_button["width"]), int(dic_button["height"]))
pause_screen = Pause_screen(dic_level["pause_screen"]) 
btm_button = Btm_button()
###########################
main_screen = Main_screen(dic_level["main_screen"])
election = False
level_elected = None
playing = False
###########################



while True:  
    total_time = pygame.time.get_ticks()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("presiono mouse")
            pause_button.update(pygame.mouse.get_pos())
            if not playing:
                print("no estaba jugando")
                level_elected = main_screen.update(pygame.mouse.get_pos())
            else:
                print("estoy jugando")
                election, level_elected, playing = pause_screen.update(pygame.mouse.get_pos(), election, level_elected, playing, pause_button)
            if game_over != None:
                election, level_elected, playing, game_over = btm_button.update(pygame.mouse.get_pos(), game_over, election, level_elected, playing, pause_button)

    if not election:
        print("viendo main screen")
        main_screen.draw(screen)
        pygame.display.flip()
    if level_elected != None:
        print("ya se escogio un nivel")
        election = True
        playing = True
        if level_elected == "one":
            imagen_fondo, rewards_list, plataform_list, lista_trampas, player_1, enemys_list = create_level_one()
        elif level_elected == "two":
            imagen_fondo, rewards_list, plataform_list, lista_trampas, player_1, enemys_list = create_level_two()
        else:
            imagen_fondo, rewards_list, plataform_list, lista_trampas, player_1, enemys_list = create_level_three()
        level_elected = None

    if election:
        if game_over == "win" or  game_over == "lose":
            game_over_back(screen)
            game_over_sign(screen, game_over)
            back_to_menu_sign(screen)
            btm_button.draw(screen)
            pygame.display.flip()
        else:
            if not pause_button.pause:
                keys = pygame.key.get_pressed()
                delta_ms = clock.tick(FPS)
                screen.blit(imagen_fondo,imagen_fondo.get_rect())
                pause_button.draw(screen)
                for plataforma in plataform_list:
                    for bloque in plataforma:
                        bloque.draw(screen)
                for trampa in lista_trampas:
                    trampa.draw(screen)
                game_over = enemys_list.update(player_1, delta_ms)
                enemys_list.draw(screen)
                player_1.events(delta_ms,keys)
                game_over = player_1.update(delta_ms,plataform_list, enemys_list.enemy_list, rewards_list.rewards_list, lista_trampas)
                player_1.draw(screen)
                rewards_list.update(delta_ms, player_1)
                rewards_list.draw(screen)
                pygame.display.flip()
                if len(enemys_list.enemy_list) == 0:
                    game_over = "win"
            else:
                pause_button.draw(screen)
                pause_screen.draw(screen)
                pygame.display.flip()
    #print(delta_ms)