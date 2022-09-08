import random
from components.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, image):
        self.index = random.randint(0,2)
        super().__init__(image, self.index)
        self.rect.y = 320
class Bird(Obstacle):
    def __init__(self, image):
        self.index = random.randint(0,1)
        self.height=random.randint(0,1)
        super().__init__(image, self.index)
        if self.height==0:
            self.rect.y = 270
        else:
            self.rect.y=210

