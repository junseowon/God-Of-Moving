import pygame
import random
import math

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("탄막 피하기 게임")

# 색상
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Clock 객체
clock = pygame.time.Clock()

# 폰트 설정
font = pygame.font.Font(None, 36)

# 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BLUE, (15, 15), 15)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed

# 탄막 클래스
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (5, 5), 5)
        self.rect = self.image.get_rect(center=(x, y))

        # 플레이어를 향한 방향 설정
        angle = math.atan2(target_y - y, target_x - x)
        self.speed_x = math.cos(angle) * 5
        self.speed_y = math.sin(angle) * 5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 화면 밖으로 나가면 제거
        if (self.rect.right < 0 or self.rect.left > WIDTH or 
            self.rect.bottom < 0 or self.rect.top > HEIGHT):
            self.kill()

# 스프라이트 그룹
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# 점수 초기화
score = 0

# 게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력
    keys = pygame.key.get_pressed()
    player.update(keys)

    # 탄막 생성 (랜덤 위치에서 플레이어를 향해 발사)
    if random.random() < 0.02:  # 탄막 생성 확률
        x, y = random.choice([(random.randint(0, WIDTH), 0),  # 위쪽
                              (random.randint(0, WIDTH), HEIGHT),  # 아래쪽
                              (0, random.randint(0, HEIGHT)),  # 왼쪽
                              (WIDTH, random.randint(0, HEIGHT))])  # 오른쪽
        bullet = Bullet(x, y, player.rect.centerx, player.rect.centery)
        bullets.add(bullet)
        all_sprites.add(bullet)

    # 충돌 감지
    if pygame.sprite.spritecollide(player, bullets, False):
        print(f"Game Over! Final Score: {score}")
        running = False

    # 점수 증가
    score += 1

    # 스프라이트 업데이트
    all_sprites.update()

    # 화면 그리기
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
