import pygame
from constantes import *
from auxiliar import Auxiliar
import json


class Plataform:
    def __init__(self, x, y,width, height, path):
        self.image = pygame.image.load(r"{0}".format(path))
        self.image = pygame.transform.scale(self.image, (width, height))
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
        for a in range(lista_plataformas[i+1][0]):
            platform.append(Plataform((int(lista_plataformas[i+1][1]["x"]))+incremento_x,int(lista_plataformas[i+1][1]["y"]),int(lista_plataformas[i+1][1]["w"]),int(lista_plataformas[i+1][1]["h"]),lista_plataformas[0]["path_platform"]))
            incremento_x += int(lista_plataformas[i+1][1]["w"])
        platforms_list.append(platform)
    return platforms_list


