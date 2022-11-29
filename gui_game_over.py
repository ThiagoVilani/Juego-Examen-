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

    def update(self, mouse_pos, game_over, election, level_elected, playing, pause_button):
        if self.rect_image_back_menu.collidepoint(mouse_pos):
            pause_button.pause = False
            return False, None, False, None
        else:
            return election, level_elected, playing, game_over

    def draw(self, screen):
        screen.blit(self.image_back_menu, self.rect_image_back_menu)