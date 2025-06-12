from gamedata.CropData import *
import pygame
from gamedata.FarmingGrid import farming_grid

def plant_crop(x,y,crop_type):
    if crop_type == None:
        return
    if farming_grid[y][x] == 'empty':
        crop_grown = {
            'type' : crop_type,
            'growth_stage' : 0,
            'growth_timer' : 0,
            'mature': False,
            'growth_stages': CROP_DATA[crop_type]['growth_stages'],
            'max_stage': CROP_DATA[crop_type]['max_stage'],
            'renewable': CROP_DATA[crop_type]['renewable'],
            }
        farming_grid[y][x] = crop_grown

def crop_growth(x,y,tick):
    #Stores value of select square in grid
    crop = farming_grid[y][x]

    #Stops function if the square is empty
    if crop == 'empty':
        return None 

    #Gets crop image
    cropImg = CROP_DATA[crop['type']]['image_stages'][crop['growth_stage']]

    #If crop is mature no growth is required
    if crop['mature'] == True:
        return cropImg         

    #Growing if crop is not mature
    if not crop['mature']:
        crop['growth_timer'] += tick
        #Changing growth stage if growth timer reaches a certain point
        if crop['growth_timer'] == crop['growth_stages'][crop['growth_stage']]:
            crop['growth_stage'] += 1
            #Setting crop to mature when growth stage reaches max stage
            if crop['growth_stage'] == crop['max_stage']:
                crop['mature'] = True
    #Applying modifications back to farming grid
    farming_grid[y][x] = crop
                   
    return cropImg  

def harvest_crop(x,y):
    crop = farming_grid[y][x]
    #Does not harvest if empty
    if crop == 'empty':
        return False  

    #Harvesting if crop is mature
    if crop['mature']:
        #Leaves crop at 2nd last stage if renewable 
        if crop['renewable']:
            crop['growth_stage'] = crop['max_stage'] - 1
            crop['growth_timer'] = crop['growth_stages'][crop['growth_stage']-1]
            crop['mature'] = False
            farming_grid[y][x] = crop
            #Tells program if harvest happened
            return True
        #Deletes the crop if not renewable    
        else:
            crop = 'empty'  
   
            farming_grid[y][x] = crop 
            #Tells program if harvest happened
            return True
    
    return False