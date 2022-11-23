import pygame
from constantes import *
from auxiliar import Auxiliar
import json


class Plataform:
    def __init__(self, x, y,width, height,  type=1):

        self.image_list = Auxiliar.getSurfaceFromSeparateFiles(r"C:\Users\vilan\OneDrive\Escritorio/images_completisimo/images/tileset/forest/Tiles/{0}.png",18,flip=False,w=width,h=height)
        
        self.image = self.image_list[type]
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

    for i in range(len(lista_plataformas)):
        platform = []
        incremento_x = 0
        for a in range(lista_plataformas[i][0]):
            platform.append(Plataform((int(lista_plataformas[i][1]["x"]))+incremento_x,int(lista_plataformas[i][1]["y"]),int(lista_plataformas[i][1]["w"]),int(lista_plataformas[i][1]["h"]),int(lista_plataformas[i][1]["type"])))
            incremento_x += int(lista_plataformas[i][1]["w"])
        platforms_list.append(platform)
    return platforms_list


