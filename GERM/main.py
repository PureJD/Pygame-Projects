import random 
import pygame
from variables import *
from main_character import Main_Character
from enemies import Enemy

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GERM")

# Creation of the main character object 
main_character = Main_Character(50, 50, 5, 5, RED, screen)

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
    for i in range(len(small_enemy_collection)):
        small_enemy_collection[i].draw()
    for i in range(len(medium_enemy_collection)):
        medium_enemy_collection[i].draw()
    for i in range(len(large_enemy_collection)):
        large_enemy_collection[i].draw()
        
        
        
        
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

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

pygame.quit()
