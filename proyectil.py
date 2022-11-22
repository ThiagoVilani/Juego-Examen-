from constantes import *
import pygame

class Projectile():
    def __init__(self, enemigo):
        self.image_projectile = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images_completisimo\images\chemistry\blue_bubble/blue_bubble__x1_iconic_png_1354829722.png")
        self.image_projectile = pygame.transform.scale(self.image_projectile,(10,10))
        try:
            self.pos_x = enemigo.pos_x
            self.pos_y = enemigo.pos_y + (enemigo.rect.h/2)
        except:
            self.pos_x = enemigo.rect.x
            self.pos_y = enemigo.rect.y + (enemigo.rect.h/2)
        self.rect_projectile = self.image_projectile.get_rect()
        self.rect_projectile.x = self.pos_x
        self.rect_projectile.y = self.pos_y

        self.direction = enemigo.direction
        if enemigo.direction == 1:
            self.direction = "right"
        elif enemigo.direction == 0:
            self.direction = "left"
        
        self.surface = self.image_projectile
        self.speed = 20


    def update(self):
        if self.direction == "left":
            self.pos_x -= self.speed
            self.rect_projectile.x = self.pos_x
            self.rect_projectile.y = self.pos_y
        else:
            self.pos_x += self.speed
            self.rect_projectile.x = self.pos_x
            self.rect_projectile.y = self.pos_y

    def draw(self, screen):
        screen.blit(self.surface, (self.pos_x, self.pos_y))




class Magazine():
    def __init__(self):
        self.list_projectiles = []
        self.projectile_to_pop = -1
    
    def creating_projectiles(self, entity):
        projectile = Projectile(entity)
        self.list_projectiles.append(projectile)
    
    def update(self, player):
        for i in range(len(self.list_projectiles)):
            self.list_projectiles[i].update()
            if self.list_projectiles[i].rect_projectile.colliderect(player.collition_rect):
                self.projectile_to_pop = i
                print("COLISION")
                player.lifes -= 1
                
        if self.projectile_to_pop != -1:
            self.list_projectiles.pop(self.projectile_to_pop)
            self.projectile_to_pop = -1


    def draw(self, screen):
        
        for projectile in self.list_projectiles:
            if DEBUG:
                pygame.draw.rect(screen, (200, 29, 249), projectile.rect_projectile)
            projectile.draw(screen)
