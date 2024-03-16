import pygame,sys,random
from pygame.math import Vector2

class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(screen,(183,191,122), snake_rect)

class Fruit:
    # The position of the fruit
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)

    # Draw the fruit
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)
            
pygame.init()
cell_size = 40
cell_number = 20
dt = 0
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

fruit = Fruit()
snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('gray')
    snake.draw_snake()
    fruit.draw_fruit()
    pygame.display.update()
    dt = clock.tick(60) / 1000