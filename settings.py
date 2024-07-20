class Settings:

    def __init__(self):
        ## Initializing the settings of the game... ##

        ## screen settings ##
        self.bgcolor = (230,230,230)
        self.screen = (1200,800)
        self.full_screen = True
        self.caption = "Alien Invasion"
        self.frame_rate = 60
        self.ship_speed = 4

        ## Bullet Settings ##
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.max_bullets = 20