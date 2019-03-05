class GameStats():
    """ tracking the data of game. """

    def __init__(self, ai_settings):
        """ initialize the data. """
        self.ai_settings = ai_settings
        self.reset_stats()
        # be active when the game go on
        self.game_active = False

        # self.score = 0

        # never to reset the highest score
        self.high_score = 0

    def reset_stats(self):
        """ initalize the data that may change during running game. """
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        