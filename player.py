import arcade

class Player(arcade.Sprite):

    def __init__(self, img_path, PLAYER_SCALING):
        super().__init__()

        self.scale = PLAYER_SCALING
        self.textures = []
        self.character_face_direction = 0

        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture(img_path)
        self.textures.append(texture)
        
        texture = arcade.load_texture(img_path,
                                      flipped_horizontally=True)     

        self.textures.append(texture)

        # By default, face right.
        self.texture = self.textures[self.character_face_direction]

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.textures[self.character_face_direction]
        elif self.change_x > 0:
            self.texture = self.textures[self.character_face_direction]
