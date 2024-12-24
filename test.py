import pygame
import sys

# Pygame 초기화
pygame.init()

# 화면 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("마우스 감지")

# 색상 정의
white = (255, 255, 255)
red = (255, 0, 0)

# 실행 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 마우스 위치 확인
    x, y = pygame.mouse.get_pos()
    if 0 <= x < screen_width or 0 <= y < screen_height:
        screen.fill(white)  # 화면 안에 있으면 흰색
    else:
        screen.fill(red)  # 화면 밖으로 나가면 빨간색

    pygame.display.flip()

# 종료
pygame.quit()
sys.exit()
