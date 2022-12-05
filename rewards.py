from constantes import *
import pygame
import random

class Rewards():
    def __init__(self, pos_x, pos_y, image_path, width_image, height_image, vertical_speed, float_update_rate, update_rate):
        self.image_reward = pygame.image.load(r"{0}.png".format(image_path))
        self.image_reward = pygame.transform.scale(self.image_reward, (width_image, height_image))#37,40
        self.rect_reward = self.image_reward.get_rect()
        self.rect_reward.x = pos_x
        self.rect_reward.y = pos_y
        self.collition_rect = self.rect_reward
        self.vertical_speed = vertical_speed #1
        self.float_update_rate = float_update_rate #70
        self.float_update_time = 0
        self.ate = False
        self.update_rate = update_rate #50
        self.update_time = 0
        self.direction = "up"
        self.float_limitator = 0
        

    def vertical_move(self):
        self.float_update_time = 0
        if self.direction == "up" and self.float_limitator > 10:
            self.float_limitator = 0
            self.direction = "down"
        elif self.direction == "down" and self.float_limitator > 10:
            self.float_limitator = 0
            self.direction = "up"
        if self.direction == "up":
            self.rect_reward.y -= self.vertical_speed
            self.float_limitator += self.vertical_speed
        else:
            self.rect_reward.y += self.vertical_speed
            self.float_limitator += self.vertical_speed


    def update(self, delta_ms, entity, sound):
        self.update_time += delta_ms
        self.float_update_time += delta_ms
        if self.update_time > self.update_rate:
            #Fue comido? # Quizas haya que sacarlo en el futuro cercano
            if self.rect_reward.colliderect(entity.rect):
                self.ate = True   
                entity.fruit_ate = True
                entity.score += 5
                sound.play_stop("eat", None)
                print("BANANA comida")         

            #Movimiento 
            if self.float_update_time > self.float_update_rate:
                self.vertical_move()
            



    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen, (200, 29, 249), self.rect_reward)
        screen.blit(self.image_reward, (self.rect_reward.x, self.rect_reward.y))


class Rewards_list():
    def __init__(self):
        self.rewards_list = []
        self.reward_to_pop = -1

    def update(self, delta_ms, entity, sound):
        for i in range(len(self.rewards_list)):
            self.rewards_list[i].update(delta_ms, entity, sound)
            if self.rewards_list[i].ate == True:
                self.reward_to_pop = i
        if self.reward_to_pop != -1:
            self.rewards_list.pop(self.reward_to_pop)
            self.reward_to_pop = -1
    
    
    def draw(self, screen):
        for reward in self.rewards_list:
            reward.draw(screen)


def create_rewards_json(image_path, width_image, height_image, vertical_speed, float_update_rate, update_rate, plataform_list):
    all_rewards = Rewards_list()
    for i in range(len(plataform_list)):
        random_number = random.randint(0, 11)
        if (random_number % 2) == 0:
            if len(plataform_list[i]) < 4:
                reward = Rewards((plataform_list[i][random.randint(0, len(plataform_list[i])-1)].rect.x), plataform_list[i][0].rect.y - 40, image_path, width_image, height_image, vertical_speed, float_update_rate, update_rate)
                all_rewards.rewards_list.append(reward)
            else:
                for a in range(2):
                    reward = Rewards((plataform_list[i][random.randint(0, len(plataform_list[i])-1)].rect.x), plataform_list[i][0].rect.y - 40, image_path, width_image, height_image, vertical_speed, float_update_rate, update_rate)
                    all_rewards.rewards_list.append(reward)
    return all_rewards