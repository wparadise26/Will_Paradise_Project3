import arcade

my_window = arcade.open_window(700, 700, "Will's Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
title = arcade.Text("Red Car", 300, 600, arcade.color.RED, 20)
author = arcade.Text("By Will Paradise", 280, 550, arcade.color.BLACK, 15)
title.draw()
author.draw()
arcade.draw_rectangle_filled(350, 350, 200, 50, arcade.color.RED)
arcade.draw_rectangle_filled(350, 270, 700, 20, arcade.color.ASH_GREY)
arcade.draw_rectangle_filled(350, 0, 700, 520, arcade.color.DARK_BROWN)
arcade.draw_circle_filled(280, 300, 25, arcade.color.BLACK)
arcade.draw_circle_filled(420, 300, 25, arcade.color.BLACK)
arcade.draw_rectangle_filled(420, 400, 10, 50, arcade.color.BLUE)
arcade.draw_rectangle_filled(330, 420, 170, 10, arcade.color.RED)
arcade.draw_rectangle_filled(260, 400, 10, 50, arcade.color.RED)

arcade.finish_render()

arcade.run()
