from constantes import *
import pygame

class Button():
    def __init__(self, x, y, w, h):
        self.surface = pygame.image.load(r"C:\Users\vilan\Desktop\images_completisimo\images\gui\jungle\btn/pause.png")
        self.surface = pygame.transform.scale(self.surface,(w, h))
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pause = False

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if self.pause:
                self.pause = False
            else:
                self.pause = True

    def draw(self, screen):
        screen.blit(self.surface, self.rect)


class Ghost_object():
    def __init__(self, x, y, w, h):
        self.surface = pygame.image.load(r"C:\Users\vilan\Desktop\images_completisimo\images\gui\jungle\upgrade\heart.png")
        self.surface = pygame.transform.scale(self.surface,(w, h))
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.surface, self.rect)
        

class Life_bar():
    def __init__(self):
        self.hearts_list = []

    def create_hearts(self, cantidad, x, y, w, h):
        x = x
        for i in range(cantidad):
            x += w
            self.hearts_list.append(Ghost_object(x, y, w, h))
    
    def update(self):
        pass

    def draw(self, screen):
        for heart in self.hearts_list:
            screen.blit(heart.surface, heart.rect)