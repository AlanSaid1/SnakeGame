import pygame,sys
from pygame.math import Vector2

class Fruit:
    # The position of the fruit
    def __init__(self):
        self.x = 4
        self.y = 5
        self.position = Vector2(self.x, self.y)

    # Draw the fruit
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.position.x, self.position.y, cell_size, cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
cell_size = 40
player_pos = pygame.rect.Rect(100, 100, 40, 40)

fruit = Fruit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('gray')

    pygame.draw.rect(screen, "blue", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    fruit.draw_fruit()
    pygame.display.update()
    dt = clock.tick(60) / 1000