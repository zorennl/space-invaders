from pyray import *

player = Rectangle(45,90,10,10)

enemies = []
bullets = []

init_window(100, 100, "raylib spaceinvaders")
set_target_fps(60)

def shoot(x, bullet_list: []):
    bullet_list.append(Vector2(x+5, 90))   

class Enemy:
    alive = 1

    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    
while not window_should_close():

    begin_drawing()
    clear_background(BLACK)

    if is_key_down(KeyboardKey.KEY_A) and player.x > 0:
        player.x -= 1
    if is_key_down(KeyboardKey.KEY_D) and player.x < 90:
        player.x += 1

    if is_key_pressed(KeyboardKey.KEY_SPACE):
        shoot(player.x, bullets)

    if is_key_pressed(KeyboardKey.KEY_R):
        enemies.append(Enemy(50, 15, 5, GREEN))

    for x in enemies:
        draw_circle(x.x, x.y, x.size, x.color)

    for i in bullets:
        draw_circle_v(i, 3, RED)
        i.y -= 1
        for x in enemies:
            if i.y - x.y < 8 and i.x - x.x < 8:
                x.alive = 0
    draw_rectangle_rec(player, WHITE)

    end_drawing()

close_window()   
