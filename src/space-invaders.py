from pyray import *
from random import randint, choice
from os.path import join as os

# Defining variables
debug = False

# General entity class 
class Entity:
    alive = 1

    def __init__(self, sprite=None, index=None, rectangle=Rectangle, color=None):
        self.sprite = sprite
        self.index = index
        self.rectangle = rectangle
        self.color = color

# Defining player 
player_pos = Vector2(42,84)
player_sprite = os('assets','space_invaders_player.png')

# Defining lists for drawing entities
enemies = []
enemy_sprite = os('assets','space_invaders_enemies.png')
bullets = []

# Initiating window
init_window(100, 100, "raylib spaceinvaders")
set_target_fps(60)

# Loading textures
player_sprite = load_texture(player_sprite)
enemy_sprite = load_texture(enemy_sprite)

# Defining functions for entities
def summon_entity(entity, entity_list: []):
    entity_list.append(entity)   
    
while not window_should_close():

    # Defining entities
    bullet = Entity(None ,None, Rectangle(int(player_pos.x+8),int(player_pos.y), 3, 3), RED)
    enemy = Entity(enemy_sprite, None, Rectangle(0,0,32,32),WHITE)

    begin_drawing()
    clear_background(BLACK)

    # Drawing player
    draw_texture_ex(player_sprite,player_pos,0,.5,WHITE)
    # Movement
    if is_key_down(KEY_A) and player_pos.x > 0:
        player_pos.x -= 1
    if is_key_down(KEY_D) and player_pos.x < 84:
        player_pos.x += 1
    if is_key_down(KEY_UP) and player_pos.y > -3:
        player_pos.y -= 1
    if is_key_down(KEY_DOWN) and player_pos.y < 84:
        player_pos.y += 1
    if is_key_pressed(KEY_F3):
        debug = not debug

    # Combat
    if is_key_pressed(KeyboardKey.KEY_SPACE):
        summon_entity(bullet,bullets)

    if is_key_pressed(KeyboardKey.KEY_R):
        summon_entity(enemy,enemies)

    # Draw entities
    for i in enemies:
        draw_texture(i.sprite, int(i.rectangle.x), int(i.rectangle.y), i.color)

    for i in bullets:
        draw_rectangle(int(i.rectangle.x),int(i.rectangle.y),int(i.rectangle.width),int(i.rectangle.height),i.color)
        i.rectangle.y -= 1

    # Removing dead entities and useen entities
    # for obj in enemies[:]:
    #     if obj.alive != 1:
    #         del enemies[enemies.index(obj)]

    # for obj in bullets[:]:
    #     if obj.alive != 1 or obj.y < -2:
    #         del bullets[bullets.index(obj)]

    # DEBUG
    if debug:
        draw_text(f'bullets:{len(bullets)}\nenemies:{len(enemies)}\nx:{player_pos.x} y:{player_pos.y}',0,0,5,GREEN)

    end_drawing()

close_window()   
