from components.obstacles import Cactus,Bird
import random
from utils.constants import BIRD,LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager():
    def __init__(self):
        self.obstacles = []
        self.step_index=0

    def update(self):
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

        self.obstacles[self.step_index//10].update( 30, self.obstacles)
        print(self.step_index)
    def draw(self, screen):
        for obstacle in self.obstacles:
            self.obstacles[self.step_index//10].draw(screen)