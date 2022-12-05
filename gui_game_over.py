from constantes import *
import pygame

def game_over_back(screen):
    background_image = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images_completisimo\images\gui\jungle\pause/bg.png")
    background_image = pygame.transform.scale(background_image, (ANCHO_VENTANA, ALTO_VENTANA))
    screen.blit(background_image, (0,0))

def game_over_sign(screen, state):
    sign_image_lose = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images_completisimo\images\gui\jungle\you_lose/header.png")
    sign_image_lose = pygame.transform.scale(sign_image_lose, (((ANCHO_VENTANA*50)/100), ((ALTO_VENTANA*40)/100)))
    sign_image_win = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images_completisimo\images\gui\jungle\you_win/header.png")
    sign_image_win = pygame.transform.scale(sign_image_win, (((ANCHO_VENTANA*50)/100), ((ALTO_VENTANA*40)/100))) 
    
    if state == "win":
        screen.blit(sign_image_win, (((ANCHO_VENTANA/2)/2),((ALTO_VENTANA/2)/2)))
    else:
        screen.blit(sign_image_lose, (((ANCHO_VENTANA/2)/2),((ALTO_VENTANA/2)/2)))


def back_to_menu_sign(screen):
    btm_image = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images_completisimo\images\gui/back_to_menu.png")
    btm_image = pygame.transform.scale(btm_image, (ANCHO_VENTANA/5, ALTO_VENTANA/3))
    screen.blit(btm_image, (ANCHO_VENTANA/2, ALTO_VENTANA/1.7))

class Btm_button():
    def __init__(self):
        self.image_back_menu = pygame.image.load(r"C:/Users/vilan/OneDrive/Escritorio/images_completisimo/images/gui/jungle/btn/menu.png")
        self.image_back_menu = pygame.transform.scale(self.image_back_menu, (ANCHO_VENTANA/11,ALTO_VENTANA/8))
        self.rect_image_back_menu = self.image_back_menu.get_rect()
        self.rect_image_back_menu.x = ANCHO_VENTANA/2.5
        self.rect_image_back_menu.y = ALTO_VENTANA/1.5

    def update(self, mouse_pos, game_over, election, level_elected, playing, pause_button, flag_insert_data):
        if self.rect_image_back_menu.collidepoint(mouse_pos):
            pause_button.pause = False
            return False, None, False, None, False
        else:
            return election, level_elected, playing, game_over

    def draw(self, screen):
        screen.blit(self.image_back_menu, self.rect_image_back_menu)



