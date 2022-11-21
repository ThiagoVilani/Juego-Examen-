import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from plataforma import Plataform, create_platforms
from enemigo import *
from rewards import *
from gui_play_screen import *
from tramps import *

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()
game_over = False

imagen_fondo = pygame.image.load(r"C:\Users\vilan\Desktop\images_completisimo\images\locations\set_bg_01\mountain/all.png").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(x=0,y=410,speed_walk=10,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)
rewards_list = create_rewards()
plataform_list = create_platforms()
pause_button = Pause_button((ANCHO_VENTANA-60), 10, 40, 40)

#  ESTO TAMBIEN HAY QUE SACARLO DE ACA
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
enemy = Enemy((ANCHO_VENTANA - 150), 480, None)
enemy_2 = Enemy((plataform_list[0][random.randint(0, (len(plataform_list[0])))].rect.x), 350, plataform_list[0])
enemy_3 = Enemy((plataform_list[3][random.randint(0, (len(plataform_list[3])))].rect.x), 100, plataform_list[3])
enemys_list = Horde()
enemys_list.enemy_list.append(enemy)
enemys_list.enemy_list.append(enemy_2)
enemys_list.enemy_list.append(enemy_3)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
lista_trampas = create_tramps(plataform_list)


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

    if not pause_button.pause:
        keys = pygame.key.get_pressed()
        delta_ms = clock.tick(FPS)
        screen.blit(imagen_fondo,imagen_fondo.get_rect())
        pause_button.draw(screen)
        for plataforma in plataform_list:
            for bloque in plataforma:
                bloque.draw(screen)
        for lista in lista_trampas:
            for trampa in lista:
                trampa.draw(screen)
        enemys_list.update(player_1, delta_ms)
        enemys_list.draw(screen)
        player_1.events(delta_ms,keys)
        game_over = player_1.update(delta_ms,plataform_list, enemys_list.enemy_list, rewards_list.rewards_list)
        player_1.draw(screen)
        rewards_list.update(delta_ms, player_1)
        rewards_list.draw(screen)
        pygame.display.flip()
    
    #print(delta_ms)

