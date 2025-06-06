from gamedata.CropData import CROP_DATA
import pygame

farming_grid = []
for y in range(10):
    farming_row = []
    for x in range(10):
        farming_row.append('empty')
    farming_grid.append(farming_row)


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
            'image_stages': CROP_DATA[crop_type]['image_stages'],
            }
        farming_grid[y][x] = crop_grown

def crop_growth(x,y,tick):
    crop = farming_grid[y][x]
    
    if crop == 'empty':
        return False 
    
    cropImg = crop['image_stages'][crop['growth_stage']]
    
    if crop['mature'] == True:
        return cropImg         
        
    if not crop['mature']:
        crop['growth_timer'] += tick
        if crop['growth_timer'] == crop['growth_stages'][crop['growth_stage']]:
            crop['growth_stage'] += 1
            if crop['growth_stage'] == crop['max_stage']:
                crop['mature'] = True
                
    farming_grid[y][x] = crop
                   
    return cropImg   

def harvest_crop(x,y):
    crop = farming_grid[y][x]
    if crop == 'empty':
        return False  
    
    if crop['mature']:
        #change_inventory('add',crop['type'],1)
        
        if crop['renewable']:
            crop['growth_stage'] = crop['max_stage'] - 1
            crop['growth_timer'] = crop['growth_stages'][crop['growth_stage']-1]
            crop['mature'] = False
            farming_grid[y][x] = crop
            return True
            
        else:
            crop = 'empty'  
   
            farming_grid[y][x] = crop         
            return True
    
    return False