import pygame
from constantes import *
from auxiliar import Auxiliar



class Plataform:
    def __init__(self, x, y,width, height,  type=1):

        self.image_list= Auxiliar.getSurfaceFromSeparateFiles(r"C:\Users\vilan\OneDrive\Escritorio/images_completisimo/images/tileset/forest/Tiles/{0}.png",18,flip=False,w=width,h=height)
        
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
        
def create_platforms():
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
    return plataform_list

