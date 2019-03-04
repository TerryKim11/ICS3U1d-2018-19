import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions
def draw_cloud():
    arcade.draw_circle_filled(100, 500, 50,arcade.color.WHITE)
    arcade.draw_circle_filled(150, 500, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(190, 500, 40, arcade.color.WHITE)

def draw_rollinghills():
    arcade.draw_circle_filled(400, -200, 380, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(600, -150, 360, arcade.color.BANGLADESH_GREEN)
    arcade.draw_circle_filled(200, -90, 320, arcade.color.DARK_OLIVE_GREEN)

def draw_tree():
    arcade.draw_rectangle_filled(100, 100, 20, 50, arcade.color.DARK_BROWN)
    arcade.draw_triangle_filled(70, 100, 130, 100, 100, 130, arcade.color.CAMOUFLAGE_GREEN)
    arcade.draw_triangle_filled(75, 120, 125, 120, 100, 150, arcade.color.CAMOUFLAGE_GREEN)
    arcade.draw_triangle_filled(80, 140, 120, 140, 100, 170, arcade.color.CAMOUFLAGE_GREEN)

    arcade.draw_rectangle_filled(550, 120, 20, 50, arcade.color.DARK_BROWN)
    arcade.draw_triangle_filled(520, 120, 580, 120, 550, 150, arcade.color.CAMOUFLAGE_GREEN)
    arcade.draw_triangle_filled(525, 140, 575, 140, 550, 170, arcade.color.CAMOUFLAGE_GREEN)
    arcade.draw_triangle_filled(530, 160, 570, 160, 550, 190, arcade.color.CAMOUFLAGE_GREEN)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions

    draw_cloud()
    draw_rollinghills()
    draw_tree()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()