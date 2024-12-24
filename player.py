from settings import *
import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, game):  
        super().__init__()
        self.game = game
        self.radius = 10
        self.color = 'green'
        self.rect = pygame.Rect(0, 0, self.radius * 2, self.radius * 2)
        self.rect.center = self.game.mouse_pos
        self.x, self.y = PLAYER_POS

    def movement(self):
        self.rect.center = self.game.mouse_pos

    def draw(self):
        pygame.draw.circle(self.game.screen, self.color, self.rect.center, self.radius)  # 동그라미 그리기

    # 점이 플레이어 원 안에 있는지 확인
    def collide_point(self, point):
        distance = math.sqrt((point[0] - self.rect.centerx) ** 2 + (point[1] - self.rect.centery) ** 2)
        return distance <= self.radius

    def over_map(self):
        self.x, self.y = (self.game.now_width // 2, self.game.now_height // 2)
        
        if self.game.mouse_pos[0] > self.game.now_width - 20:
            self.game.mouse_pos = pygame.mouse.set_pos(self.x, self.y)
        elif self.game.mouse_pos[0] < 20:
            self.game.mouse_pos = pygame.mouse.set_pos(self.x, self.y)
        elif self.game.mouse_pos[1] < 20:
            self.game.mouse_pos = pygame.mouse.set_pos(self.x, self.y)
        elif self.game.mouse_pos[1] > self.game.now_height - 20:
            self.game.mouse_pos = pygame.mouse.set_pos(self.x, self.y)

    def update(self):
        self.movement()
        self.over_map()
