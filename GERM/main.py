import pygame
from variables import *
from main_character import Main_Character

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GERM")

main_character = Main_Character(50, 50, 5, 5, RED, screen)  # Pass screen as an argument

gameloop = True
while gameloop:
    screen.fill(BLACK)
    main_character.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

        # Movement of the character
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main_character.x -= 5
            if event.key == pygame.K_RIGHT:
                main_character.x += 5
            if event.key == pygame.K_UP:
                main_character.y -= 5
            if event.key == pygame.K_DOWN:
                main_character.y += 5

    pygame.display.update()

pygame.quit()
