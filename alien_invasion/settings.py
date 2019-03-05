class Settings():
    """ store all of the settings of 'alien_invasion' """

    def __init__(self):
        """ initial the settings of the static game. """
        # set screen
        self.screen_with = 900
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # set the ship
        # self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # set the bullet
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3

        # set alien properties
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        
        # acculate the game
        self.speedup_scale = 1.1
        # increase the aliens points
        self.score_scale = 1.5

        # fleet_direction equal 1 go right, equal -1 go left
        #self.fleet_direction = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ initialize changing settings according game go on """
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.bullet_speed_factor = 3


        # fleet_direction equal 1 go right, equal -1 go left
        self.fleet_direction = 1

        # record score
        self.alien_points = 50


    def increase_speed(self):
        """ speed up settings and increase aliens' points. """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)





