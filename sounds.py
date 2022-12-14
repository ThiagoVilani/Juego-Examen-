from constantes import *
import pygame

pygame.mixer.init()


class Sounds():
    def __init__(self, dic_sounds):
        self.eat = pygame.mixer.Sound(r"{0}".format(dic_sounds["eat_path"]))
        self.shoot = pygame.mixer.Sound(r"{0}".format(dic_sounds["shoot_path"]))
        self.music = pygame.mixer.Sound(r"{0}".format(dic_sounds["music_path"]))
        self.shoot_enemy = pygame.mixer.Sound(r"{0}".format(dic_sounds["shoot_enemy"]))
        self.impact = pygame.mixer.Sound(r"{0}".format(dic_sounds["impact"]))
        self.click = pygame.mixer.Sound(r"{0}".format(dic_sounds["click"]))
        self.hit_dirt = pygame.mixer.Sound(r"{0}".format(dic_sounds["hit_dirt"]))
        self.enemy_death = pygame.mixer.Sound(r"{0}".format(dic_sounds["enemy_death"]))
        self.sound = True


    def play_stop(self, type, state:bool):
        if self.sound:
            if type == "eat":
                self.eat.play()
            elif type == "shoot":
                self.shoot.play()
            elif type == "shoot_enemy":
                self.shoot_enemy.play()
            elif type == "impact":
                self.impact.play()
            elif type == "click":
                self.click.play()
            elif type == "enemy_death":
                self.enemy_death.play()
                print("sonido muerte enemigo")
        if type == None:
            if state:
                self.music.play(-1)
                self.sound = True
            else:
                self.music.stop()
                self.sound = False
    