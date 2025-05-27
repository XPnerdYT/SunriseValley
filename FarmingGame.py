#Farming Game
#2025-05-23

import pygame

pygame.init()
size = (1200,900)
screen = pygame.display.set_mode(size)

GREEN = (100,245,0)
DARKGREEN = (10,120,0)

farming_grid = []
for y in range(12):
    farming_row = []
    for x in range(12):
        farming_row.append('empty')
    farming_grid.append(farming_row)

for item in farming_grid:
    print(item)


pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
