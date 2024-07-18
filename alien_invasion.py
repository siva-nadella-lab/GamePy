import sys
import pygame
from settings import Settings as GameSettings
from ship import Ship

class AlienInvasion:
    ## Alien Invasion Class ##

    def __init__(self) -> None:
        ## Initializing the class and its variables ##
        pygame.init()
        self.gameSettings = GameSettings()

        ## control the frame rate of the display during the game to a second - further controlled in the run_game function##
        self.clock = pygame.time.Clock()
        if self.gameSettings.full_screen:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            self.screen.screen_width = self.screen.get_rect().width
            self.screen.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(self.gameSettings.screen)
        pygame.display.set_caption(self.gameSettings.caption)

        self.ship = Ship(self)


    def run_game(self):
        ## Main loop of the game ##

        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        ## Respond to key presses and mouse events ##
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up =False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down =False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.gameSettings.bgcolor)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    ## Make game instance and run ##
    ai = AlienInvasion()
    ai.run_game()
