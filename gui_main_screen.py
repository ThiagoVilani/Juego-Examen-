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



        self.header_image = pygame.image.load(r"{0}".format(dic_main_screen["menu"]["header"]["path_image"]))
        self.header_image = pygame.transform.scale(self.header_image, (self.rect_table_image.w - (self.rect_table_image.w/7), self.rect_table_image.h/3))
        self.rect_header_image = self.header_image.get_rect()
        self.rect_header_image.centerx = self.rect_table_image.centerx#self.rect_table_image.x + self.rect_table_image.x/7
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
        
#TECLADO
        self.keyboard_image = pygame.image.load(r"{0}".format(dic_main_screen["menu"]["keyboard"]["path_image"]))
        self.keyboard_image = pygame.transform.scale(self.keyboard_image, (ANCHO_VENTANA-((ANCHO_VENTANA*20)/100), ALTO_VENTANA-((ALTO_VENTANA*50)/100)))
        self.rect_keyboard_image = self.keyboard_image.get_rect()
        self.rect_keyboard_image.centerx = ANCHO_VENTANA/2
        self.rect_keyboard_image.centery = ALTO_VENTANA/2

        self.rect_a = pygame.Rect(self.rect_keyboard_image)
        self.rect_a.h = self.rect_a.h/5
        self.rect_a.w = self.rect_a.w/12
        self.rect_a.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*32)/100
        self.rect_a.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100

        self.rect_s = pygame.Rect(self.rect_a)
        self.rect_s.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*115)/100
        self.rect_s.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100

        self.rect_d = pygame.Rect(self.rect_a)
        self.rect_d.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*200)/100
        self.rect_d.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100

        self.rect_f = pygame.Rect(self.rect_a)
        self.rect_f.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*280)/100
        self.rect_f.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100

        self.rect_g = pygame.Rect(self.rect_a)
        self.rect_g.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*360)/100
        self.rect_g.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100

        self.rect_h = pygame.Rect(self.rect_a)
        self.rect_h.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*440)/100
        self.rect_h.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100

        self.rect_j = pygame.Rect(self.rect_a)
        self.rect_j.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*520)/100
        self.rect_j.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100

        self.rect_k = pygame.Rect(self.rect_a)
        self.rect_k.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*600)/100
        self.rect_k.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100

        self.rect_l = pygame.Rect(self.rect_a)
        self.rect_l.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*680)/100
        self.rect_l.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*55)/100

        self.rect_q = pygame.Rect(self.rect_a)
        self.rect_q.x = self.rect_keyboard_image.x 
        self.rect_q.y = self.rect_keyboard_image.y 

        self.rect_w = pygame.Rect(self.rect_a)
        self.rect_w.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*85)/100
        self.rect_w.y = self.rect_keyboard_image.y

        self.rect_e = pygame.Rect(self.rect_a)
        self.rect_e.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*165)/100
        self.rect_e.y = self.rect_keyboard_image.y

        self.rect_r = pygame.Rect(self.rect_a)
        self.rect_r.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*245)/100
        self.rect_r.y = self.rect_keyboard_image.y 

        self.rect_t = pygame.Rect(self.rect_a)
        self.rect_t.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*325)/100
        self.rect_t.y = self.rect_keyboard_image.y

        self.rect_y = pygame.Rect(self.rect_a)
        self.rect_y.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*405)/100
        self.rect_y.y = self.rect_keyboard_image.y

        self.rect_u = pygame.Rect(self.rect_a)
        self.rect_u.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*485)/100
        self.rect_u.y = self.rect_keyboard_image.y 

        self.rect_i = pygame.Rect(self.rect_a)
        self.rect_i.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*565)/100
        self.rect_i.y = self.rect_keyboard_image.y

        self.rect_o = pygame.Rect(self.rect_a)
        self.rect_o.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*645)/100
        self.rect_o.y = self.rect_keyboard_image.y

        self.rect_p = pygame.Rect(self.rect_a)
        self.rect_p.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*725)/100
        self.rect_p.y = self.rect_keyboard_image.y

        self.rect_z = pygame.Rect(self.rect_a)
        self.rect_z.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*90)/100
        self.rect_z.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100

        self.rect_x = pygame.Rect(self.rect_a)
        self.rect_x.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*170)/100
        self.rect_x.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100

        self.rect_c = pygame.Rect(self.rect_a)
        self.rect_c.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*250)/100
        self.rect_c.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100

        self.rect_v = pygame.Rect(self.rect_a)
        self.rect_v.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*330)/100
        self.rect_v.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100

        self.rect_b = pygame.Rect(self.rect_a)
        self.rect_b.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*410)/100
        self.rect_b.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100

        self.rect_n = pygame.Rect(self.rect_a)
        self.rect_n.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*490)/100
        self.rect_n.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100

        self.rect_m = pygame.Rect(self.rect_a)
        self.rect_m.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*570)/100
        self.rect_m.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*100)/100

        self.rect_space = pygame.Rect(self.rect_keyboard_image)
        self.rect_space.h = self.rect_space.h/5
        self.rect_space.w = self.rect_space.w/6
        self.rect_space.x = self.rect_keyboard_image.x + (self.rect_keyboard_image.x*67)/100
        self.rect_space.y = self.rect_keyboard_image.y + (self.rect_keyboard_image.y*150)/100

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
                if self.rect_a.collidepoint(mouse_pos):
                    self.name = "{0}A".format(self.name)
                if self.rect_b.collidepoint(mouse_pos):
                    self.name = "{0}B".format(self.name)
                if self.rect_c.collidepoint(mouse_pos):
                    self.name = "{0}C".format(self.name)
                if self.rect_d.collidepoint(mouse_pos):
                    self.name = "{0}D".format(self.name)
                if self.rect_e.collidepoint(mouse_pos):
                    self.name = "{0}E".format(self.name)
                if self.rect_f.collidepoint(mouse_pos):
                    self.name = "{0}F".format(self.name)
                if self.rect_g.collidepoint(mouse_pos):
                    self.name = "{0}G".format(self.name)
                if self.rect_h.collidepoint(mouse_pos):
                    self.name = "{0}H".format(self.name)
                if self.rect_i.collidepoint(mouse_pos):
                    self.name = "{0}I".format(self.name)
                if self.rect_j.collidepoint(mouse_pos):
                    self.name = "{0}J".format(self.name)
                if self.rect_k.collidepoint(mouse_pos):
                    self.name = "{0}K".format(self.name)
                if self.rect_l.collidepoint(mouse_pos):
                    self.name = "{0}L".format(self.name)
                if self.rect_m.collidepoint(mouse_pos):
                    self.name = "{0}M".format(self.name)
                if self.rect_n.collidepoint(mouse_pos):
                    self.name = "{0}N".format(self.name)
                if self.rect_o.collidepoint(mouse_pos):
                    self.name = "{0}O".format(self.name)
                if self.rect_p.collidepoint(mouse_pos):
                    self.name = "{0}P".format(self.name)
                if self.rect_q.collidepoint(mouse_pos):
                    self.name = "{0}Q".format(self.name)
                if self.rect_r.collidepoint(mouse_pos):
                    self.name = "{0}R".format(self.name)
                if self.rect_s.collidepoint(mouse_pos):
                    self.name = "{0}S".format(self.name)
                if self.rect_t.collidepoint(mouse_pos):
                    self.name = "{0}T".format(self.name)
                if self.rect_u.collidepoint(mouse_pos):
                    self.name = "{0}U".format(self.name)
                if self.rect_v.collidepoint(mouse_pos):
                    self.name = "{0}V".format(self.name)
                if self.rect_w.collidepoint(mouse_pos):
                    self.name = "{0}W".format(self.name)
                if self.rect_x.collidepoint(mouse_pos):
                    self.name = "{0}X".format(self.name)
                if self.rect_y.collidepoint(mouse_pos):
                    self.name = "{0}Y".format(self.name)
                if self.rect_z.collidepoint(mouse_pos):
                    self.name = "{0}Z".format(self.name)
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


    def draw(self, screen):
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
                
               
        



def change_resolution(ancho_ventana, alto_ventana):
    with open(r"C:\Users\vilan\OneDrive\Escritorio\Juego-Examen-\settings.json") as file:
        data = json.load(file)
        dic_settings = data.copy()

    dic_settings["ancho ventana"] = ancho_ventana
    dic_settings["alto ventana"] = alto_ventana

    with open(r"C:\Users\vilan\OneDrive\Escritorio\Juego-Examen-\settings.json", "w") as file:
        json.dump(dic_settings, file)

