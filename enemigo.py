from auxiliar import Auxiliar
import random
import pygame
from constantes import *
from proyectil import *

class Enemy():
    def __init__(self, x, y, platform, dic_enemy, difficulty):
        self.pos_x = x
        self.pos_y = y
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"{0}".format(dic_enemy["path_image_walk"]), dic_enemy["columns"], dic_enemy["rows"])
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"{0}".format(dic_enemy["path_image_walk"]), dic_enemy["columns"], dic_enemy["rows"], True)
        for i in range(len(self.walk_l)):
            self.walk_l[i] = pygame.transform.scale(self.walk_l[i], (dic_enemy["width"], dic_enemy["height"]))
            self.walk_r[i] = pygame.transform.scale(self.walk_r[i], (dic_enemy["width"], dic_enemy["height"]))
        self.frame = 0
        self.speed_walk = random.randint(dic_enemy["difficulty"][difficulty]["speed_range"][0], dic_enemy["difficulty"][difficulty]["speed_range"][1])
        self.animation = self.walk_l
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.collition_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.w - 50 , self.rect.h - 20)
        self.collition_rect_top = pygame.Rect(self.rect.x + 30, self.rect.y + 6, self.rect.w - 70, self.rect.h - 50)
        self.collition_rect_left = pygame.Rect(self.rect.x + 20, self.rect.y + 30, self.rect.w - 90, self.rect.h - 50)
        self.collition_rect_right = pygame.Rect(self.rect.x - 20, self.rect.y + 30, self.rect.w - 90, self.rect.h - 50)
        self.death = False
        self.lifes = dic_enemy["difficulty"][difficulty]["lifes"]
        if platform == None:
            self.right_limit = ANCHO_VENTANA - 100
            self.left_limit = ANCHO_VENTANA - 1000
        else:            
            self.right_limit = platform[-1].rect.x
            self.left_limit = platform[0].rect.x
   
        self.direction = "left"
        self.magazine = Magazine()
        self.start_time = 0
        self.start_shoot = random.randint(dic_enemy["start_shoot_range"][0], dic_enemy["start_shoot_range"][1])
        self.total_time = 0
        self.shoot_time = 0
        self.update_rate = dic_enemy["update_rate"]
        self.shoot_rate = random.randint(dic_enemy["difficulty"][difficulty]["shoot_rate"][0], dic_enemy["difficulty"][difficulty]["shoot_rate"][1])
        
    
    def shoot(self, delta_ms, sound):
        self.start_time += delta_ms
        self.shoot_time  += delta_ms
        if self.start_shoot < self.start_time:
            if self.shoot_time > self.shoot_rate:
                    self.shoot_time = 0
                    self.magazine.creating_projectiles(self)
                    sound.play_stop("shoot_enemy", None)
                    

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

    def update(self, player, delta_ms, sound):
        self.total_time += delta_ms
        if self.update_rate < self.total_time:
            self.total_time = 0

            #Actualizacion de frames
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

            self.shoot(delta_ms, sound) #Disparo
           
            self.patrolling() #Patrullaje de lado a lado

            self.rect.x = self.pos_x
            self.rect.y = self.pos_y
            self.collition_rect.x = self.pos_x + 20
            self.collition_rect.y = self.pos_y + 6
            self.collition_rect_top.x = self.pos_x + 30
            self.collition_rect_top.y = self.pos_y + 6
            self.collition_rect_left.x = self.pos_x + 20
            self.collition_rect_left.y = self.pos_y + 30
            self.collition_rect_right.x = self.pos_x + 65
            self.collition_rect_right.y = self.pos_y + 30
            
            self.magazine.update(player, sound)
            
            if self.lifes < 1:
                self.death = True

            if self.collition_rect_left.colliderect(player.collition_rect):
                player.lifes -= 1
                player.enemy_collide_left = True
            if self.collition_rect_top.colliderect(player.collition_rect):
                self.lifes = 0
            if self.collition_rect_right.colliderect(player.collition_rect):
                player.lifes -= 1
                player.enemy_collide_right = True
            if self.death == True:
                player.score += 100

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, (200, 0,  0), self.collition_rect)
            pygame.draw.rect(screen, (50, 29, 49), self.collition_rect_top)
            pygame.draw.rect(screen, (200, 29, 249), self.collition_rect_right)
            pygame.draw.rect(screen, (20, 29, 249), self.collition_rect_left)
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
        self.magazine.draw(screen)
        

class Horde():
    def __init__(self):
        self.enemy_list = []
        self.enemy_to_pop = -1

    def update(self, player, delta_ms, sound):
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].update(player, delta_ms, sound)
            if self.enemy_list[i].pos_x < -50:
                self.enemy_list[i].pos_x = ANCHO_VENTANA + 50
            if self.enemy_list[i].death == True:
                self.enemy_to_pop = i
                sound.play_stop("enemy_death", None)
                print("muere enemigo")
        if self.enemy_to_pop != -1:
            self.enemy_list.pop(self.enemy_to_pop)
            self.enemy_to_pop = -1
          
    def draw(self, screen):
        for enemy in self.enemy_list:
            enemy.draw(screen)
        
#def create_enemys_list(plataform_list):
#    enemy = Enemy((ANCHO_VENTANA - 150), 480, None)
#    enemy_2 = Enemy((plataform_list[0][random.randint(0, len(plataform_list[0])-1)].rect.x), 350, plataform_list[0])
#    enemy_3 = Enemy((plataform_list[3][random.randint(0, len(plataform_list[3])-1)].rect.x), 100, plataform_list[3])
#    enemys_list = Horde()
#    enemys_list.enemy_list.append(enemy)
#    enemys_list.enemy_list.append(enemy_2)
#    enemys_list.enemy_list.append(enemy_3)
#    return enemys_list



def create_enemys_json(platforms_list, dic_enemys, difficulty):
    all_enemys = Horde()
    all_enemys.enemy_list.append(Enemy((ANCHO_VENTANA - 150), GROUND_LEVEL-(dic_enemys["height"])+10, None, dic_enemys, difficulty))
    for i in range(len(platforms_list)):
        if len(platforms_list[i]) > 5:
            enemy = Enemy((platforms_list[i][random.randint(0, len(platforms_list[i])-1)].rect.x), platforms_list[i][0].rect.y-(dic_enemys["width"]/2), platforms_list[i], dic_enemys, difficulty)
            all_enemys.enemy_list.append(enemy)
    return all_enemys