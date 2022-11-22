from constantes import *
import pygame

def game_over_back(screen):
    background_image = pygame.image.load(r"C:\Users\vilan\Desktop\images_completisimo\images\gui\jungle\pause/bg.png")
    background_image = pygame.transform.scale(background_image, (ANCHO_VENTANA, ALTO_VENTANA))
    screen.blit(background_image, (0,0))


def game_over_sign(screen, state):
    sign_image_lose = pygame.image.load(r"C:\Users\vilan\Desktop\images_completisimo\images\gui\jungle\you_lose/header.png")
    sign_image_lose = pygame.transform.scale(sign_image_lose, (((ANCHO_VENTANA*50)/100), ((ALTO_VENTANA*40)/100)))
    sign_image_win = pygame.image.load(r"C:\Users\vilan\Desktop\images_completisimo\images\gui\jungle\you_win/header.png")
    sign_image_win = pygame.transform.scale(sign_image_win, (((ANCHO_VENTANA*50)/100), ((ALTO_VENTANA*40)/100))) 
    
    if state == "win":
        screen.blit(sign_image_win, (((ANCHO_VENTANA/2)/2),((ALTO_VENTANA/2)/2)))
    else:
        screen.blit(sign_image_lose, (((ANCHO_VENTANA/2)/2),((ALTO_VENTANA/2)/2)))