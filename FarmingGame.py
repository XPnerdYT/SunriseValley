import pygame
import time

from gamedata.CropData import CROP_DATA
from Variables import *
from CropGrowth import *

pygame.init()
size = (1200,800)
screen = pygame.display.set_mode(size)

#Images
farmingBG = pygame.image.load('images/FarmingBackground.png')
farmingBG = pygame.transform.scale(farmingBG,[1200,800])

grid_hitboxes = []
for y in range(len(farming_grid)):
    grid_hitboxes_row = []
    for x in range(len(farming_grid)):
        grid_hitboxes_row.append([121+75*x-5*y,345+y*40-5*x,70,39])
    grid_hitboxes.append(grid_hitboxes_row)

counter = 0
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    screen.blit(farmingBG,[0,0])
    
    #Add a feature where player selects crops, for now we can just change this variable to test different crops
    selected = 'blueberry'
    
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
                    if farming_grid[numY][numX] == 'empty':
                        plant_crop(numX, numY, selected)
                    else:
                        harvest_crop(numX, numY)
    
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