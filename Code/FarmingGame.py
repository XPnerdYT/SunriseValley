#Farming Game
#Reagan
#2025-05-23

import pygame

pygame.init()
size = (1200,800)
screen = pygame.display.set_mode(size)

##Colours
BLACK = (0,0,0)
RED = (255,0,0)

##Images
farmingBG = pygame.image.load('FarmingBackground.png')
farmingBG = pygame.transform.scale(farmingBG,[1200,800])

##Creating the farming grid
farming_grid = []
for y in range(10):
    farming_row = []
    for x in range(10):
        farming_row.append('empty')
    farming_grid.append(farming_row)
for item in farming_grid:
    print(item)

#DELETE LATER------
clock = pygame.time.Clock()
running = True
#-----------------
while running:
    screen.fill(BLACK)
    screen.blit(farmingBG,[0,0])

    ##Hitboxes for planting crops in the farming grid
    for y in range(len(farming_grid)):
        for x in range(len(farming_grid)):
            pygame.draw.rect(screen,RED,[116+75*x-5*y,341+y*40-5*x,72,37],1)
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        pygame.draw.rect(screen,RED,[mouseX,mouseY,10,10],1)   
        
#DELETE LATER----- 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False          
            
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
#-----------------
