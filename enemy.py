import arcade
from math import sqrt 


def scale(vector, magnitude):
    # this is helper function 

    vx, vy = vector
    old_magnitude = sqrt(vx * vx + vy * vy) if vx * vx + vy * vy else 0
    factor = magnitude / old_magnitude
    return vx * factor, vy * factor

class Enemy(arcade.Sprite):
    # customize a Sprite for enemy featues 

    def __init__(self, path, scale, center_x, center_y, change_x=None, boundary_left=None, boundary_right=None):
        super().__init__()

        self.scale = scale
        self.center_x = center_x
        self.center_y = center_y
        self.change_x = change_x
        self.boundary_left = boundary_left
        self.boundary_right = boundary_right

        self.textures = []

        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture(path)
        self.textures.append(texture)
        
        flipped_texture = arcade.load_texture(path,
                                      flipped_horizontally=True)     

        self.textures.append(flipped_texture)

        # By default, face right.
        self.texture = self.textures[1]

    def update(self):
        # updates the sprite 

        self.position = [
            self._position[0] + self.change_x,
            self._position[1] + self.change_y,
        ]

        self.angle += self.change_angle

        # flip the sprite image
        if self.change_x == 1:
            self.texture = self.textures[0]
        else:
            self.texture = self.textures[1]

        # move the sprite within the boundries
        if self.boundary_left is not None and self.left < self.boundary_left:
            self.change_x *= -1

        elif self.boundary_right is not None and self.right > self.boundary_right:
            self.change_x *= -1


    def on_collison(self, other_sprite):
        # bumps the other_sprite away from itself 

        away = (self.center_x - other_sprite.center_x, self.center_y - other_sprite.center_y)
        away_x, away_y = scale(away, 10)
        other_sprite.center_x = other_sprite.center_x - away_x
        other_sprite.center_y = other_sprite.center_y - away_y
