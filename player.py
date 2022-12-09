import pygame
from constantes import *
from auxiliar import Auxiliar
from proyectil import *
from gui_play_screen import *

class Player:
    #def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height, path_image_stay, path_image_jump, path_image_walk, path_image_shoot, path_image_knife, path_image_death, p_scale=1,interval_time_jump=100) -> None:
    def __init__(self, dic_player, dic_life_bar, dic_score_table, difficulty) -> None:

        '''
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("images/caracters/stink/walk.png",15,1,scale=p_scale)[:12]
        '''

        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles(r"{0}".format(dic_player["animations_frames"]["stay"]["path_image_stay"]), dic_player["animations_frames"]["stay"]["quantity"], flip=False, scale=dic_player["settings"]["p_scale"])
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles(r"{0}".format(dic_player["animations_frames"]["stay"]["path_image_stay"]), dic_player["animations_frames"]["stay"]["quantity"], flip=True, scale=dic_player["settings"]["p_scale"])
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles(r"{0}".format(dic_player["animations_frames"]["jump"]["path_image_jump"]), dic_player["animations_frames"]["jump"]["quantity"], flip=False, scale=dic_player["settings"]["p_scale"])
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles(r"{0}".format(dic_player["animations_frames"]["jump"]["path_image_jump"]), dic_player["animations_frames"]["jump"]["quantity"], flip=True, scale=dic_player["settings"]["p_scale"])
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles(r"{0}".format(dic_player["animations_frames"]["walk"]["path_image_walk"]), dic_player["animations_frames"]["walk"]["quantity"], flip=False, scale=dic_player["settings"]["p_scale"])
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles(r"{0}".format(dic_player["animations_frames"]["walk"]["path_image_walk"]), dic_player["animations_frames"]["walk"]["quantity"], flip=True, scale=dic_player["settings"]["p_scale"])
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles(r"{0}".format(dic_player["animations_frames"]["shoot"]["path_image_shoot"]), dic_player["animations_frames"]["shoot"]["quantity"], flip=False, scale=dic_player["settings"]["p_scale"], repeat_frame=2)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles(r"{0}".format(dic_player["animations_frames"]["shoot"]["path_image_shoot"]), dic_player["animations_frames"]["shoot"]["quantity"], flip=True, scale=dic_player["settings"]["p_scale"], repeat_frame=2)
        self.knife_r = Auxiliar.getSurfaceFromSeparateFiles(r"{0}".format(dic_player["animations_frames"]["knife"]["path_image_knife"]), dic_player["animations_frames"]["knife"]["quantity"], flip=False, scale=dic_player["settings"]["p_scale"], repeat_frame=1)
        self.knife_l = Auxiliar.getSurfaceFromSeparateFiles(r"{0}".format(dic_player["animations_frames"]["knife"]["path_image_knife"]), dic_player["animations_frames"]["knife"]["quantity"], flip=True, scale=dic_player["settings"]["p_scale"], repeat_frame=1)
        self.death_l = Auxiliar.getSurfaceFromSeparateFiles(r"{0}".format(dic_player["animations_frames"]["death"]["path_image_death"]), dic_player["animations_frames"]["death"]["quantity"], flip=True, scale=dic_player["settings"]["p_scale"])
        self.death_r = Auxiliar.getSurfaceFromSeparateFiles(r"{0}".format(dic_player["animations_frames"]["death"]["path_image_death"]), dic_player["animations_frames"]["death"]["quantity"], flip=False, scale=dic_player["settings"]["p_scale"])
        
        self.flag_sound_dirt = False
        self.name = None
        self.score_table = Score(dic_score_table)
        self.score = 0
        self.fruit_ate = False
        self.enemy_collide_left = False
        self.enemy_collide_right = False
        self.enemy_collide_top = False
        self.tramp_collide_left = False
        self.tramp_collide_right = False
        self.tramp_collide_top = False
        self.lifes = dic_player["settings"]["difficulty"][difficulty]["lifes"]
        self.life_bar = Life_bar()
        self.life_bar.create_hearts(self.lifes, dic_life_bar)
        self.magazine = Magazine()
        self.high_time = 0
        self.flag_high = False
        self.flag_death_frame = False
        self.death_animation_time = 0
        self.death_time = False
        self.death = False
        self.frame = 0
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  dic_player["settings"]["speed_walk"]
        self.speed_run =  dic_player["settings"]["speed_run"]
        self.gravity = dic_player["settings"]["gravity"]
        self.jump_power = dic_player["settings"]["jump_power"]
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = dic_player["settings"]["pos_x"]
        self.rect.y = dic_player["settings"]["pos_y"]
        self.collition_rect = pygame.Rect(dic_player["settings"]["pos_x"]+self.rect.width/3, dic_player["settings"]["pos_y"], self.rect.width/3, self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = dic_player["settings"]["pos_y"] + self.rect.height - GROUND_COLLIDE_H
        

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False
        
        self.shoot_cooldown = 500
        self.time_shoot_cooldown = 0
        self.update_rate = 50
        self.total_time = 0
        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = dic_player["settings"]["frame_rate_ms"]
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = dic_player["settings"]["move_rate_ms"]
        self.y_start_jump = 0
        self.jump_height = dic_player["settings"]["jump_height"]

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = dic_player["settings"]["interval_time_jump"]



    def collide_tramp(self, tramp_list):
        for tramp in tramp_list:
            if self.collition_rect.colliderect(tramp.collition_rect_top):
                self.lifes = 0
            if self.collition_rect.colliderect(tramp.collition_rect_right):
                self.change_x(50)
            if self.collition_rect.colliderect(tramp.collition_rect_left):
                self.change_x(-50)
                    


    def eating_fruits(self, delta_ms):
        if self.fruit_ate and not self.flag_high:
            self.speed_walk += 10
            self.flag_high = True
            self.fruit_ate = False
            print("mas rapida")
        if self.flag_high:
            self.high_time += delta_ms
        if self.high_time > 3000:
            self.high_time = 0
            self.flag_high = False
            self.speed_walk -= 10
            print("termino el efecto")

    def walk(self,direction):
        if not self.death:
            if(self.is_jump == False and self.is_fall == False):
                if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                    self.frame = 0
                    self.direction = direction
                    if(direction == DIRECTION_R):
                        self.move_x = self.speed_walk
                        self.animation = self.walk_r
                    else:
                        self.move_x = -self.speed_walk
                        self.animation = self.walk_l
        else:
            self.death_animation()


    def shoot(self,on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l  
    
    def fire(self, sound):
        print("dispara")
        self.magazine.creating_projectiles(self)
        sound.play_stop("shoot", None)

    def knife(self,on_off = True):
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                else:
                    self.animation = self.knife_l      

    def death_animation(self):
        if self.direction == DIRECTION_R:
            self.animation = self.death_r
        else:
            self.animation = self.death_l
        if not self.flag_death_frame:
            self.flag_death_frame = True
            self.frame = 0

    def jump(self,on_off = True, plataform_list=None):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

        
    

    def stay(self):
        if not self.death:
            if(self.is_knife or self.is_shoot):
                return

            if(self.animation != self.stay_r and self.animation != self.stay_l):
                if(self.direction == DIRECTION_R):
                    self.animation = self.stay_r
                else:
                    self.animation = self.stay_l
                self.move_x = 0
                self.move_y = 0
                self.frame = 0
        if self.death:
            self.death_animation()

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        if not self.death or (self.death and self.is_fall) or (self.death and self.is_jump):
            self.tiempo_transcurrido_move += delta_ms
            if(self.tiempo_transcurrido_move >= self.move_rate_ms):
                self.tiempo_transcurrido_move = 0
                if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                    self.move_y = 0
            
                self.change_x(self.move_x)
                self.change_y(self.move_y)

                if(not self.is_on_plataform(plataform_list)):
                    if(self.move_y == 0):
                        self.is_fall = True
                        self.change_y(self.gravity)
                else:
                    if (self.is_jump): 
                        self.jump(False, plataform_list)
                    self.is_fall = False            

    def is_on_plataform(self,plataform_list):
        retorno = False
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True  
        else:
            for plataforma in  plataform_list:
                for bloque in plataforma:
                    if(self.ground_collition_rect.colliderect(bloque.ground_collition_rect)):
                        retorno = True
                        break       
        return retorno                 

    def do_animation(self,delta_ms):
        if not self.death or (self.death and self.is_fall and self.is_jump):
            self.tiempo_transcurrido_animation += delta_ms
            if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
                self.tiempo_transcurrido_animation = 0
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else:
                    self.frame = 0
        if self.death and not self.is_fall and not self.is_jump:
            self.death_animation_time += delta_ms
            if self.death_animation_time > 800:
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1 
                else:
                    self.death_time = True

    
    def enemy_push_me(self):
        if self.enemy_collide_left:
            self.change_x(-50)
            self.enemy_collide_left = False
        if self.enemy_collide_right:
            self.change_x(50)
            self.enemy_collide_right = False
        

    def update(self,delta_ms,plataform_list, enemys_list, rewards_list, tramp_list, sound):
        self.total_time += delta_ms
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        
        if self.update_rate < self.total_time:
            if not self.death:
                self.enemy_push_me()
            for enemy in enemys_list:
                self.total_time = 0
                self.magazine.update(enemy, sound)

            self.eating_fruits(delta_ms)
            self.collide_tramp(tramp_list)
            self.life_bar.update(self)
            self.score_table.update(self)

        if self.lifes < 1:
            self.death = True
        if self.death and self.death_time:
            return "lose"
       
    
    
    def draw(self,screen):
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        if not self.death:
            pass                 
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        self.magazine.draw(screen)
        self.life_bar.draw(screen)
        self.score_table.draw(screen)


    def events(self,delta_ms,keys, sound):
        self.tiempo_transcurrido += delta_ms

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

        if(not keys[pygame.K_a]):
            self.shoot(False)  

        if(not keys[pygame.K_a]):
            self.knife(False)  

        if(keys[pygame.K_s] and not keys[pygame.K_a]):
            self.time_shoot_cooldown += delta_ms
            self.shoot()   
            if self.shoot_cooldown < self.time_shoot_cooldown:
                self.fire(sound)
                self.time_shoot_cooldown = 0
                 
        if(keys[pygame.K_a] and not keys[pygame.K_s]):
            self.knife()   