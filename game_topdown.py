import arcade
from player import PlayerCharacter
from helpers import scale
from enemy import Enemy
# 💻 Try changing these numbers to adjust the scale of the game
TILE_SCALING = 2
PLAYER_SCALING = 2
ENEMY_SCALING = 2
ENEMY_SIZE = 2

# Grid Size
SPRITE_PIXEL_SIZE = 28
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# SPRITE_SCALING = 0.5

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600


SCREEN_TITLE = "Better Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5
UPDATES_PER_FRAME = 5
# animation sprite
RIGHT_FACING = 0
LEFT_FACING = 1

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        self.game_over = False
        # Track the current state of what key is pressed

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # sets up map
        map_name = "assets/map/map_topdown.tmj"

        layer_options = {
            "Walls": {"use_spatial_hash": True}
        }

        # read in the tiled map
        self.tile_map = arcade.load_tilemap(
            map_name, layer_options=layer_options, scaling=TILE_SCALING
        )

        self.end_of_map = self.tile_map.width * GRID_PIXEL_SIZE

        # sets wall and SpriteLists
        self.wall_list = self.tile_map.sprite_lists["Walls"]
        self.background_list = self.tile_map.sprite_lists["Background"]

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)


        # Sprite lists
        # self.player_list = arcade.SpriteList()

        # Set up the player
        # self.player_sprite = Player("assets/sprites/slime.png",
        #                             PLAYER_SCALING)
        self.player = PlayerCharacter()

        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 200
        self.player_list.append(self.player_sprite)


        # sets up enemies
        self.enemy_list = arcade.SpriteList()

        # enemy with boundries
        enemy1 = Enemy("assets/sprites/enemy_cow_sprite.png", ENEMY_SCALING)
        enemy1.bottom = 500
        enemy1.left = 600

        # Set boundaries on the left/right the enemy can't cross
        enemy1.boundary_right = 900
        enemy1.boundary_left = 600

        # enemies speed
        enemy1.change_x = 1

        # enemy with no boundries
        enemy2 = Enemy("assets/sprites/enemy_cow_sprite.png", ENEMY_SCALING)
        enemy2.bottom = 800
        enemy2.left = 300

        # enemies speed
        enemy2.change_x = 2
     
        # add enemies to list
        self.enemy_list.append(enemy1)
        self.enemy_list.append(enemy2)

        # Keep player from running through the wall_list layer
        walls = [self.wall_list, ]
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, walls, gravity_constant=0
        )

        # sets up camera 
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # center camera on user
        self.pan_camera_to_user()

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen
        self.camera.use()
        self.clear()

        # draw all the map
        self.background_list.draw()
        self.wall_list.draw()

        # Draw all the sprites.
        self.player_list.draw()
        self.enemy_list.draw()

        if self.game_over == True:
            x_pos = self.player_sprite.center_x+100
            y_pos = self.player_sprite.center_y+100
            text_size = 25

            arcade.draw_text(f"Game Over :(", x_pos, y_pos, arcade.color.WHITE, text_size)
    

    def on_update(self, delta_time):
        """ Movement and game logic """

        if not self.game_over:
            self.physics_engine.update()
            # self.player_sprite.update()
            self.player_list.update_animation(RIGHT_FACING, LEFT_FACING)

            self.enemy_list.update()

        # Pan to the user
        self.pan_camera_to_user(panning_fraction=0.12)
        
        # if the player collides with an enemy
        enemies_hit = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)
        for enemy in enemies_hit:
            enemy.on_collison(self.player_sprite)


        for enemy in self.enemy_list:
            # If the enemy hit a wall, reverse
            if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0:
                enemy.change_x *= -1
            # If the enemy hit the left boundary, reverse
            elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                enemy.change_x *= -1
            # If the enemy hit the right boundary, reverse
            elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                enemy.change_x *= -1


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.up_pressed = True
            self.update_player_speed()

        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.update_player_speed()

        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.update_player_speed()

        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.update_player_speed()
        elif key == arcade.key.ESCAPE:
            arcade.exit()


    def on_key_release(self, key, modifiers):

        """Called when the user releases a key. """

        if key == arcade.key.UP:
            self.up_pressed = False
            self.update_player_speed()

        elif key == arcade.key.DOWN:
            self.down_pressed = False
            self.update_player_speed()

        elif key == arcade.key.LEFT:
            self.left_pressed = False
            self.update_player_speed()

        elif key == arcade.key.RIGHT:
            self.right_pressed = False
            self.update_player_speed()

    def pan_camera_to_user(self, panning_fraction: float = 1.0):
        """ Manage Scrolling """

        # This spot would center on the user
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )

        user_centered = screen_center_x, screen_center_y

        self.camera.move_to(user_centered, panning_fraction)

    def update_player_speed(self):
        # Calculate speed based on the keys pressed

        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = MOVEMENT_SPEED

        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -MOVEMENT_SPEED

        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -MOVEMENT_SPEED

        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = MOVEMENT_SPEED



if __name__ == "__main__":
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


