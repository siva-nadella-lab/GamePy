import sys
import pygame
from settings import Settings as GameSettings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
            self.gameSettings.screen = (self.screen.get_rect().width, self.screen.get_rect().height)
        else:
            self.screen = pygame.display.set_mode(self.gameSettings.screen)
        pygame.display.set_caption(self.gameSettings.caption)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._createAlienFleet()

    def _createAlienFleet(self):
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width = alien.rect.width
        alien_height = alien.rect.height

        current_x, current_y = alien_width, alien_height
        while current_y < (self.gameSettings.screen[1] - 3 * alien_height):

            while (current_x < self.gameSettings.screen[0] - 2 * alien_width):
                self._createAlien(current_x, current_y)
                current_x += 2*alien_width
            
            current_x = alien_width
            current_y += 2 * alien_height

    def _createAlien(self, xPosition, yPosition):
        newAlien = Alien(self)
        newAlien.x = xPosition
        newAlien.rect.x = xPosition
        newAlien.rect.y = yPosition
        self.aliens.add(newAlien)

    def run_game(self):
        ## Main loop of the game ##

        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            self._clear_used_bullets()

            self._update_screen()
            self.clock.tick(60)

    def _clear_used_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)
        print ("Bullet Count: " + len(self.bullets).__str__())

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
        print(event.key)
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
                sys.exit()

    def _fire_bullet(self):
        if (len(self.bullets) <= self.gameSettings.max_bullets):
            newBullet = Bullet(self)
            self.bullets.add(newBullet)

    def _update_screen(self):
        self.screen.fill(self.gameSettings.bgcolor)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    ## Make game instance and run ##
    ai = AlienInvasion()
    ai.run_game()
