from pygame.sprite import Sprite
from utils.constants import SCREEN_WIDTH

class Obstacle(Sprite):

    def __init__(self, image, index):
        
        self.image = image
        self.index = index
        self.rect = self.image[self.index].get_rect()
        self.rect.x = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image[self.index], self.rect)

    def update(self, obstacle_speed, obstacles,game_running,game):
        self.rect.x -= obstacle_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        if not game_running:
            obstacles.pop()
        
            
            