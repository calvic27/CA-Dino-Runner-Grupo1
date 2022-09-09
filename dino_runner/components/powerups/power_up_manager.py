import random
import pygame
from components.powerups.shield import Hammer, Shield
from utils.constants import DEFAULT_TYPE, HAMMER_TYPE, SHIELD_TYPE

class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.when_appers = 0
        self.test=0 

    def update(self, game,poitns):
        self.generate_power_ups(poitns)
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            self.test+=2
            if game.dinosaur.dino_rect.colliderect(power_up.rect) and self.test<= 30:
                power_up.start_time = pygame.time.get_ticks()
                if power_up.type==HAMMER_TYPE:
                    game.dinosaur.type =HAMMER_TYPE
                    game.dinosaur.isHammerType = True
                    game.dinosaur.isShieldType = False
                if power_up.type==SHIELD_TYPE:
                    game.dinosaur.type =SHIELD_TYPE
                    game.dinosaur.isShieldType = True
                    game.dinosaur.isHammerType = False
                power_up.start_time = pygame.time.get_ticks()
                time_random = random.randrange(2,4)
                game.dinosaur.shield_time_up = (time_random )
                self.power_ups.remove(power_up)
            else:
                self.test=0
                game.dinosaur.type=DEFAULT_TYPE
                

    def generate_power_ups(self,points):
        x =random.randint(0,1)
        if x==0:
            if (points%150)==0:
                if len(self.power_ups) == 0:
                    x=random.randint(0,1)
                    if x==0:
                        self.power_ups.append(Shield())
                    else:
                        self.power_ups.append(Hammer())

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []