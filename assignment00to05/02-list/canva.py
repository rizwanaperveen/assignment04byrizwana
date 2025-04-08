import pygame
import time
pygame.init()

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
CELL_SIZE = 60
ERASER_SIZE = 30

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption("Enter effect in pygame")

grid = []

for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE) 
        grid.append(rect)

eraser = pygame.Rect(300, 300, ERASER_SIZE, ERASER_SIZE)
running = True
while running:

    screen.fill(WHITE)

    for rect in grid:
        pygame.draw.rect(screen, BLUE, rect)
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y)
    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):
            new_grid.append(rect)

    grid = new_grid

    pygame.draw.rect(screen, GREEN, eraser)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    time.sleep(0.1)

pygame.quit()