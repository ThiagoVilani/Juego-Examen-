from platform import platform
import pygame
from pygame.locals import *
import sys
from constantes import *
from player import Player
from plataforma import Plataform 
from enemigo import *
from rewards import *

flags = DOUBLEBUF

screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()
game_over = False
#enemy.creating_list_projectile(1)
#imagen_game_over = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\game_over.png").convert()

imagen_fondo = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images_completisimo\images\locations\set_bg_01\mountain/all.png").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
player_1 = Player(x=0,y=410,speed_walk=10,speed_run=12,gravity=14,jump_power=30,frame_rate_ms=100,move_rate_ms=50,jump_height=140,p_scale=0.2,interval_time_jump=300)


#           SACAR DE ACA
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
reward_1 = Rewards(700, 350)
reward_2 = Rewards(200, 100)
rewards_list = Rewards_list()
rewards_list.rewards_list.append(reward_1)
rewards_list.rewards_list.append(reward_2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#      HAY QUE SACAR ESTO LO MAS PRONTO POSIBLE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
plataform_list = []

#Plataforma inferior
platform_1 = []
platform_1.append(Plataform(x=600,y=400,width=50,height=50,type=12))
platform_1.append(Plataform(x=650,y=400,width=50,height=50,type=13))
platform_1.append(Plataform(x=700,y=400,width=50,height=50,type=13))
platform_1.append(Plataform(x=750,y=400,width=50,height=50,type=13))
platform_1.append(Plataform(x=800,y=400,width=50,height=50,type=13))
platform_1.append(Plataform(x=850,y=400,width=50,height=50,type=13))
platform_1.append(Plataform(x=900,y=400,width=50,height=50,type=13))
platform_1.append(Plataform(x=950,y=400,width=50,height=50,type=13))
platform_1.append(Plataform(x=1000,y=400,width=50,height=50,type=14))

#Plataforma chiquita inferior
platform_2 = []
platform_2.append(Plataform(x=470,y=220,width=50,height=50,type=12))
platform_2.append(Plataform(x=520,y=220,width=50,height=50,type=14))

#Plataforma chiquita superior
platform_3 = []
platform_3.append(Plataform(x=500,y=330,width=50,height=50,type=12))
platform_3.append(Plataform(x=550,y=330,width=50,height=50,type=14))

#Plataforma grande superior
platform_4 = []
platform_4.append(Plataform(x=50,y=150,width=50,height=50,type=12))
platform_4.append(Plataform(x=100,y=150,width=50,height=50,type=13))
platform_4.append(Plataform(x=150,y=150,width=50,height=50,type=13))
platform_4.append(Plataform(x=200,y=150,width=50,height=50,type=13))
platform_4.append(Plataform(x=250,y=150,width=50,height=50,type=13))
platform_4.append(Plataform(x=300,y=150,width=50,height=50,type=13))
platform_4.append(Plataform(x=350,y=150,width=50,height=50,type=13))
platform_4.append(Plataform(x=400,y=150,width=50,height=50,type=13))
platform_4.append(Plataform(x=450,y=150,width=50,height=50,type=14))

plataform_list.append(platform_1)
plataform_list.append(platform_2)
plataform_list.append(platform_3)
plataform_list.append(platform_4)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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




while True:   
    total_time = pygame.time.get_ticks()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())



    for plataforma in plataform_list:
        for bloque in plataforma:
            bloque.draw(screen)
    enemys_list.update(player_1, delta_ms)
    enemys_list.draw(screen)
    player_1.events(delta_ms,keys)
    game_over = player_1.update(delta_ms,plataform_list, enemys_list.enemy_list, rewards_list.rewards_list)
    player_1.draw(screen)
    rewards_list.update(delta_ms, player_1)
    rewards_list.draw(screen)
    # enemigos update
    # player dibujarlo
    # dibujar todo el nivel
    #if game_over:
    #   screen.blit(imagen_game_over,imagen_fondo.get_rect())

    pygame.display.flip()
    
    #print(delta_ms)

