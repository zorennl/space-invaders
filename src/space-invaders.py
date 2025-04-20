from pyray import *
from random import randint, choice

# Defining player 
player = Rectangle(45,90,10,10)

# Defining lists for drawing entities
enemies = []
bullets = []

# Initiating window
init_window(100, 100, "raylib spaceinvaders")
set_target_fps(60)

# Summon function for entities
def summon_entity(x, y, size, color, entity_list: []):
    entity_list.append(Entity(x,y,size,color))   

# General entity class 
class Entity:
    alive = 1

    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    
while not window_should_close():

    begin_drawing()
    clear_background(BLACK)

    # Movement
    if is_key_down(KeyboardKey.KEY_A) and player.x > 0:
        player.x -= 1
    if is_key_down(KeyboardKey.KEY_D) and player.x < 90:
        player.x += 1

    # Combat
    if is_key_pressed(KeyboardKey.KEY_SPACE):
        summon_entity(int(player.x+5),int(player.y),3,RED,bullets)

    if is_key_pressed(KeyboardKey.KEY_R):
        summon_entity(randint(6,94),6,5,BLUE,enemies)

    # Removing dead entities and useen entities
    for i in enemies:
        if i.alive == 1:
            draw_circle(i.x, i.y, i.size, i.color)
        # else:
        #     enemies.pop(i)

    for i in bullets:
        if i.alive == 1:
            draw_circle(i.x, i.y, i.size, i.color)
        # else:
        #     bullets.pop(i)
        i.y -= 1

    for obj in enemies[:]:
        if obj.alive != 1:
            del enemies[enemies.index(obj)]

    for obj in bullets[:]:
        if obj.alive != 1 or obj.y < -2:
            del bullets[bullets.index(obj)]


    # Detecting colision between a bullet and a enemy
    for b in bullets:
        for e in enemies:
            if b.x - e.x < 3 + e.size and b.y - e.y < 3 + e.size and b.alive == 1 and e.alive == 1:
                b.alive = 0
                e.alive = 0

    # DEBUG
    entities = len(bullets) + len(enemies)
    draw_text(f'entities:{entities}',0,0,5,GREEN)

    # Drawing player
    draw_rectangle_rec(player, WHITE)

    end_drawing()

close_window()   
