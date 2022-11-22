import pygame
from auxiliar import Auxiliar

class Platform():
    def __init__(self, x, y):
        self.frame = 0
        self.pos_x = x
        self.pos_y = y
        self.image = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\OneDrive\Escritorio\images/tile/sheet1.png",8,8)#[type]
        self.image = pygame.transform.scale(self.image[1],(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y
        self.rect_visual = pygame.Rect(self.rect.x, self.rect.y, self.rect.h, self.rect.w)


    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (20, 200, 200), self.rect_visual)
        screen.blit(self.image, self.rect_visual)