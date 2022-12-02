import pygame
from constantes import *
from auxiliar import Auxiliar
import json


class Plataform:
    def __init__(self, x, y,width, height, path):
        self.image = pygame.image.load(r"{0}".format(path))
        self.image = pygame.transform.scale(self.image, ((ALTO_VENTANA*width)/100, (ALTO_VENTANA*height)/100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        

def create_platforms_json(lista_plataformas):
    platforms_list = []
    for i in range(len(lista_plataformas)-1):
        platform = []
        incremento_x = 0

        platform.append(Plataform((ANCHO_VENTANA*(int(lista_plataformas[i+1][1]["x"])))/100, GROUND_LEVEL - int(lista_plataformas[i+1][1]["y"]),int(lista_plataformas[i+1][1]["w"]),int(lista_plataformas[i+1][1]["h"]),lista_plataformas[0]["path_platform"]))
        incremento_x += (ALTO_VENTANA*(int(lista_plataformas[i+1][1]["w"])))/100
        for a in range((lista_plataformas[i+1][0])-1):
            platform.append(Plataform(platform[0].rect.x+incremento_x, GROUND_LEVEL - int(lista_plataformas[i+1][1]["y"]),int(lista_plataformas[i+1][1]["w"]),int(lista_plataformas[i+1][1]["h"]),lista_plataformas[0]["path_platform"]))
            incremento_x += (ALTO_VENTANA*(int(lista_plataformas[i+1][1]["w"])))/100
        platforms_list.append(platform)
        for e in range(len(platform)):
            print(platform[e].rect.x)
    return platforms_list


