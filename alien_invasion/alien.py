import pygame 
from pygame.sprite import Sprite


class Alien(Sprite):
    """ a class represent alien. """

    def __init__(self, ai_settings, screen):
        """ initialize the alien and set the first position."""
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the alien image, and set its rect property
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # the alien at left-top firstly
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the position of alien
        self.x = float(self.rect.x)

    def blitme(self):
        """ show the alien at point position. """
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """ if alien in screen orign, return Turn. """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True 

    def update(self):
        """ alien go right. """
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
