from constantes import *
import pygame
import sys


class Main_screen():
    def __init__(self, dic_main_screen):
#QUIT
        self.quit_image = pygame.image.load(r"{0}".format(dic_main_screen["quit_image"]))
        self.quit_image = pygame.transform.scale(self.quit_image, ((ANCHO_VENTANA*5)/100, (ANCHO_VENTANA*5)/100))
        self.rect_quit_image = self.quit_image.get_rect()
        self.rect_quit_image.centerx = (ANCHO_VENTANA*95)/100
        self.rect_quit_image.y = (ALTO_VENTANA*2)/100       
#QUIT
#IMAGEN y TITULO
        self.background_image = pygame.image.load(r"{0}".format(dic_main_screen["background_image"]))
        self.background_image = pygame.transform.scale(self.background_image, (ANCHO_VENTANA, ALTO_VENTANA))
        
        self.title_image = pygame.image.load(r"{0}".format(dic_main_screen["title"]["path_image"]))
        self.title_image = pygame.transform.scale(self.title_image, (dic_main_screen["title"]["width"], dic_main_screen["title"]["height"]))
        self.rect_title_image = self.title_image.get_rect()
        self.rect_title_image.centerx = ANCHO_VENTANA/2#dic_main_screen["title"]["pos_x"]
        self.rect_title_image.centery = (ALTO_VENTANA*15)/100#dic_main_screen["title"]["pos_y"]
#IMAGEN y TITULO

#TABLA
        self.table_image = pygame.image.load(r"{0}".format(dic_main_screen["menu"]["table"]["path_image"]))
        self.table_image = pygame.transform.scale(self.table_image, ((ANCHO_VENTANA*40)/100, (ANCHO_VENTANA*30)/100))
        self.rect_table_image = self.table_image.get_rect()
        self.rect_table_image.centerx = ANCHO_VENTANA/2#dic_main_screen["menu"]["table"]["pos_x"]
        self.rect_table_image.centery = ALTO_VENTANA/2#dic_main_screen["menu"]["table"]["pos_y"]
#TABLA


#NIVELES
        self.header_image = pygame.image.load(r"{0}".format(dic_main_screen["menu"]["header"]["path_image"]))
        self.header_image = pygame.transform.scale(self.header_image, (self.rect_table_image.w - (self.rect_table_image.w/7), self.rect_table_image.h/3))
        self.rect_header_image = self.header_image.get_rect()
        self.rect_header_image.centerx = self.rect_table_image.centerx#self.rect_table_image.x + self.rect_table_image.x/7
        self.rect_header_image.y = self.rect_table_image.y 

        self.denied_image = pygame.image.load(r"{0}".format(dic_main_screen["menu"]["levels_buttons"]["path_image_lod"]))
        self.denied_image = pygame.transform.scale(self.denied_image, (self.rect_table_image.w/5, self.rect_table_image.h/4))
        self.rect_denied_image = self.denied_image.get_rect()

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
#NIVELES


