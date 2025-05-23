#Farming Game
#2025-05-23

import pygame

pygame.init()
size = (1200,900)
screen = pygame.display.set_mode(size)

GREEN = (0,255,0)
BLUE = (0,0,255)

farming_grid = []
for y in range(12):
    farming_row = []
    for x in range(12):
        farming_row.append('EMPTY')
    farming_grid.append(farming_row)

for item in farming_grid:
    print(item)

def farming_hitbox(mouseX,mouseY):
    for y in range(len(farming_grid)):
        for x in range(len(farming_grid[y])):
            if x%2 == 0 and y%2 == 0:
                pygame.draw.rect(screen,GREEN,[75*x,75*y,75,75])
            elif x%2 == 1 and y%2 == 1:
                pygame.draw.rect(screen,GREEN,[75*x,75*y,75,75])
            else:
                pygame.draw.rect(screen,BLUE,[75*x,75*y,75,75])

farming_hitbox(1,2)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
