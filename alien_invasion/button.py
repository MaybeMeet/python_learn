import pygame.font

class Button():
    
    def __init__(self, ai_settings, screen, msg):
        """intialize for Button"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the shape of the button and other properties
        self.width, self.height = 200, 50
        self.button_color = (0, 55, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # creat the button's rect object, and make it center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # create the mark
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ make msg to trans image. And make it center on button. """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # draw a button with color, and draw text
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
