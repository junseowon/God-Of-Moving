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
        pygame.mouse.get_rel()
        self.mouse_pos = pygame.mouse.get_pos()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.last_ticks = pygame.time.get_ticks() // 50

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
        self.item = Item()
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


        
    def create_bullets(self):
        # 화면 밖에서 랜덤으로 총알이 발사될 위치 지정
        positions = [
            (random.randint(0, self.now_width), 0),  # 위쪽
            (random.randint(0, self.now_width), self.now_height),  # 아래쪽
            (0, random.randint(0, self.now_height)),  # 왼쪽
            (self.now_width, random.randint(0, self.now_height))  # 오른쪽
        ]
    
        # 각 총알은 화면 밖에서 생성되어 플레이어 방향으로 향하게 됩니다.
        for pos in positions:
            x, y = pos
            bullet = Bullet(self, x, y, self.mouse_pos[0], self.mouse_pos[1])  # 플레이어 위치를 목표로
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)

    def update(self):
        self.player.update()
        self.mouse_pos = pygame.mouse.get_pos()

        self.score += 1

        if random.randint(1, 20) == 1:
            self.create_bullets()

        self.all_sprites.update()

        for bullet in self.bullets:
            if self.player.collide_point(bullet.rect.center):
                bullet.kill()  # 충돌한 총알 제거
                self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                pygame.mouse.set_visible(True)
                print('죽음')
                self.running = False               
        
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        print(self.now_width)
        """
        if self.now_width > 300:            
            self.current_tick = pygame.time.get_ticks() // 50
            self.max_screen_width = WIDTH - (self.current_tick - self.last_ticks)
            self.screen_width_percentage = self.max_screen_width / WIDTH

            self.max_screen_height = HEIGHT - (self.current_tick - self.last_ticks)
            self.screen_height_percentage = self.max_screen_height / HEIGHT

            self.now_width = (int)(WIDTH * self.screen_width_percentage)
            self.now_height = (int)(HEIGHT * self.screen_height_percentage)

            self.screen = pygame.display.set_mode((self.now_width, self.now_height))
        else:
            print('최소')
            self.screen = pygame.display.set_mode((300, 300))
        """

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
                    if self.item.on_click():  # 클릭된 아이템이 클릭되었는지 확인
                        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
                        self.last_ticks = pygame.time.get_ticks() // 50
                        
                        # 점수 이펙트 생성 (아이템의 위치 위로 "+1" 텍스트가 올라가도록)
                        self.score_effect = ScoreEffect(self.item.rect.centerx, self.item.rect.top)
                        self.score_effects.add(self.score_effect)
                        self.all_sprites.add(self.score_effect)
                        self.item.kill()  # 아이템 제거
 
                        # 새로운 아이템 생성
                        self.item = Item()
                        self.items.add(self.item)
                        self.all_sprites.add(self.item)
                    

    def run(self):
        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos(PLAYER_POS)
        while self.running:
            self.check_events()
            self.draw()
            self.update()
            
