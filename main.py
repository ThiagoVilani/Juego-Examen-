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
from game_init import *
from level_manager import *

flags = DOUBLEBUF

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.3)
ranking_table, pause_button, pause_screen, btm_button, main_screen, sounds, screen, clocky = game_init(flags)
clock = pygame.time.Clock()
game_over = None
difficulty = None
flag_insert_data = False
flag_game_over = False
election = False
level_elected = None
playing = False
#sounds.music.play(-1)
level_manager = Level_manager()

while True:  
    total_time = pygame.time.get_ticks()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause_button.update(None, True)
        if event.type == pygame.MOUSEBUTTONDOWN:
            sounds.play_stop("click", None)
            pause_button.update(pygame.mouse.get_pos(), False)
            if not playing:
                print("no estaba jugando")
                level_elected, difficulty = main_screen.update(pygame.mouse.get_pos(), sounds)
                clocky.update(None, game_over, pause_button.pause, True)
            else:
                print("estoy jugando")
                election, level_elected, playing = pause_screen.update(pygame.mouse.get_pos(), election, level_elected, playing, pause_button, sounds)
            if game_over != None:
                election, level_elected, playing, game_over, flag_insert_data = btm_button.update(pygame.mouse.get_pos(), game_over, election, level_elected, playing, pause_button, flag_insert_data)

#Lo primero que veo
    if not election: 
        main_screen.draw(screen, level_manager.lvl_unlocked)
        pygame.display.flip()

#Cuando ya elegi el nivel
    if level_elected != None:
        print("ya se eligio un nivel")
        election = True
        playing = True
        if level_elected == "one":
            imagen_fondo, rewards_list, plataform_list, lista_trampas, player_1, enemys_list = level_manager.create_level(difficulty, 1)
     
        elif level_elected == "two":
            try:
                imagen_fondo, rewards_list, plataform_list, lista_trampas, player_1, enemys_list = level_manager.create_level(difficulty, 2)
            except:
                print("no esta el nivel desbloqueado")
                level_elected = None
                election = False
                playing = False
        else:
            try:
                imagen_fondo, rewards_list, plataform_list, lista_trampas, player_1, enemys_list = level_manager.create_level(difficulty, 3)
            except:
                print("no esta el nivel desbloqueado")
                level_elected = None
                election = False
                playing = False
        level_elected = None

#Ya elegi nivel y dificultad
    if election:
        delta_ms = clock.tick(FPS)
        game_over = clocky.update(delta_ms, game_over, pause_button.pause, False)
        #Si se temrino el juego
        if game_over == None:
            flag_game_over = False
        if game_over == "win" or  game_over == "lose":
            if game_over == "win" and not flag_game_over:
                flag_game_over = True
                #if level_manager.lvl_unlocked < 3:
                if level_manager.lvl_playing == level_manager.lvl_unlocked:
                    level_manager.lvl_unlocked += 1
                    print(level_manager.lvl_unlocked)
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
        #Si estoy jugando
        else:
            #Si no esta en pausa
            if not pause_button.pause:
                keys = pygame.key.get_pressed()
                screen.blit(imagen_fondo,imagen_fondo.get_rect())
                pause_button.draw(screen)
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
            #Si esta en pausa
            else:
                pause_button.draw(screen)
                pause_screen.draw(screen)
                pygame.display.flip()
    #print(delta_ms)