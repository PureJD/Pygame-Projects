import pygame
from variables import *



# Initialize the game   
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("GERM")

class Main_Character:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


main_character = Main_Character(50, 50, 5, 5, RED)




gameloop = True
while gameloop:
    screen.fill(BLACK)
    main_character.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        
        # movement of the character
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