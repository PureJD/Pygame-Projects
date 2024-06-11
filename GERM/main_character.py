import pygame

class Main_Character:
    def __init__(self, x, y, width, height, color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.screen = screen  # Pass screen as a parameter and store it as an attribute

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    
    def collision(self, enemy):
        if self.x < enemy.x + enemy.width and self.x + self.width > enemy.x and self.y < enemy.y + enemy.height and self.y + self.height > enemy.y:
            return True
        return False
