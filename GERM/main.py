import random 
import pygame
from variables import *
from main_character import Main_Character
from enemies import Enemy

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GERM")

# To adjust the speed of the game (60 frames per second)
clock = pygame.time.Clock()

# Creation of the main character object 
main_character = Main_Character(50, 50, main_character_size, main_character_size, RED, screen)

small_enemy_collection = []
for i in range(100):
    enemy = Enemy(random.randint(0, WIDTH), random.randint(0, HEIGHT), 5, 5, BLUE, screen)
    small_enemy_collection.append(enemy)

medium_enemy_collection = []
for i in range(50):
    enemy = Enemy(random.randint(0, WIDTH), random.randint(0, HEIGHT), 10, 10, GREEN, screen)
    medium_enemy_collection.append(enemy)
    
large_enemy_collection = []
for i in range(20):
    enemy = Enemy(random.randint(0, WIDTH), random.randint(0, HEIGHT), 20, 20, YELLOW, screen)
    large_enemy_collection.append(enemy)


gameloop = True
while gameloop:
    # Fill the background screen with black color
    screen.fill(BLACK)
    # Draw the main character
    main_character.draw()
    
    # Draw the enemy
    for enemy in small_enemy_collection + medium_enemy_collection + large_enemy_collection:
        enemy.draw()
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    # Check for collision between the main character and the enemy
    for enemy in small_enemy_collection + medium_enemy_collection + large_enemy_collection:
        if main_character.collision(enemy):
            main_character_size += 1
            main_character = Main_Character(50, 50, main_character_size, main_character_size, RED, screen)
            


    # key press events that allow for the button to be held down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        main_character.x -= 5
    if keys[pygame.K_RIGHT]:
        main_character.x += 5
    if keys[pygame.K_UP]:
        main_character.y -= 5
    if keys[pygame.K_DOWN]:
        main_character.y += 5
                

    pygame.display.update()
    clock.tick(60)

pygame.quit()
