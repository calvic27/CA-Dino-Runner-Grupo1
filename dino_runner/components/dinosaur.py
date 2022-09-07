import time
from pygame.sprite import Sprite
from utils.constants import RUNNING

class Dinosaur(Sprite):
    X_POS = 50
    Y_POS = 300

    def __init__(self):
        self.steps=0 
        self.image=RUNNING[0]
        self.dino_rect =self.image.get_rect()
        self.dino_rect.x =self.X_POS
        self.dino_rect.y=self.Y_POS
   
    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x, self.dino_rect.y))
    
    def update2 (self):
        if  self.steps <= 5 :
            self.image=RUNNING[1]
            self.steps +=1

        elif self.steps <= 10:
            self.image=RUNNING[0]
            self.steps +=1
        else:
            self.steps-=10

    def key_press():
        pass

