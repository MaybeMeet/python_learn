import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        """ initialize the ship and set its first position. """
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship images and get 
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set ship at the bottom centered of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store the minimum value of center
        self.center = float(self.rect.centerx)

        # mark of moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ according the moving mark to adjust the ship position"""
        # update the center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        
        # according self.center to update rect object
        self.rect.centerx = self.center

    def blitme(self):
        """ set the position of ship"""
        self.screen.blit(self.image,self.rect)


    def center_ship(self):
        """ let ship on screen center. """
        self.center = self.screen_rect.centerx

