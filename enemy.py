import arcade
from helpers import scale
from random import random
from math import tau, cos, sin

class Enemy(arcade.Sprite):

    def update(self):
        """
        Update the sprite.
        """
        self.position = [
            self._position[0] + self.change_x,
            self._position[1] + self.change_y,
        ]
        self.angle += self.change_angle

    def on_collison(self, other_sprite):
        away = (self.center_x - other_sprite.center_x, self.center_y - other_sprite.center_y)
        away_x, away_y = scale(away, 10)
        other_sprite.center_x = other_sprite.center_x - away_x
        other_sprite.center_y = other_sprite.center_y - away_y

        
