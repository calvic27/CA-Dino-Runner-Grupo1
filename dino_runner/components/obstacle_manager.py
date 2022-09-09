from components.obstacles import Cactus,Bird
import random
import pygame
from utils.constants import BIRD, DEFAULT_TYPE,LARGE_CACTUS, SMALL_CACTUS,GAME_OVER


class ObstacleManager():
    def __init__(self):
        self.obstacles = []
        self.step_index=0

    def update(self,game,game_running,screen):
        if len(self.obstacles) == 0:
            x=random.randint(0,2)
            if x==0:
                self.obstacles.append(Bird(BIRD))
            if x==1:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            if x==2:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            self.step_index+=1
            if self.step_index >= 10:
                self.step_index=0
        for obstacle in self.obstacles:
            if not game.dinosaur.isShieldType and not game.dinosaur.isHammerType:
                if game.dinosaur.dino_rect.colliderect(obstacle.rect):
                    pygame.time.delay(1000)
                    game.playing =False 
                    game_running=False
                   
            if game.dinosaur.dino_rect.colliderect(obstacle.rect) and game.dinosaur.isHammerType:
                    self.obstacles=[]
                    game.dinosaur.isHammerType=False
                    game.dinosaur.type=DEFAULT_TYPE
                    break
            while game.dinosaur.dino_rect.colliderect(obstacle.rect) and game.dinosaur.isShieldType:
                self.obstacles[self.step_index//10].update( game.game_speed, self.obstacles,game_running,game)
                if not game.dinosaur.dino_rect.colliderect(obstacle.rect) and game.dinosaur.isShieldType:
                    game.dinosaur.isShieldType=False
                    game.dinosaur.type=DEFAULT_TYPE
            self.obstacles[self.step_index//10].update( game.game_speed, self.obstacles,game_running,game)



    def draw(self, screen):
        for obstacle in self.obstacles:
            self.obstacles[self.step_index//10].draw(screen)

