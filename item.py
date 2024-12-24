import pygame
import random
from settings import *

class ScoreEffect(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.font.Font(NEODGM_FONT_PATH, 24).render("+화면증가", True, (255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.y_speed = -2  # 텍스트의 위로 올라가는 속도
        self.lifetime = 30  # 텍스트 지속 시간 (프레임 단위)

    def update(self):
        # 텍스트가 위로 올라가도록 설정
        self.rect.y += self.y_speed
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.kill()  # 시간이 지나면 텍스트 삭제

# 아이템 클래스
class Item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, WIDTH - self.rect.width - 40)
        self.rect.y = random.randint(20, HEIGHT - self.rect.height - 40)
        print(self.rect.x, self.rect.y)
        # 클릭 횟수 초기화
        self.click_count = 0

    def on_click(self):
        # 클릭이 발생하면 클릭 횟수 증가
        self.click_count += 1
        self.glow_time = 15  # 반짝이는 효과 시간을 15프레임으로 설정
        if self.click_count >= 1:  # 클릭 횟수가 3번 이상이면 아이템 제거
            return True  # 아이템을 제거해야 한다는 신호 반환
        return False

