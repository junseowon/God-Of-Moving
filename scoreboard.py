import sys
import pygame
from settings import *

class Scoreboard:
    def __init__(self, game):
        pygame.init()
        self.game = game
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        
        self.last_score = 0

        self.font = pygame.font.Font(NEODGM_FONT_PATH, 40)
        self.score_font = pygame.font.Font(NEODGM_FONT_PATH, 100)
        self.start_text = self.font.render('스페이스를 눌러 재시작', True, GREEN)
        self.start_text_width = self.start_text.get_rect().size[0]
        self.start_text_height = self.start_text.get_rect().size[1]
        self.score_text = self.font.render('점수', True, GREEN)

    def draw(self):
        self.screen.fill('black')

        self.score_num_text = self.score_font.render(f"{self.last_score}", True, GREEN)


        self.screen.blit(self.score_num_text, (HALF_WIDTH - self.score_num_text.get_rect().centerx, 200))

        self.screen.blit(self.start_text, (HALF_WIDTH - self.start_text_width // 2, HALF_HEIGHT + self.start_text_height + 100))
        self.screen.blit(self.score_text, (HALF_WIDTH - self.score_text.get_rect().centerx, 150))

    def update(self):
        if not self.last_score == self.game.score:
            self.last_score += 1

        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.game.__init__()
                self.game.run()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()