class Ranking_table():
    def __init__(self):
        self.table_image = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images_completisimo\images\gui\jungle\shop/4.png")
        self.table_image = pygame.transform.scale(self.table_image, (ANCHO_VENTANA/4, ALTO_VENTANA/2))
        self.rect_table_image = self.table_image.get_rect()
        self.rect_table_image.x = ANCHO_VENTANA - ((ANCHO_VENTANA*97)/100)
        self.rect_table_image.y = ALTO_VENTANA - ((ALTO_VENTANA*97)/100)

        self.ranking_txt = pygame.image.load(r"C:\Users\vilan\OneDrive\Escritorio\images_completisimo\images\gui\jungle\rating/header.png")
        self.ranking_txt = pygame.transform.scale(self.ranking_txt, (self.rect_table_image.w - (self.rect_table_image.w*10)/100, self.rect_table_image.h - (self.rect_table_image.h*70)/100))
        self.rect_ranking_txt = self.ranking_txt.get_rect()
        self.rect_ranking_txt.x = self.rect_table_image.x
        self.rect_ranking_txt.y = self.rect_table_image.y

        font_FO = pygame.font.SysFont("Fugaz One", int(self.rect_table_image.h/9))


        self.score_txt = font_FO.render("SCORE", True, (255,255,255), None )
        self.rect_score_txt = self.score_txt.get_rect()
        self.rect_score_txt.x = self.rect_table_image.w-(self.rect_table_image.w*75)/100
        self.rect_score_txt.y = self.rect_table_image.h-(self.rect_table_image.h*70)/100

        self.name_txt = font_FO.render("NAME", True, (255,255,255), None )
        self.rect_name_txt = self.name_txt.get_rect()
        self.rect_name_txt.x = self.rect_table_image.w-(self.rect_table_image.w*30)/100
        self.rect_name_txt.y = self.rect_table_image.h-(self.rect_table_image.h*70)/100

        #SCORES
        self.f_pos_score = font_FO.render("", True, (255,0,0), None)
        self.rect_f_pos_score = self.f_pos_score.get_rect()
        self.rect_f_pos_score.x = self.rect_table_image.w-(self.rect_table_image.w*75)/100
        self.rect_f_pos_score.y = self.rect_table_image.h-(self.rect_table_image.h*60)/100

        self.s_pos_score = font_FO.render("", True, (255,0,0), None)
        self.rect_s_pos_score = self.s_pos_score.get_rect()
        self.rect_s_pos_score.x = self.rect_table_image.w-(self.rect_table_image.w*75)/100
        self.rect_s_pos_score.y = self.rect_table_image.h-(self.rect_table_image.h*40)/100

        self.t_pos_score = font_FO.render("", True, (255,0,0), None)
        self.rect_t_pos_score = self.t_pos_score.get_rect()
        self.rect_t_pos_score.x = self.rect_table_image.w-(self.rect_table_image.w*75)/100
        self.rect_t_pos_score.y = self.rect_table_image.h-(self.rect_table_image.h*20)/100
        
        #NAMES
        self.f_pos_name = font_FO.render("", True, (0,0,255), None)
        self.rect_f_pos_name = self.f_pos_name.get_rect()
        self.rect_f_pos_name.x = self.rect_table_image.w-(self.rect_table_image.w*30)/100
        self.rect_f_pos_name.y = self.rect_table_image.h-(self.rect_table_image.h*60)/100

        self.s_pos_name = font_FO.render("", True, (0,0,255), None)
        self.rect_s_pos_name = self.s_pos_name.get_rect()
        self.rect_s_pos_name.x = self.rect_table_image.w-(self.rect_table_image.w*30)/100
        self.rect_s_pos_name.y = self.rect_table_image.h-(self.rect_table_image.h*40)/100

        self.t_pos_name = font_FO.render("", True, (0,0,255), None)
        self.rect_t_pos_name = self.t_pos_name.get_rect()
        self.rect_t_pos_name.x = self.rect_table_image.w-(self.rect_table_image.w*30)/100
        self.rect_t_pos_name.y = self.rect_table_image.h-(self.rect_table_image.h*20)/100

    
    def update(self, ranking_list):
        font_FO = pygame.font.SysFont("Fugaz One", int(self.rect_table_image.h/9))
        if len(ranking_list)>2:
            self.f_pos_name = font_FO.render("{0}".format(ranking_list[0][0]), True, (255,255,255), None)
            self.f_pos_score = font_FO.render("{0}".format(ranking_list[0][1]), True, (255,255,255), None)
            self.s_pos_name = font_FO.render("{0}".format(ranking_list[1][0]), True, (255,255,255), None)
            self.s_pos_score = font_FO.render("{0}".format(ranking_list[1][1]), True, (255,255,255), None)
            self.t_pos_name = font_FO.render("{0}".format(ranking_list[2][0]), True, (255,255,255), None)
            self.t_pos_score = font_FO.render("{0}".format(ranking_list[2][1]), True, (255,255,255), None)
        else:
            if len(ranking_list)>1:
                self.f_pos_name = font_FO.render("{0}".format(ranking_list[0][0]), True, (255,255,255), None)
                self.f_pos_score = font_FO.render("{0}".format(ranking_list[0][1]), True, (255,255,255), None)
                self.s_pos_name = font_FO.render("{0}".format(ranking_list[1][0]), True, (255,255,255), None)
                self.s_pos_score = font_FO.render("{0}".format(ranking_list[1][1]), True, (255,255,255), None)
            else:
                self.f_pos_name = font_FO.render("{0}".format(ranking_list[0][0]), True, (255,255,255), None)
                self.f_pos_score = font_FO.render("{0}".format(ranking_list[0][1]), True, (255,255,255), None)
        
            
        
        


    def draw(self, screen):
        screen.blit(self.table_image, self.rect_table_image)
        screen.blit(self.ranking_txt, self.rect_ranking_txt)
        screen.blit(self.score_txt, self.rect_score_txt)
        screen.blit(self.name_txt, self.rect_name_txt)
        screen.blit(self.f_pos_score, self.rect_f_pos_score)
        screen.blit(self.s_pos_score, self.rect_s_pos_score)
        screen.blit(self.t_pos_score, self.rect_t_pos_score)
        screen.blit(self.f_pos_name, self.rect_f_pos_name)
        screen.blit(self.s_pos_name, self.rect_s_pos_name)
        screen.blit(self.t_pos_name, self.rect_t_pos_name)