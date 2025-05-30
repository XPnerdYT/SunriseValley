#FarmingGame Crop Test
#Reagan
#2025-05-24
import time
from CropData import CROP_DATA

farming_grid = []
for y in range(10):
    farming_row = []
    for x in range(10):
        farming_row.append('empty')
    farming_grid.append(farming_row)


def plant_crop(x,y,crop_type):
    if farming_grid[y][x] == 'empty':
        crop_grown = {
            'type' : crop_type,
            'growth_stage' : 0,
            'growth_timer' : 0,
            'growth_stages': CROP_DATA[crop_type]['growth_stages'],
            'max_stage': CROP_DATA[crop_type]['max_stage'],
            'mature': False
            }
        farming_grid[y][x] = crop_grown

def crop_growth(x,y):
    crop = farming_grid[y][x]
    
    print(crop)
    
    if crop == 'empty':
        return False
    
    if crop['mature'] == True:
        return False
    
    if not crop['mature']:
        crop['growth_timer'] += 1
        if crop['growth_timer'] == crop['growth_stages'][crop['growth_stage']]:
            crop['growth_stage'] += 1        
        
    if crop['growth_stage'] == crop['max_stage']:
        crop['mature'] = True            
    
    return True  

while True:
    plant_crop(2,1,'carrot')
    
    growth = crop_growth(2,1)
    
    time.sleep(0.0167)
    
    if growth:
        continue
    else:
        break 