#TECLADO
        self.keyboard_image = pygame.image.load(r"{0}".format(dic_main_screen["menu"]["keyboard"]["path_image"]))
        self.keyboard_image = pygame.transform.scale(self.keyboard_image, (ANCHO_VENTANA-((ANCHO_VENTANA*20)/100), ALTO_VENTANA-((ALTO_VENTANA*50)/100)))
        self.rect_keyboard_image = self.keyboard_image.get_rect()
        self.rect_keyboard_image.centerx = ANCHO_VENTANA/2
        self.rect_keyboard_image.centery = ALTO_VENTANA/2

        self.letters_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.letters_rect_list = []

        for i in range(26):
            self.letters_rect_list.append(pygame.Rect(self.rect_keyboard_image))
        for i in range(26):
            self.letters_rect_list[i].h = self.letters_rect_list[i].h/5
            self.letters_rect_list[i].w = self.letters_rect_list[i].w/12

        self.letters_rect_list[0].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*32)/100
        self.letters_rect_list[0].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100
        
        self.letters_rect_list[18].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*115)/110
        self.letters_rect_list[18].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100
        
        self.letters_rect_list[3].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*200)/100
        self.letters_rect_list[3].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100
        
        self.letters_rect_list[5].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*280)/100
        self.letters_rect_list[5].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100
        
        self.letters_rect_list[6].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*360)/100
        self.letters_rect_list[6].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100
        
        self.letters_rect_list[7].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*440)/100
        self.letters_rect_list[7].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100
        
        self.letters_rect_list[9].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*520)/100
        self.letters_rect_list[9].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100
        
        self.letters_rect_list[10].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*600)/100
        self.letters_rect_list[10].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100
        
        self.letters_rect_list[11].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*680)/100
        self.letters_rect_list[11].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100
        
        self.letters_rect_list[16].x = self.rect_keyboard_image.x 
        self.letters_rect_list[16].y = self.rect_keyboard_image.y 
        
        self.letters_rect_list[22].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*85)/100
        self.letters_rect_list[22].y = self.rect_keyboard_image.y
        
        self.letters_rect_list[4].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*165)/100
        self.letters_rect_list[4].y = self.rect_keyboard_image.y
        
        self.letters_rect_list[17].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*245)/100
        self.letters_rect_list[17].y = self.rect_keyboard_image.y 
        
        self.letters_rect_list[19].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*325)/100
        self.letters_rect_list[19].y = self.rect_keyboard_image.y
        
        self.letters_rect_list[24].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*405)/100
        self.letters_rect_list[24].y = self.rect_keyboard_image.y
        
        self.letters_rect_list[20].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*485)/100
        self.letters_rect_list[20].y = self.rect_keyboard_image.y 
        
        self.letters_rect_list[8].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*565)/100
        self.letters_rect_list[8].y = self.rect_keyboard_image.y
        
        self.letters_rect_list[14].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*645)/100
        self.letters_rect_list[14].y = self.rect_keyboard_image.y
        
        self.letters_rect_list[15].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*725)/100
        self.letters_rect_list[15].y = self.rect_keyboard_image.y
        
        self.letters_rect_list[25].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*90)/100
        self.letters_rect_list[25].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100
        
        self.letters_rect_list[23].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*170)/100
        self.letters_rect_list[23].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100
        
        self.letters_rect_list[2].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*250)/100
        self.letters_rect_list[2].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100
        
        self.letters_rect_list[21].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*330)/100
        self.letters_rect_list[21].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100
        
        self.letters_rect_list[1].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*410)/100
        self.letters_rect_list[1].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100
        
        self.letters_rect_list[13].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*490)/100
        self.letters_rect_list[13].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100
        
        self.letters_rect_list[12].x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*570)/100
        self.letters_rect_list[12].y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100

        self.rect_input_space = pygame.Rect(self.rect_keyboard_image)
        self.rect_input_space.w = ANCHO_VENTANA - (ANCHO_VENTANA*40)/100
        self.rect_input_space.h = ALTO_VENTANA - (ALTO_VENTANA*90)/100
        self.rect_input_space.centerx = ANCHO_VENTANA/2
        self.rect_input_space.centery = ALTO_VENTANA - (ALTO_VENTANA*20)/100

        self.rect_enter = pygame.Rect(self.rect_keyboard_image)
        self.rect_enter.w = self.rect_enter.w/5
        self.rect_enter.h = self.rect_enter.h/5
        self.rect_enter.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*67)/100
        self.rect_enter.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*150)/100
#TECLADO
        

