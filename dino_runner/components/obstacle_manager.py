from dino_runner.components.cactus import Cactus
from utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
            self.obstacles.append(Cactus(LARGE_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(15, self.obstacles)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)