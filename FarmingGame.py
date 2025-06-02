
import pygame
import time

from gamedata.CropData import CROP_DATA
from Variables import *
from CropGrowth import plant_crop, crop_growth, farming_grid

pygame.init()
size = (1200,800)
screen = pygame.display.set_mode(size)

#Images
farmingBG = pygame.image.load('images/FarmingBackground.png')
farmingBG = pygame.transform.scale(farmingBG,[1200,800])

#Display grid for debug
for item in farming_grid:
    print(item)

grid_hitboxes = []
for y in range(len(farming_grid)):
    grid_hitboxes_row = []
    for x in range(len(farming_grid)):
        grid_hitboxes_row.append([116+75*x-5*y,343+y*40-5*x,70,39])
    grid_hitboxes.append(grid_hitboxes_row)
for item in grid_hitboxes:
    print(item)

#Grid to store whether a crop is growing or not    
growth_grid = []
for y in range(10):
    growth_row = []
    for x in range(10):
        growth_row.append(False)
    growth_grid.append(growth_row)
for item in growth_grid:
    print(item)

counter = 0
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    screen.blit(farmingBG,[0,0])
    
    #Adds a tick every 5 frames
    tick = 0
    counter += 1
    if counter % 5 == 0:
        tick = 1
        counter = 0
    
    #Gets location and checks if mouse is pressed        
    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        
        #updating grid to plant crops
        for numY, row in enumerate(grid_hitboxes):
            for numX, rect in enumerate(row):
                if pygame.Rect(rect).collidepoint(mouseX, mouseY):
                    #'carrot' should become a variable for a crop that is selected by the player
                    plant_crop(numX, numY, 'potato')
    
    #updating planted crops
    for y in range(len(farming_grid)):
        for x in range(len(farming_grid[y])):
            cropImg = crop_growth(x,y,tick)
            if cropImg != False:
                screen.blit(cropImg,(grid_hitboxes[y][x][:2]))
                

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False          
            
    pygame.display.flip()
    clock.tick(fps)
