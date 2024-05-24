############################################
# 💻 Experiment with the settings, see what you discover!
############################################


import arcade
from helpers import fixCrash
from enemy import Enemy
from player import Player

class MyGame(arcade.Window):
    """Main application class."""

    def __init__(self):
        """
        Initializer
        """

        self.screen_width = 800
        self.screen_height = 600

        super().__init__(
            width = self.screen_width, 
            height = self.screen_height, 
            title = "Game 1")


        # Physics
        self.MOVEMENT_SPEED = 5

        # game over
        self.game_over = False
        
        """Set up the game and initialize the variables."""

        # Set up the player
        self.player_list = arcade.SpriteList()

        self.player_sprite = Player(
            path = "assets/sprites/slime.png",
            scale = 2,
            center_x = 250,
            center_y = 270,
        )

        # loads another version of the sprite image, flipped 
        texture = arcade.load_texture("assets/sprites/slime.png",
                                      flipped_horizontally=True)
        
        self.player_sprite.textures.append(texture)

    
        self.player_list.append(self.player_sprite)

        # sets up map
        map_name = "assets/map/map_topdown.tmj" 

        layer_options = {
            "Walls": {"use_spatial_hash": True}
        }

        # map scaling
        self.TILE_SCALING = 2
        self.SPRITE_PIXEL_SIZE = 128
        self.GRID_PIXEL_SIZE = self.SPRITE_PIXEL_SIZE * self.TILE_SCALING

        # read in the tiled map
        self.tile_map = arcade.load_tilemap(
            map_name, 
            layer_options=layer_options,
              scaling=self.TILE_SCALING
        )

        self.end_of_map = self.tile_map.width * self.GRID_PIXEL_SIZE

        # sets wall and coin SpriteLists
        self.wall_list = self.tile_map.sprite_lists["Walls"]
        self.background_list = self.tile_map.sprite_lists["Background"]
  
        # sets the background color
        arcade.set_background_color(arcade.color.BLIZZARD_BLUE)

        # Keep player from running through the wall_list layer
        walls = [self.wall_list]

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, walls, gravity_constant=0
        )

        # sets up camera 
        self.camera = arcade.Camera(self.screen_width, self.screen_height)

        # center camera on user
        self.pan_camera_to_user()

        # SETS UP ENEMIES
        self.enemy_list = arcade.SpriteList()

        # enemy with boundries
        enemy1 = Enemy(
            path = "assets/sprites/slime.png", 
            scale = 2,
            center_x = 350,
            center_y = 335, 
            change_x = 1, 
            boundary_right= 600,
            boundary_left= 200
            )    

        self.enemy_list.append(enemy1)



    def on_draw(self):
        """
        Render the screen.
        """

        # draw parts of the game

        self.camera.use()
        self.clear()
        
        # draws the map layers
        self.background_list.draw()
        self.wall_list.draw()

        # draws the player
        self.player_list.draw()
        self.enemy_list.draw()
  

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """

        if key == arcade.key.W:
            self.player_sprite.change_y = self.MOVEMENT_SPEED

        if key == arcade.key.A:
            self.player_sprite.change_x = -self.MOVEMENT_SPEED

        elif key == arcade.key.D:
            self.player_sprite.change_x = self.MOVEMENT_SPEED

        elif key == arcade.key.S:
            self.player_sprite.change_y = -self.MOVEMENT_SPEED

        elif key == arcade.key.ESCAPE:
            arcade.exit()

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        
        if key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Call update on all sprites and physics
        self.physics_engine.update()
        self.player_list.update()
        self.enemy_list.update()

        if self.player_sprite.center_x < 0:
            self.player_sprite.center_x = 0

        # if the player collides with an enemy
        enemies_hit = arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)
        for enemy in enemies_hit:
            enemy.on_collison(self.player_sprite)

        # Pan to the user
        self.pan_camera_to_user(panning_fraction=0.12)

    def pan_camera_to_user(self, panning_fraction: float = 1.0):
        """ Manage Scrolling """

        # This spot would center on the user
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width/2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height/3)

        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0

        user_centered = screen_center_x, screen_center_y

        self.camera.move_to(user_centered, panning_fraction)


fixCrash()
window = MyGame()
arcade.run()