#SETTING
        self.settings_wheel_image = pygame.image.load(r"{0}".format(dic_main_screen["settings"]["set_wheel_path_image"]))
        self.settings_wheel_image = pygame.transform.scale(self.settings_wheel_image, ((ANCHO_VENTANA*5)/100, (ANCHO_VENTANA*5)/100))
        self.rect_settings_wheel = self.settings_wheel_image.get_rect()
        self.rect_settings_wheel.centerx = (ANCHO_VENTANA*5)/100
        self.rect_settings_wheel.y = (ALTO_VENTANA*2)/100    
        
        self.font_FO = pygame.font.SysFont("Fugaz One", int(self.rect_table_image.h/9))

        self.resolution_txt = self.font_FO.render("Resolution:", True, (255,255,255), None )
        self.rect_resolution_txt = self.resolution_txt.get_rect()
        self.rect_resolution_txt.x = self.rect_table_image.x+(self.rect_table_image.w*10)/100
        self.rect_resolution_txt.y = self.rect_table_image.y+(self.rect_table_image.h*22)/100

        self.oth_sh_txt = self.font_FO.render("1100 x 600", True, (255,255,255), None )
        self.rect_oth_sh_txt = self.oth_sh_txt.get_rect()
        self.rect_oth_sh_txt.x = self.rect_table_image.x+(self.rect_table_image.w*50)/100
        self.rect_oth_sh_txt.y = self.rect_table_image.y+(self.rect_table_image.h*7)/100

        self.othf_eh_txt = self.font_FO.render("1500 x 800", True, (255,255,255), None )
        self.rect_othf_eh_txt = self.othf_eh_txt.get_rect()
        self.rect_othf_eh_txt.x = self.rect_table_image.x+(self.rect_table_image.w*50)/100
        self.rect_othf_eh_txt.y = self.rect_table_image.y+(self.rect_table_image.h*22)/100

        self.othnh_oth_txt = self.font_FO.render("1920 x 1080", True, (255,255,255), None )
        self.rect_othnh_oth_txt = self.othnh_oth_txt.get_rect()
        self.rect_othnh_oth_txt.x = self.rect_table_image.x+(self.rect_table_image.w*50)/100
        self.rect_othnh_oth_txt.y = self.rect_table_image.y+(self.rect_table_image.h*37)/100
        
        self.sound_txt = self.font_FO.render("Sound", True, (255,255,255), None )
        self.rect_sound_txt = self.sound_txt.get_rect()
        self.rect_sound_txt.x = self.rect_table_image.x+(self.rect_table_image.w*10)/100
        self.rect_sound_txt.y = self.rect_table_image.y+(self.rect_table_image.h*60)/100

        self.yes_txt = self.font_FO.render("Yes", True, (255,255,255), None )
        self.rect_yes_txt = self.yes_txt.get_rect()
        self.rect_yes_txt.x = self.rect_table_image.x+(self.rect_table_image.w*70)/100
        self.rect_yes_txt.y = self.rect_table_image.y+(self.rect_table_image.h*60)/100

        self.no_txt = self.font_FO.render("No", True, (255,255,255), None )
        self.rect_no_txt = self.no_txt.get_rect()
        self.rect_no_txt.x = self.rect_table_image.x+(self.rect_table_image.w*50)/100
        self.rect_no_txt.y = self.rect_table_image.y+(self.rect_table_image.h*60)/100

        self.restart_txt = self.font_FO.render("Restart to apply changes", True, (255,0,0), (0,0,0) )
        self.rect_restart_txt = self.restart_txt.get_rect()
        self.rect_restart_txt.x = self.rect_table_image.x+(self.rect_table_image.w*5)/100
        self.rect_restart_txt.y = self.rect_table_image.y+(self.rect_table_image.h*80)/100
#SETTING



#DIFFICULTY
        self.sel_df_txt = self.font_FO.render("SELECT DIFFICULTY", True, (255,255,255), None )
        self.rect_sel_df_txt = self.sel_df_txt.get_rect()
        self.rect_sel_df_txt.centerx = self.rect_table_image.centerx
        self.rect_sel_df_txt.y = self.rect_table_image.y+(self.rect_table_image.h*10)/100

        self.easy_txt = self.font_FO.render("Easy", True, (255,255,255), None )
        self.rect_easy_txt = self.easy_txt.get_rect()
        self.rect_easy_txt.centerx = self.rect_table_image.centerx
        self.rect_easy_txt.y = self.rect_table_image.y+(self.rect_table_image.h*30)/100

        self.medium_txt = self.font_FO.render("Medium", True, (255,255,255), None )
        self.rect_medium_txt = self.medium_txt.get_rect()
        self.rect_medium_txt.centerx = self.rect_table_image.centerx
        self.rect_medium_txt.y = self.rect_table_image.y+(self.rect_table_image.h*50)/100

        self.hard_txt = self.font_FO.render("Hard", True, (255,255,255), None )
        self.rect_hard_txt = self.hard_txt.get_rect()
        self.rect_hard_txt.centerx = self.rect_table_image.centerx
        self.rect_hard_txt.y = self.rect_table_image.y+(self.rect_table_image.h*70)/100
