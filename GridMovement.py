#Grid Movement System
#2025-05-16

import pygame

pygame.init()
size = (800,800)
screen = pygame.display.set_mode(size)

#colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

#setting grid
def grid_draw(pX,pY):
    grid = [[0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0]]            
    grid[pY][pX] = 2
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                square = BLACK
            elif grid[y][x] == 1:
                square = WHITE
            elif grid[y][x] == 2:
                square = RED
            pygame.draw.rect(screen,square,[x*100,y*100,100,100])

#User input for movement            
def player_movement(pX, pY):
    keys = pygame.key.get_pressed()
    pygame.time.delay(80)
    
    if keys[pygame.K_a]: 
        if 0 < pX <= 7:
            pX -= 1
    elif keys[pygame.K_d]: 
        if 0 <= pX < 7:
            pX += 1
    elif keys[pygame.K_w]: 
        if 0 < pY <= 7:
            pY -= 1
    elif keys[pygame.K_s]: 
        if 0 <= pY < 7:
            pY += 1
            
    return pX, pY

pX = 0
pY = 0
clock = pygame.time.Clock()  
running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
    pX, pY = player_movement(pX,pY)   
    grid_draw(pX,pY)   
    pygame.display.flip()
    clock.tick(120)
pygame.quit()

    
