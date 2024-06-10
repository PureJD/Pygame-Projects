import pygame

# Initialize the game   
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((2200, 1200))

# Set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the window name    
pygame.display.set_caption("GERM")

gameloop = True
while gameloop:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

    pygame.display.update()