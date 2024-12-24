from settings import *
import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        # 플레이어 위치를 목표로 각도 계산 (각도를 라디안으로 변환)
        dx = target_x - x
        dy = target_y - y
        angle = math.degrees(math.atan2(dy, dx))  # 목표 방향으로 각도 계산
        
        # 속도 설정
        speed = 5
        self.dx = math.cos(math.radians(angle)) * speed
        self.dy = math.sin(math.radians(angle)) * speed

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # 화면 밖으로 나가면 삭제
        if (self.rect.top < 0 or self.rect.bottom > HEIGHT or
            self.rect.left < 0 or self.rect.right > WIDTH):
            self.kill()