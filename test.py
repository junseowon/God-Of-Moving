import pygame
import sys

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("계속 올라가는 점수판")

# 폰트 설정
font = pygame.font.Font(None, 74)

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 점수 변수
score = 0

# 프레임 설정
clock = pygame.time.Clock()
FPS = 60

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 점수 증가
    score += 1

    # 화면 초기화
    screen.fill(BLACK)

    # 점수 렌더링
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2))

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 조절
    clock.tick(FPS)

# 종료
pygame.quit()
sys.exit()
