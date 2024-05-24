import arcade

class Player(arcade.Sprite):

    def __init__(self, path, scale, center_x, center_y):
        super().__init__()

        self.scale = scale
        self.center_x = center_x
        self.center_y = center_y
        self.textures = []

        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture(path)
        self.textures.append(texture)
        
        texture = arcade.load_texture(path,
                                      flipped_horizontally=True)     

        self.textures.append(texture)

        # By default, face right.
        self.texture = self.textures[0]

    def update(self):
        super().update()
      
        # Change the sprite direction
        if self.change_x > 0:
            self.texture = self.textures[0]
        elif self.change_x < 0:
            self.texture = self.textures[1]
