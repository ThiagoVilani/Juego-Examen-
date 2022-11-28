import pygame
from pygame.locals import *
import sys
from constantes import *
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

#imagen_fondo, rewards_list, plataform_list, pause_button, lista_trampas, player_1, enemys_list = create_level_one()
#imagen_fondo, rewards_list, plataform_list, pause_button, lista_trampas, player_1, enemys_list = create_level_two()
imagen_fondo, rewards_list, plataform_list, pause_button, lista_trampas, player_1, enemys_list = create_level_three()


while True:   
    total_time = pygame.time.get_ticks()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pause_button.update(pygame.mouse.get_pos())
    
    pause_button.draw(screen)
    pygame.display.flip()

    if game_over == "win" or  game_over == "lose":
        game_over_back(screen)
        game_over_sign(screen, game_over)
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

    #print(delta_ms)

