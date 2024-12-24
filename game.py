import sys
import pygame
import random
from settings import *
from player import *
from bullet import *
from item import *
from scoreboard import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.mouse.get_rel()
        self.mouse_pos = pygame.mouse.get_pos()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.last_ticks = pygame.time.get_ticks() // 100
        self.running = True
        
        self.now_width = WIDTH
        self.now_height = HEIGHT

        self.score = 0

        self.font = pygame.font.Font(NEODGM_FONT_PATH, 36)

        self.all_sprites = pygame.sprite.Group()

        self.bullets = pygame.sprite.Group()

        self.items = pygame.sprite.Group()

        self.score_effects = pygame.sprite.Group()

        self.new_game()
        

    def new_game(self):
        self.player = Player(self)
        self.item = Item(self)
        self.scoreboard = Scoreboard(self)
        self.items.add(self.item)
        self.all_sprites.add(self.item)

    def draw(self):
        self.screen.fill('black')
        for sprite in self.all_sprites:
            if isinstance(sprite, Player):
                pass
            else:
                self.screen.blit(sprite.image, sprite.rect)  # 총알은 기존 방식대로 그리기
        self.player.draw()
        self.score_text = self.font.render(f"{self.score}", True, WHITE)
        self.screen.blit(self.score_text, (self.now_width // 2 - self.score_text.get_rect().centerx, 10))

    def create_bullets(self):
        # 화면 밖에서 랜덤으로 총알이 발사될 위치 지정
        positions = [
            (random.randint(0, self.now_width), 0),  # 위쪽
            (random.randint(0, self.now_width), self.now_height),  # 아래쪽
            (0, random.randint(0, self.now_height)),  # 왼쪽
            (self.now_height, random.randint(0, self.now_height))  # 오른쪽
        ]
    
        # 각 총알은 화면 밖에서 생성되어 플레이어 방향으로 향하게 됩니다.
        for pos in positions:
            x, y = pos
            bullet = Bullet(x, y, self.mouse_pos[0], self.mouse_pos[1])  # 플레이어 위치를 목표로
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)

    def update(self):
        self.player.update()
        self.mouse_pos = pygame.mouse.get_pos()

        self.score += 1

        if self.now_width >= 250:
            self.current_tick = pygame.time.get_ticks() // 100

        self.max_screen_width = WIDTH - (self.current_tick - self.last_ticks)
        self.screen_width_percentage = self.max_screen_width / WIDTH

        self.max_screen_height = HEIGHT - (self.current_tick - self.last_ticks)
        self.screen_height_percentage = self.max_screen_height / HEIGHT

        self.now_width = (int)(WIDTH * self.screen_width_percentage)
        self.now_height = (int)(HEIGHT * self.screen_height_percentage)

        if random.randint(1, 30) == 1:
            self.create_bullets()

        self.all_sprites.update()

        for bullet in self.bullets:
            if self.player.collide_point(bullet.rect.center):
                bullet.kill()  # 충돌한 총알 제거
                pygame.mouse.set_visible(True)
                self.scoreboard.run()


        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        self.screen = pygame.display.set_mode((self.now_width, self.now_height))

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스 클릭 위치 얻기
                now_mouse_pos = pygame.mouse.get_pos()
                # 아이템과 마우스 클릭 위치가 겹치는지 확인
                if self.item.rect.collidepoint(now_mouse_pos):
                    if self.item.on_click():  # 클릭된 아이템이 3번 클릭되었는지 확인
                        self.last_ticks = pygame.time.get_ticks() // 100
                        
                        # 점수 이펙트 생성 (아이템의 위치 위로 "+1" 텍스트가 올라가도록)
                        self.score_effect = ScoreEffect(self.item.rect.centerx, self.item.rect.top)
                        self.score_effects.add(self.score_effect)
                        self.all_sprites.add(self.score_effect)
                        self.item.kill()  # 아이템 제거
 
                        # 새로운 아이템 생성
                        self.item = Item(self)
                        self.items.add(self.item)
                        self.all_sprites.add(self.item)

    def run(self):
        while self.running:
            self.check_events()
            self.update()
            self.draw()
