import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ a class that manage the ship pull bullets """

    def __init__(self,ai_settings,screen,ship):
        # creat a bullet object in ship
        super(Bullet,self).__init__()
        self.screen = screen

        # creat a rect shape bullet in (0,0), and set a correct position
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the position of the bullets
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ bullet moving up """
        # update bullets position
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """ plant the bullet on the screen """
        pygame.draw.rect(self.screen,self.color,self.rect)
        


