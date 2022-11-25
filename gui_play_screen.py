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

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Score():
    def __init__(self, x_back, y_back, w_back, h_back, w_number, h_number):
        self.image_back = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images_completisimo\images\gui\jungle/bubble/table.png")
        self.image_back = pygame.transform.scale(self.image_back, (w_back, h_back))
        self.back_rect = self.image_back.get_rect()
        self.back_rect.x = x_back
        self.back_rect.y = y_back
        
        self.image_score = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images/score.png")
        self.image_score = pygame.transform.scale(self.image_score, (130, 90))
        self.score_rect = self.image_score.get_rect()
        self.score_rect.x = self.back_rect.x
        self.score_rect.y = self.back_rect.y - 10
        
        self.numbers_list = []
        
        #Cargo las imagenes de los numeros
        for i in range(9):
            number = pygame.image.load(f"C:/Users/vilan/OneDrive/Escritorio/images_completisimo/images/gui/jungle/bubble/{i}.png")
            number = pygame.transform.scale(number, (w_number, h_number))
            self.numbers_list.append(number)
        

        #Asigno la imagen segun la posicion del numero en el tablero f=first, s=second, t=third
        self.image_number_fpos = self.numbers_list[0]
        self.rect_fpos = self.image_number_fpos.get_rect()
        self.rect_fpos.x = (self.back_rect.x + 20) + ((self.back_rect.w/5)*4)
        self.rect_fpos.y = 20
        
        self.image_number_spos = self.numbers_list[0]
        self.rect_spos = self.image_number_spos.get_rect()
        self.rect_spos.x = (self.back_rect.x + 20) + ((self.back_rect.w/5)*3)
        self.rect_spos.y = 20
        
        self.image_number_tpos = self.numbers_list[0]
        self.rect_tpos = self.image_number_tpos.get_rect()
        self.rect_tpos.x = (self.back_rect.x + 20) + ((self.back_rect.w/5)*2)
        self.rect_tpos.y = 20

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
            self.image_number_tpos = self.image_number_zero
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

    def create_hearts(self, cantidad, x, y, w, h):
        x = x
        for i in range(cantidad):
            x += w
            self.hearts_list.append(Ghost_object(x, y, w, h))
    
    def update(self, entity):
        if 0 < len(self.hearts_list):
            if entity.lifes < len(self.hearts_list):
                self.hearts_list.pop(-1)

    def draw(self, screen):
        for heart in self.hearts_list:
            screen.blit(heart.surface, heart.rect)