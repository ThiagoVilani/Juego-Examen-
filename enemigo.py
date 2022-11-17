from auxiliar import Auxiliar
import random
import pygame
from constantes import *
from proyectil import *

class Enemy():
    def __init__(self, x, y, platform):
        self.pos_x = x
        self.pos_y = y
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\Desktop\images\inhabitants\dust\walk_left.png", 8, 1)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"C:\Users\vilan\Desktop\images\inhabitants\dust\walk_left.png", 8, 1, True)
        self.frame = 0
        self.speed_walk = random.randint(5, 10)
        self.animation = self.walk_l
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.collition_rect = pygame.Rect(self.rect.x + 20, self.rect.y + 6, self.rect.w - 45, self.rect.h - 10)
        if platform == None:
            self.right_limit = ANCHO_VENTANA - 100
            self.left_limit = ANCHO_VENTANA - 1000
        else:            
            self.right_limit = platform[-1].rect.x
            self.left_limit = platform[0].rect.x
   
        self.direction = "left"
        self.magazine = Magazine()
        self.start_time = 0
        self.start_shoot = random.randint(5000, 7000)
        self.total_time = 0
        self.shoot_time = 0
        self.update_rate = 50
        self.shoot_rate = random.randint(1500, 2000)
        
    
    def shoot(self, delta_ms):
        self.start_time += delta_ms
        print(self.start_time, "start time")
        self.shoot_time  += delta_ms
        if self.start_shoot < self.start_time:
            if self.shoot_time > self.shoot_rate:
                    self.shoot_time = 0
                    self.magazine.creating_projectiles(self)
                    

    def patrolling(self):
        if self.pos_x > self.right_limit:
            self.direction = "left"
        elif self.pos_x < self.left_limit:
            self.direction = "right"

        if self.direction == "left":
            self.pos_x -= self.speed_walk
            self.animation = self.walk_l
        else:
            self.pos_x += self.speed_walk
            self.animation = self.walk_r

    def update(self, player, delta_ms):
        self.total_time += delta_ms
        if self.update_rate < self.total_time:
            self.total_time = 0

            #Actualizacion de frames
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

            self.shoot(delta_ms) #Disparo
           
            self.patrolling() #Patrullaje de lado a lado

            self.rect.x = self.pos_x
            self.rect.y = self.pos_y
            self.collition_rect.x = self.pos_x + 20
            self.collition_rect.y = self.pos_y + 6
            self.magazine.update(player)

            if self.collition_rect.colliderect(player.collition_rect):
                player.death = True
                if player.direction == DIRECTION_R:
                    player.animation = player.death_r
                else:
                    player.animation = player.death_l



    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, (200, 29, 249), self.collition_rect)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
        self.magazine.draw(screen)
        

class Horde():
    def __init__(self):
        self.enemy_list = []

    def update(self, player, delta_ms):
        for enemy in self.enemy_list:
            enemy.update(player, delta_ms)
            if enemy.pos_x < -50:
                enemy.pos_x = ANCHO_VENTANA + 50
            
    def draw(self, screen):
        for enemy in self.enemy_list:
            enemy.draw(screen)
        