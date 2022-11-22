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
        self.collition_rect_top = pygame.Rect(self.rect.x+15, (self.rect.y+20), (self.rect.w-30), (self.rect.h-30))
        self.collition_rect_left = pygame.Rect((self.rect.x), (self.rect.y+25), (self.rect.w-30), (self.rect.h-35))
        self.collition_rect_right = pygame.Rect((self.rect.x+30), (self.rect.y+25), (self.rect.w-30), (self.rect.h-35))


    def update(self):
        pass


    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, (200, 0, 0), self.collition_rect_top)
            pygame.draw.rect(screen, (0, 200, 0), self.collition_rect_right)
            pygame.draw.rect(screen, (0, 0, 200), self.collition_rect_left)
        screen.blit(self.image, self.rect)



def create_tramps(platform):
    tramps_list = []
    
    tramps_list_1 = []
    tramps_list_1.append(Tramp(platform[0]))
    tramps_list_1.append(Tramp(platform[0]))
    
    
    tramps_list_2 = []
    tramps_list_2.append(Tramp(platform[3]))
    tramps_list_2.append(Tramp(platform[3]))
    

    tramps_list.append(tramps_list_1)
    tramps_list.append(tramps_list_2)

    return tramps_list

