import pygame
from constantes import *
import random

class Tramp():
    def __init__(self, platform):
        self.image = pygame.image.load(r"C:\Users\vilan\Desktop\images_completisimo\images\tileset\space_ship\Tiles/spike.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(platform[0].rect.x, platform[-1].rect.x)
        self.rect.y = platform[0].rect.y -30


    def update(self):
        pass


    def draw(self, screen):
        if DEBUG:
            pass#pygame.draw.rect(screen, (200, 200, 200), self.collition_rect)
        screen.blit(self.image, self.rect)



def create_tramps(platform):
    tramps_list = []
    
    tramps_list_1 = []
    tramps_list_1.append(Tramp(platform[0]))
    tramps_list_1.append(Tramp(platform[0]))
    tramps_list_1.append(Tramp(platform[0]))
    
    tramps_list_2 = []
    tramps_list_2.append(Tramp(platform[3]))
    tramps_list_2.append(Tramp(platform[3]))
    tramps_list_2.append(Tramp(platform[3]))

    tramps_list.append(tramps_list_1)
    tramps_list.append(tramps_list_2)

    return tramps_list

