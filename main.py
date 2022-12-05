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
from ranking import *
from sounds import *

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.3)
clock = pygame.time.Clock()
game_over = None


###############################
with open(r"C:\Users\vilan\OneDrive\Escritorio\Juego-Examen-\level_one.json") as archivo:
        datita = json.load(archivo)
        dic_level = datita.copy()
difficulty = None
flag_insert_data = False
ranking_table = Ranking_table()
pause_button = Pause_button(dic_button["path_pause_icon"], dic_button["path_play_icon"], int(dic_button["x"]), int(dic_button["y"]), int(dic_button["width"]), int(dic_button["height"]))
pause_screen = Pause_screen(dic_level["pause_screen"]) 
btm_button = Btm_button()
clocky = Clock()
main_screen = Main_screen(dic_level["main_screen"])
election = False
level_elected = None
playing = False
###########################
sounds = Sounds(dic_level["sounds"])
sounds.music.play(-1)


while True:  
    total_time = pygame.time.get_ticks()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pause_button.update(pygame.mouse.get_pos())
            if not playing:
                print("no estaba jugando")
                level_elected, difficulty = main_screen.update(pygame.mouse.get_pos(), sounds)
                clocky.update(None, game_over, pause_button.pause, True)
            else:
                print("estoy jugando")
                election, level_elected, playing = pause_screen.update(pygame.mouse.get_pos(), election, level_elected, playing, pause_button, sounds)
            if game_over != None:
                election, level_elected, playing, game_over, flag_insert_data = btm_button.update(pygame.mouse.get_pos(), game_over, election, level_elected, playing, pause_button, flag_insert_data)

    if not election: 
        main_screen.draw(screen)
        pygame.display.flip()
        
    if level_elected != None:
        print("ya se escogio un nivel")
        election = True
        playing = True
        if level_elected == "one":
            imagen_fondo, rewards_list, plataform_list, lista_trampas, player_1, enemys_list = create_level_one(difficulty)
        elif level_elected == "two":
            imagen_fondo, rewards_list, plataform_list, lista_trampas, player_1, enemys_list = create_level_two(difficulty)
        else:
            imagen_fondo, rewards_list, plataform_list, lista_trampas, player_1, enemys_list = create_level_three(difficulty)
        level_elected = None

    if election:
        delta_ms = clock.tick(FPS)
        game_over = clocky.update(delta_ms, game_over, pause_button.pause, False)
        if game_over == "win" or  game_over == "lose":
            game_over_back(screen)
            game_over_sign(screen, game_over)
            back_to_menu_sign(screen)
            btm_button.draw(screen)
            if not flag_insert_data:
                insert_data("all_score", main_screen.name, player_1.score, "score")
                flag_insert_data = True
                ranking_table.update(read_order_desc("all_score", "score"))
            ranking_table.draw(screen)
            pygame.display.flip()
        else:
            if not pause_button.pause:
                keys = pygame.key.get_pressed()
                #delta_ms = clock.tick(FPS)
                screen.blit(imagen_fondo,imagen_fondo.get_rect())
                pause_button.draw(screen)
                #game_over = clocky.update(delta_ms, game_over)
                clocky.draw(screen)
                for plataforma in plataform_list:
                    for bloque in plataforma:
                        bloque.draw(screen)
                for trampa in lista_trampas:
                    trampa.draw(screen)
                game_over = enemys_list.update(player_1, delta_ms, sounds)
                enemys_list.draw(screen)
                player_1.events(delta_ms,keys, sounds)
                game_over = player_1.update(delta_ms,plataform_list, enemys_list.enemy_list, rewards_list.rewards_list, lista_trampas, sounds)
                player_1.draw(screen)
                rewards_list.update(delta_ms, player_1, sounds)
                rewards_list.draw(screen)
                pygame.display.flip()
                if len(enemys_list.enemy_list) == 0:
                    game_over = "win"
            else:
                pause_button.draw(screen)
                pause_screen.draw(screen)
                pygame.display.flip()
    #print(delta_ms)