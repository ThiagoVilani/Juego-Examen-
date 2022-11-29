from constantes import *
import pygame

class Pause_button():
    def __init__(self, path_pause_image, path_play_image, x, y, w, h):
        self.surface_pause = pygame.image.load(r"{0}".format(path_pause_image))
        self.surface_pause = pygame.transform.scale(self.surface_pause,(w, h))
        self.surface_play = pygame.image.load(r"{0}".format(path_play_image))
        self.surface_play = pygame.transform.scale(self.surface_play,(w, h))
        self.surface = self.surface_pause
        self.rect = self.surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pause = False

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if self.pause:
                self.surface = self.surface_pause
                self.pause = False
            else:
                self.surface = self.surface_play
                self.pause = True

    def draw(self, screen):
        screen.blit(self.surface, self.rect)


class Pause_screen():
    def __init__(self, dic_pause_screen):
        self.image_table = pygame.image.load(r"{0}".format(dic_pause_screen["table"]["path_image"]))
        self.image_table = pygame.transform.scale(self.image_table, (dic_pause_screen["table"]["width"], dic_pause_screen["table"]["height"]))
        self.rect_image_table = self.image_table.get_rect()
        self.rect_image_table.x = dic_pause_screen["table"]["pos_x"]
        self.rect_image_table.y = dic_pause_screen["table"]["pos_y"]

        self.image_pause = pygame.image.load(r"{0}".format(dic_pause_screen["pause"]["path_image"]))
        self.image_pause = pygame.transform.scale(self.image_pause, (self.rect_image_table.w - self.rect_image_table.w/4, self.rect_image_table.h/3))
        self.rect_image_pause = self.image_pause.get_rect()
        self.rect_image_pause.x = self.rect_image_table.x + (self.rect_image_table.x/9)
        self.rect_image_pause.y = self.rect_image_table.y

        self.image_back_menu = pygame.image.load(r"{0}".format(dic_pause_screen["back_menu"]["path_image"]))
        self.image_back_menu = pygame.transform.scale(self.image_back_menu, (self.rect_image_table.w/4, self.rect_image_table.h/4))
        self.rect_image_back_menu = self.image_back_menu.get_rect()
        self.rect_image_back_menu.x = self.rect_image_table.x + (self.rect_image_table.w/5)
        self.rect_image_back_menu.y = self.rect_image_table.y + (self.rect_image_table.h/2.5)

        self.image_sound = pygame.image.load(r"{0}".format(dic_pause_screen["sound"]["path_image"]))
        self.image_sound = pygame.transform.scale(self.image_sound, (self.rect_image_table.w/4, self.rect_image_table.h/4))
        self.rect_image_sound = self.image_sound.get_rect()
        self.rect_image_sound.x = self.rect_image_table.x + (self.rect_image_table.w/2)
        self.rect_image_sound.y = self.rect_image_table.y + (self.rect_image_table.h/2.5)

    
    def update(self, mouse_pos, election, level_elected, playing, pause_button):
        if self.rect_image_back_menu.collidepoint(mouse_pos):
            pause_button.pause = False
            return False, None, False
        else:
            return election, level_elected, playing


    def draw(self, screen):
        screen.blit(self.image_table, self.rect_image_table)
        screen.blit(self.image_pause, self.rect_image_pause)
        screen.blit(self.image_back_menu, self.rect_image_back_menu)
        screen.blit(self.image_sound, self.rect_image_sound)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Score():
    def __init__(self, dic_score_table):
        self.image_back = pygame.image.load(r"{0}".format(dic_score_table["path_image_back"]))
        self.image_back = pygame.transform.scale(self.image_back, (dic_score_table["w_back"], dic_score_table["h_back"]))
        self.back_rect = self.image_back.get_rect()
        self.back_rect.x = dic_score_table["x_back"]
        self.back_rect.y = dic_score_table["y_back"]
        
        self.image_score = pygame.image.load(r"{0}".format(dic_score_table["path_image_score"]))
        self.image_score = pygame.transform.scale(self.image_score, (dic_score_table["w_score"], dic_score_table["h_score"]))
        self.score_rect = self.image_score.get_rect()
        self.score_rect.x = self.back_rect.x
        self.score_rect.y = self.back_rect.y - 10
        
        self.numbers_list = []
        
        #Cargo las imagenes de los numeros
        for i in range(9):
            #number = pygame.image.load(f"{0}".format(dic_score_table["numbers"]["path_image_numbers"]))
            number = pygame.image.load(r"{0}{1}.png".format(dic_score_table["numbers"]["path_image_numbers"], i))
            number = pygame.transform.scale(number, (dic_score_table["numbers"]["w_number"], dic_score_table["numbers"]["h_number"]))
            self.numbers_list.append(number)
        

        #Asigno la imagen segun la posicion del numero en el tablero f=first, s=second, t=third
        self.image_number_fpos = self.numbers_list[0]
        self.rect_fpos = self.image_number_fpos.get_rect()
        self.rect_fpos.x = (self.back_rect.x + 20) + ((self.back_rect.w/5)*4)
        self.rect_fpos.y = self.back_rect.y + (self.back_rect.h/3)
        
        self.image_number_spos = self.numbers_list[0]
        self.rect_spos = self.image_number_spos.get_rect()
        self.rect_spos.x = (self.back_rect.x + 20) + ((self.back_rect.w/5)*3)
        self.rect_spos.y = self.back_rect.y + (self.back_rect.h/3)
        
        self.image_number_tpos = self.numbers_list[0]
        self.rect_tpos = self.image_number_tpos.get_rect()
        self.rect_tpos.x = (self.back_rect.x + 20) + ((self.back_rect.w/5)*2)
        self.rect_tpos.y = self.back_rect.y + (self.back_rect.h/3)

    def update(self, entity):
        score = str(entity.score)
        score = list(score)
        print(score)
        if len(score) == 1:
            self.image_number_fpos = self.numbers_list[entity.score]
            self.image_number_spos = self.numbers_list[0]
            self.image_number_tpos = self.numbers_list[0]
        
        if len(score) == 2:
            self.image_number_fpos = self.numbers_list[int(score[-1])]
            self.image_number_spos = self.numbers_list[int(score[-2])]
            self.image_number_tpos = self.numbers_list[0]
        if len(score) == 3:
            self.image_number_fpos = self.numbers_list[int(score[-1])]
            self.image_number_spos = self.numbers_list[int(score[-2])]
            self.image_number_tpos = self.numbers_list[int(score[-3])]

    def draw(self, screen):
        screen.blit(self.image_back, self.back_rect)
        screen.blit(self.image_score, self.score_rect)
        screen.blit(self.image_number_fpos, self.rect_fpos)
        screen.blit(self.image_number_spos, self.rect_spos)
        screen.blit(self.image_number_tpos, self.rect_tpos)
        


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Ghost_object():
    def __init__(self, x, y, w, h):
        self.surface = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images_completisimo\images\gui\jungle\upgrade\heart.png")
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

    def create_hearts(self, quantity, dic_life_bar):
        x = dic_life_bar["pos_x"]
        for i in range(quantity):
            x += dic_life_bar["width"]
            self.hearts_list.append(Ghost_object(x, dic_life_bar["pos_y"], dic_life_bar["width"], dic_life_bar["height"]))
    
    def update(self, entity):
        if 0 < len(self.hearts_list):
            if entity.lifes < len(self.hearts_list):
                self.hearts_list.pop(-1)

    def draw(self, screen):
        for heart in self.hearts_list:
            screen.blit(heart.surface, heart.rect)