#DIFFICULTY


    
        self.name = ""
        self.has_name = False
        self.has_difficulty = False
        self.difficulty = None
        self.font = pygame.font.Font(None, self.rect_input_space.h)
        self.text_to_impress = None
        self.setting = False
        self.need_to_restart = False


        
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


    def update(self, mouse_pos, sound):
        level_elected = None
        if self.rect_quit_image.collidepoint(mouse_pos):
            pygame.quit()
            sys.exit()
        #ESTAMOS EN EL TECLADO
        if len(self.name) < 3:
            if not self.has_name:
                for i in range(len(self.letters_list)):
                    if self.letters_rect_list[i].collidepoint(mouse_pos):
                        self.name = "{0}{1}".format(self.name, self.letters_list[i])    

                self.text_to_impress = self.font.render(self.name, 0, (255, 255, 255))
        else:
            if self.rect_enter.collidepoint(mouse_pos):
                self.has_name = True
        
        #ESTAMOS ELIGIENDO DIFICULTAD
        if self.has_name:
            if not self.has_difficulty:
                if self.rect_easy_txt.collidepoint(mouse_pos):
                    self.has_difficulty = True
                    self.difficulty = "easy"
                if self.rect_medium_txt.collidepoint(mouse_pos):
                    self.has_difficulty = True
                    self.difficulty = "medium"
                if self.rect_hard_txt.collidepoint(mouse_pos):
                    self.has_difficulty = True
                    self.difficulty = "hard"
            else:
                #ESTAMOS ELIGIENDO NIVEL Y TOCANDO LA CONFIG
                if self.rect_settings_wheel.collidepoint(mouse_pos):
                    if not self.setting:
                        self.setting = True
                    else:
                        self.setting = False
                        self.need_to_restart = False
                    
                if not self.setting:
                    if self.rect_l_one_image.collidepoint(mouse_pos):
                        level_elected = "one"
                    if self.rect_l_two_image.collidepoint(mouse_pos):
                        level_elected = "two"
                    if self.rect_l_three_image.collidepoint(mouse_pos):
                            level_elected = "three"
                else:
                    if self.rect_no_txt.collidepoint(mouse_pos):
                        sound.play_stop(None, False)
                    if self.rect_yes_txt.collidepoint(mouse_pos):
                        sound.play_stop(None, True)
                    if self.rect_oth_sh_txt.collidepoint(mouse_pos):
                        self.need_to_restart = True
                        change_resolution(1100, 600)
                    if self.rect_othf_eh_txt.collidepoint(mouse_pos):
                        self.need_to_restart = True
                        change_resolution(1500, 800)
                    if self.rect_othnh_oth_txt.collidepoint(mouse_pos):
                        self.need_to_restart = True
                        change_resolution(1920, 1080)

        print(self.name)
        return level_elected, self.difficulty


#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


    def draw(self, screen, lvls_unlocked):
        if DEBUG:
            pygame.draw.rect(screen, (255, 255, 255), self.rect_header_image)
        screen.blit(self.background_image, (0,0))
        screen.blit(self.title_image, (self.rect_title_image))
        screen.blit(self.quit_image, self.rect_quit_image)
        if not self.has_name:
            screen.blit(self.keyboard_image, self.rect_keyboard_image)
            pygame.draw.rect(screen, (0, 0, 0), self.rect_input_space)
            if self.text_to_impress != None:
                screen.blit(self.text_to_impress, (self.rect_input_space))
        else:
            if not self.has_difficulty:
                screen.blit(self.table_image, (self.rect_table_image))
                screen.blit(self.sel_df_txt, self.rect_sel_df_txt)
                screen.blit(self.easy_txt, self.rect_easy_txt)
                screen.blit(self.medium_txt, self.rect_medium_txt)
                screen.blit(self.hard_txt, self.rect_hard_txt)
            else:
                screen.blit(self.settings_wheel_image, self.rect_settings_wheel)
                if self.setting:
                    screen.blit(self.table_image, (self.rect_table_image))
                    screen.blit(self.resolution_txt, self.rect_resolution_txt)
                    screen.blit(self.oth_sh_txt, self.rect_oth_sh_txt)
                    screen.blit(self.othf_eh_txt, self.rect_othf_eh_txt)
                    screen.blit(self.othnh_oth_txt, self.rect_othnh_oth_txt)
                    screen.blit(self.sound_txt, self.rect_sound_txt)
                    screen.blit(self.yes_txt, self.rect_yes_txt)
                    screen.blit(self.no_txt, self.rect_no_txt)
                    if self.need_to_restart:
                        screen.blit(self.restart_txt, self.rect_restart_txt)
                else:
                    screen.blit(self.table_image, (self.rect_table_image))
                    screen.blit(self.header_image, self.rect_header_image)
                    screen.blit(self.l_one_image, self.rect_l_one_image)
                    screen.blit(self.l_two_image, self.rect_l_two_image)
                    screen.blit(self.l_three_image, self.rect_l_three_image)
                    if lvls_unlocked<3:
                        screen.blit(self.denied_image, self.rect_l_three_image)
                    if lvls_unlocked<2:
                        screen.blit(self.denied_image, self.rect_l_two_image)
                        screen.blit(self.denied_image, self.rect_l_three_image)
               
        



def change_resolution(ancho_ventana, alto_ventana):
    with open(r"C:\Users\vilan\OneDrive\Escritorio\Juego-Examen-\settings.json") as file:
        data = json.load(file)
        dic_settings = data.copy()

    dic_settings["ancho ventana"] = ancho_ventana
    dic_settings["alto ventana"] = alto_ventana

    with open(r"C:\Users\vilan\OneDrive\Escritorio\Juego-Examen-\settings.json", "w") as file:
        json.dump(dic_settings, file)

