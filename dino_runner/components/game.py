from cgitb import text
from distutils import text_file
import pygame
from components.obstacle_manager import ObstacleManager
from utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from utils import text_utils 
from components.dinisaur import Dinosaur


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.dinosaur = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.poitns=0
        self.post_points=0
        self.game_running= True
        self.obstacles_value=True

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def execute(self):
        while self.game_running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.game_running=False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.dinosaur.update(user_input,self.obstacles_value)
        self.obstacle_manager.update(self,self.obstacles_value,self.screen)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.show_score()
        self.dinosaur.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        if self.poitns<=300:
            self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            if self.x_pos_bg <= -image_width:
                self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
                self.x_pos_bg = 0
            self.x_pos_bg -= self.game_speed
        else:
            self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            pygame.display.flip()
            if self.x_pos_bg <= -image_width:
                self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
                self.x_pos_bg = 0
            self.x_pos_bg -= self.game_speed

    def show_score (self):
        x=0
        self.poitns +=1
        if self.poitns %100==0:
            self.game_speed +=1
        text, text_rect = text_utils.get_score_element(self.poitns,x)
        self.screen.blit(text,text_rect)
        text2,text_rect2 =text_utils.get_score_element(self.post_points,x+1)
        self.screen.blit(text2,text_rect2)

    def show_menu(self):
        self.game_running=True
        white_color=(255,255,255)
        self.screen.fill(white_color)
        self.show_options_menu()
        pygame.display.update()
        self.handle_key_event_menu()

    def show_options_menu(self):
        half_screen_height =SCREEN_HEIGHT//2
        half_screen_width =SCREEN_WIDTH//2
        if self.post_points==0:
            text,text_rect=text_utils.get_text_element("press any key to start",half_screen_width,half_screen_height)
        else:
            text,text_rect=text_utils.get_text_element("press any key to restart",half_screen_width,half_screen_height)

        self.screen.blit(text, text_rect)

    def handle_key_event_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.game_running=False
                pygame.display.quit()
                pygame.quit()
            if event.type ==pygame.KEYDOWN:
                self.run()
                self.obstacles_value=True
                self.post_points=self.poitns
                self.poitns=0


    