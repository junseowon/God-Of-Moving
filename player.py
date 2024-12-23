from settings import *
import pygame
import math

class Player:
    def __init__(self, game):  
        self.game = game
        self.x, self.y = PLAYER_POS

    def draw(self):
        pygame.draw.circle(self.game.screen, 'green', self.game.mouse_pos, 15)

    def over_map(self):
        if self.game.mouse_pos[0] > WIDTH - 20:
            self.game.mouse_pos = pygame.mouse.set_pos(PLAYER_POS)
        elif self.game.mouse_pos[0] < 20:
            self.game.mouse_pos = pygame.mouse.set_pos(PLAYER_POS)
        elif self.game.mouse_pos[1] < 20:
            self.game.mouse_pos = pygame.mouse.set_pos(PLAYER_POS)
        elif self.game.mouse_pos[1] > HEIGHT - 20:
            self.game.mouse_pos = pygame.mouse.set_pos(PLAYER_POS)


    def update(self):
        self.over_map()
