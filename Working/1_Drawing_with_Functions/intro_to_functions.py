import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions
def draw_cloud(x, y):
    arcade.draw_circle_filled(x, y, 50,arcade.color.WHITE)
    arcade.draw_circle_filled(x + 50, y, 60, arcade.color.WHITE)
    arcade.draw_circle_filled(x + 90, y, 40, arcade.color.WHITE)

def draw_rollinghills():
    arcade.draw_circle_filled(400, -200, 380, arcade.color.DARK_GREEN)
    arcade.draw_circle_filled(600, -150, 360, arcade.color.BANGLADESH_GREEN)
    arcade.draw_circle_filled(200, -90, 320, arcade.color.DARK_OLIVE_GREEN)

def draw_tree(x, y):
    arcade.draw_rectangle_filled(x, y, 20, 50, arcade.color.DARK_BROWN)
    arcade.draw_triangle_filled(x - 30, y, x + 30, y, x, y + 30, arcade.color.CAMOUFLAGE_GREEN)
    arcade.draw_triangle_filled(x - 25, y + 20, x + 25, y + 20, x, y + 50, arcade.color.CAMOUFLAGE_GREEN)
    arcade.draw_triangle_filled(x - 20, y + 40, x + 20, y + 40, x, y + 70, arcade.color.CAMOUFLAGE_GREEN)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)
    arcade.start_render()

   # call your draw functions

    draw_cloud(100, 500)
    draw_cloud(450, 520)
    draw_cloud(690, 380)
    draw_rollinghills()
    draw_tree(100, 100)
    draw_tree(170, 80)
    draw_tree(210, 140)
    draw_tree(340, 50)
    draw_tree(550, 120)
    draw_tree(600, 80)
    draw_tree(670, 150)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()