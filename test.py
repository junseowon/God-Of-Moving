import pygame
from pygame.locals import *

# Pygame 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cooldown Restart Example")

# 색상
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 쿨타임 관련 변수
cooldown_time = 2000  # 쿨타임 (밀리초 단위)
last_used_time = pygame.time.get_ticks()  # 처음 시작 시간

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                # 스페이스바를 누르면 쿨타임 즉시 재시작
                last_used_time = pygame.time.get_ticks()
                print("쿨타임 재시작!")

    # 현재 시간
    current_time = pygame.time.get_ticks()

    # 쿨타임이 끝났다면 스킬 사용
    if current_time - last_used_time >= cooldown_time:
        print("스킬 사용 가능!")

    # 화면 업데이트
    screen.fill(WHITE)

    # 쿨타임 바 표시
    cooldown_left = max(0, cooldown_time - (current_time - last_used_time))
    print(cooldown_left)
    cooldown_percentage = cooldown_left / cooldown_time
    bar_width = 200
    pygame.draw.rect(screen, RED, (300, 500, int(bar_width * cooldown_percentage), 20))

    pygame.display.flip()

pygame.quit()
