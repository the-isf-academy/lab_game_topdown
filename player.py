import arcade


class PlayerCharacter(arcade.Sprite):
    def __init__(self):

        # Set up parent class
        super().__init__()


        # Default to face-right
        self.character_face_direction = 0

        # Used for flipping between image sequences

        self.cur_texture = 0



        # self.scale = CHARACTER_SCALING


        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)

        self.points = [[-22, -64], [22, -64], [22, 28], [-22, 28]]



        # --- Load Textures ---



        # Images from Kenney.nl's Asset Pack 3

        main_path = ":resources:images/animated_characters/female_adventurer/femaleAdventurer"


        # Load textures for idle standing

        # self.idle_texture_pair = load_texture_pair(f"{main_path}_idle.png")

        #   # Load textures for walking

        self.walk_textures = []

        for i in range(8):

            texture = load_texture_pair(f"{main_path}_walk{i}.png")

            self.walk_textures.append(texture)



    def update_animation(self,  RIGHT_FACING, LEFT_FACING, UPDATES_PER_FRAME):



        # Figure out if we need to flip face left or right

        if self.change_x < 0 and self.character_face_direction == RIGHT_FACING:

            self.character_face_direction = LEFT_FACING

        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:

            self.character_face_direction = RIGHT_FACING



        # Idle animation

        if self.change_x == 0 and self.change_y == 0:

            self.texture = self.idle_texture_pair[self.character_face_direction]

            return



        # Walking animation

        self.cur_texture += 1

        if self.cur_texture > 7 * UPDATES_PER_FRAME:

            self.cur_texture = 0

        frame = self.cur_texture // UPDATES_PER_FRAME

        direction = self.character_face_direction

        self.texture = self.walk_textures[frame][direction]
