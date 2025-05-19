#Grid Movement System
#2025-05-16

import pygame

pygame.init()
size = (800,800)
screen = pygame.display.set_mode(size)

#colours
RED = (255,0,0)
GRASS1 = (51, 138, 55)
GRASS2 = (29, 102, 32)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

#setting grid
def grid_draw(pX,pY):
    row = []
    for i in range(16):
        if i % 2 == 0:
            row.append(0)
        elif i % 2 == 1:
            row.append(1)
    rowR = list(reversed(row))
    grid = []
    for i in range(16):
        if i%2 == 0:
            grid.append(row[:])
        elif i%2 == 1:
            grid.append(rowR[:])            
    grid[pY][pX] = 2
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                square = GRASS1
            elif grid[y][x] == 1:
                square = GRASS2
            elif grid[y][x] == 2:
                square = RED
            pygame.draw.rect(screen,square,[x*50,y*50,50,50])

#User input for movement            
def player_movement(pX, pY):
    keys = pygame.key.get_pressed()
    pygame.time.delay(50)
    
    if keys[pygame.K_a]: 
        if 0 < pX <= 15:
            pX -= 1
    elif keys[pygame.K_d]: 
        if 0 <= pX < 15:
            pX += 1
    elif keys[pygame.K_w]: 
        if 0 < pY <= 15:
            pY -= 1
    elif keys[pygame.K_s]: 
        if 0 <= pY < 15:
            pY += 1
            
    return pX, pY

pX = 0
pY = 0
clock = pygame.time.Clock()  
running = True
while running:
    screen.fill(BLACK)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
    pX, pY = player_movement(pX,pY)   
    grid_draw(pX,pY)   
    pygame.display.flip()
    clock.tick(120)
pygame.quit()

    
