from constantes import *
import pygame


class Main_screen():
    def __init__(self, dic_main_screen):
        self.background_image = pygame.image.load(r"{0}".format(dic_main_screen["background_image"]))
        self.background_image = pygame.transform.scale(self.background_image, (ANCHO_VENTANA, ALTO_VENTANA))
        
        self.title_image = pygame.image.load(r"{0}".format(dic_main_screen["title"]["path_image"]))
        self.title_image = pygame.transform.scale(self.title_image, (dic_main_screen["title"]["width"], dic_main_screen["title"]["height"]))
        self.rect_title_image = self.title_image.get_rect()
        self.rect_title_image.x = dic_main_screen["title"]["pos_x"]
        self.rect_title_image.y = dic_main_screen["title"]["pos_y"]

        self.table_image = pygame.image.load(r"{0}".format(dic_main_screen["menu"]["table"]["path_image"]))
        self.table_image = pygame.transform.scale(self.table_image, (dic_main_screen["menu"]["table"]["width"], dic_main_screen["menu"]["table"]["height"]))
        self.rect_table_image = self.table_image.get_rect()
        self.rect_table_image.x = dic_main_screen["menu"]["table"]["pos_x"]
        self.rect_table_image.y = dic_main_screen["menu"]["table"]["pos_y"]
        
        self.header_image = pygame.image.load(r"{0}".format(dic_main_screen["menu"]["header"]["path_image"]))
        self.header_image = pygame.transform.scale(self.header_image, (self.rect_table_image.w - (self.rect_table_image.w/7), self.rect_table_image.h/3))
        self.rect_header_image = self.header_image.get_rect()
        self.rect_header_image.x = self.rect_table_image.x + self.rect_table_image.x/7
        self.rect_header_image.y = self.rect_table_image.y 

        self.l_one_image = pygame.image.load(r"{0}".format(dic_main_screen["menu"]["levels_buttons"]["path_image_lo"]))
        self.l_one_image = pygame.transform.scale(self.l_one_image, (self.rect_table_image.w/5, self.rect_table_image.h/4))
        self.rect_l_one_image = self.l_one_image.get_rect()
        self.rect_l_one_image.x = self.rect_table_image.x + self.rect_table_image.w/6
        self.rect_l_one_image.y = self.rect_table_image.y + self.rect_table_image.h/3


        self.l_two_image = pygame.image.load(r"{0}".format(dic_main_screen["menu"]["levels_buttons"]["path_image_lt"]))
        self.l_two_image = pygame.transform.scale(self.l_two_image, (self.rect_table_image.w/5, self.rect_table_image.h/4))
        self.rect_l_two_image = self.l_two_image.get_rect()
        self.rect_l_two_image.x = self.rect_table_image.x + self.rect_table_image.w/2.5
        self.rect_l_two_image.y = self.rect_table_image.y + self.rect_table_image.h/3
        
        self.l_three_image = pygame.image.load(r"{0}".format(dic_main_screen["menu"]["levels_buttons"]["path_image_lth"]))
        self.l_three_image = pygame.transform.scale(self.l_three_image, (self.rect_table_image.w/5, self.rect_table_image.h/4))
        self.rect_l_three_image = self.l_three_image.get_rect()
        self.rect_l_three_image.x = self.rect_table_image.x + self.rect_table_image.w/1.6
        self.rect_l_three_image.y = self.rect_table_image.y + self.rect_table_image.h/3
        



    def update(self, mouse_pos):
        level_elected = None
        if self.rect_l_one_image.collidepoint(mouse_pos):
            level_elected = "one"
        if self.rect_l_two_image.collidepoint(mouse_pos):
            level_elected = "two"
        if self.rect_l_three_image.collidepoint(mouse_pos):
            level_elected = "three"
        return level_elected

    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, (255, 255, 255), self.rect_header_image)
        screen.blit(self.background_image, (0,0))
        screen.blit(self.title_image, (self.rect_title_image))
        screen.blit(self.table_image, (self.rect_table_image))
        screen.blit(self.header_image, self.rect_header_image)
        screen.blit(self.l_one_image, self.rect_l_one_image)
        screen.blit(self.l_two_image, self.rect_l_two_image)
        screen.blit(self.l_three_image, self.rect_l_three_image)
    # REVISAR CLASE DE FORM, EL JSON QUEDO EN LA LINEA 93


