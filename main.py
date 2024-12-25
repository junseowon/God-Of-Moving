import sys
import pygame
from settings import *
from game import *
from scoreboard import *

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("무빙의 신")
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()

        self.title_image = pygame.image.load('./UI/title.png')
        self.title = self.title_image.get_rect()
        self.title.centerx = self.title.size[0] // 2
        self.title.centery = self.title.size[1] // 2

        self.font = pygame.font.Font(NEODGM_FONT_PATH, 40)
        self.start_text = self.font.render('스페이스를 눌러 시작', True, GREEN)
        self.start_text_width = self.start_text.get_rect().size[0]
        self.start_text_height = self.start_text.get_rect().size[1]

        self.new_game()

    def draw(self):
        self.screen.fill('black')

        self.screen.blit(self.title_image, (HALF_WIDTH - self.title.centerx, 100))
        self.screen.blit(self.start_text, (HALF_WIDTH - self.start_text_width // 2, HALF_HEIGHT + self.start_text_height + 100))

    def update(self):
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)

    def new_game(self):
        self.game = Game()
        self.scoreboard = Scoreboard(self.game)
        self.mouse_pos = pygame.mouse.set_pos(PLAYER_POS)

    def check_events(self):
        
        if self.scoreboard.retry:           
            self.game = Game()     
            self.game.run()
            self.scoreboard.__init__(self.game)

        if not self.game.running:
            print(self.game.running, "죽음")           
            self.scoreboard.run()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                #self.new_game()
                self.game.run()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()            

if __name__ == '__main__':
    main = Main()
    main.run()