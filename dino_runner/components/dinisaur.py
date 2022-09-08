from calendar import c
from re import A
import pygame
from pygame.sprite import Sprite

from utils.constants import (
    DUCKING,
    RUNNING,
    JUMPING,
    DUCKING_SHIELD,
    RUNNING_SHIELD,
    JUMPING_SHIELD,
    DEFAULT_TYPE,
    SHIELD_TYPE
)

class Dinosaur(Sprite):
    X_POS = 50
    JUMP_VEL = 8.5

    def __init__(self):
        self.actions = [{DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD},{DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}]
        self.Y_POS =[340,300]
        self.x=1
        self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
        self.type = DEFAULT_TYPE
        self.image = self.actions[1][self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS[1]
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.step_index = 0

    def update(self, user_input,obstacles_value):
        if self.dino_jump:
            self.jump(obstacles_value)
        if self.dino_duck or self.dino_run:
            self.action_dino(self.x) 
        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
            self.x=0
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False
            self.x=1

        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def action_dino(self, pos_y):
        self.image =self.actions[pos_y][self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS[pos_y]
        self.step_index += 1

    def jump(self,obstacles_value):
            self.image = self.jump_img[self.type]
            if self.dino_jump:
                self.dino_rect.y -= self.jump_vel * 4
                self.jump_vel -= 0.8
            if self.jump_vel < -self.JUMP_VEL:
                if obstacles_value:
                    self.dino_rect.y = self.Y_POS[1]
                    self.dino_jump = False
                    self.jump_vel = self.JUMP_VEL
                if not obstacles_value:
                    self.dino_rect.y = self.Y_POS[1]
