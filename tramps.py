import pygame
from constantes import *
import random

class Tramp():
    def __init__(self, path_image, platform, height, width):
        self.image = pygame.image.load(r"{0}".format(path_image))
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(platform[0].rect.x, platform[-1].rect.x)
        self.rect.y = platform[0].rect.y -30
        self.collition_rect_top = pygame.Rect(self.rect.x+15, (self.rect.y+20), (self.rect.w-30), (self.rect.h-30))
        self.collition_rect_left = pygame.Rect((self.rect.x), (self.rect.y+25), (self.rect.w-30), (self.rect.h-35))
        self.collition_rect_right = pygame.Rect((self.rect.x+30), (self.rect.y+25), (self.rect.w-30), (self.rect.h-35))


    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, (200, 0, 0), self.collition_rect_top)
            pygame.draw.rect(screen, (0, 200, 0), self.collition_rect_right)
            pygame.draw.rect(screen, (0, 0, 200), self.collition_rect_left)
        screen.blit(self.image, self.rect)



def create_tramps(platform):
    tramps_list = []
    
    tramps_list_1 = []
    tramps_list_1.append()
    tramps_list_1.append(Tramp(platform[0]))
    
    
    tramps_list_2 = []
    tramps_list_2.append(Tramp(platform[3]))
    tramps_list_2.append(Tramp(platform[3]))
    

    tramps_list.append(tramps_list_1)
    tramps_list.append(tramps_list_2)

    return tramps_list

def create_tramps_json(platforms_list, path_image, height, width):
    tramps_list = []
    for i in range(len(platforms_list)):
        random_number = random.randint(0, 11)
        if (random_number % 2) == 0 and len(platforms_list[i])>3:# and len(platforms_list[i]) > 4:   
            tramp = Tramp(path_image, platforms_list[i], height, width)
            tramps_list.append(tramp)
    return tramps_list

