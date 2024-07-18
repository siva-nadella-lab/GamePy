import pygame

class Ship:
    ## Ship's behavior, settings and actions are defined here ##

    def __init__(self, ai_game):
        ## Initialization ##

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.speed = ai_game.gameSettings.ship_speed

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.originalX = self.rect.x
        self.originalY = self.rect.y

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
            return
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
            return
        if self.moving_up and self.rect.y > 0:
            self.rect.y -= self.speed
            return
        if self.moving_down and self.rect.y < self.screen_rect.bottom-50:
            self.rect.y += self.speed
            return

    def resetPosition(self):
        self.rect.x = self.originalX
        self.rect.y = self.originalY

    def blitme(self):
        self.screen.blit(self.image, self.rect)