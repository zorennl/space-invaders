from pyray import *
from random import randint, choice

# General entity class 
class Entity:
    alive = 1

    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

# Defining player 
player = Rectangle(45,90,10,10)

# Defining lists for drawing entities
enemies = []
bullets = []

# Initiating window
init_window(100, 100, "raylib spaceinvaders")
set_target_fps(60)

# Defining functions for entities
def summon_entity(entity, entity_list: []):
    entity_list.append(entity)   
def draw_entity(entity):
    draw_circle(entity.x,entity.y,entity.size,entity.color)
    
while not window_should_close():

    # Defining entities
    bullet = Entity(int(player.x+5),int(player.y),3,RED)
    enemy = Entity(randint(6,94),6,5,BLUE)

    begin_drawing()
    clear_background(BLACK)

    # Drawing player
    draw_rectangle_rec(player, WHITE)

    # Movement
    if is_key_down(KeyboardKey.KEY_A) and player.x > 0:
        player.x -= 1
    if is_key_down(KeyboardKey.KEY_D) and player.x < 90:
        player.x += 1

    # Combat
    if is_key_pressed(KeyboardKey.KEY_SPACE):
        summon_entity(bullet,bullets)

    if is_key_pressed(KeyboardKey.KEY_R):
        summon_entity(enemy,enemies)

    # Draw entities
    for i in enemies:
        draw_entity(i)

    for i in bullets:
        draw_entity(i)
        i.y -= 1

    # Removing dead entities and useen entities
    for obj in enemies[:]:
        if obj.alive != 1:
            del enemies[enemies.index(obj)]

    for obj in bullets[:]:
        if obj.alive != 1 or obj.y < -2:
            del bullets[bullets.index(obj)]


    # Detecting colision between a bullet and a enemy
    for b in bullets:
        for e in enemies:
            dist_x = abs(b.x - e.x)
            dist_y = abs(b.y - e.y)
            dist = dist_x + dist_y
            if dist < 3 + e.size:
                b.alive = 0
                e.alive = 0

    # DEBUG
    draw_text(f'bullets:{len(bullets)}\nenemies:{len(enemies)}',0,0,5,GREEN)

    end_drawing()

close_window()   
