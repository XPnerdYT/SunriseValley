#Farming Game
#2025-05-23

import pygame

pygame.init()
size = (1200,800)
screen = pygame.display.set_mode(size)

BLACK = (0,0,0)
RED = (255,0,0)

farmingBG = pygame.image.load('FarmingBackground.png')
farmingBG = pygame.transform.scale(farmingBG,[1200,800])

farming_grid = []
for y in range(10):
    farming_row = []
    for x in range(10):
        farming_row.append('empty')
    farming_grid.append(farming_row)

for item in farming_grid:
    print(item)

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)
    screen.blit(farmingBG,[0,0])
    
    for y in range(len(farming_grid)):
        for x in range(len(farming_grid)):
            pygame.draw.rect(screen,RED,[115+75*x-4*y,340+y*40-5*x,72,37],2)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
