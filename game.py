import sys
import pygame
from settings import *
from player import *

## 컬러 세팅 ##
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.mouse.get_rel()
        self.mouse_pos = pygame.mouse.get_pos()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.new_game()

    def new_game(self):
        self.player = Player(self)

    def draw(self):
        self.screen.fill('black')
        self.player.draw() 

    def update(self):
        self.player.update()
        pygame.display.flip()
        self.mouse_pos = pygame.mouse.get_pos()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption("무빙의 신")

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
