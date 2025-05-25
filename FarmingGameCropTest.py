#FarmingGame Crop Test
#2025-05-24
import time

farming_grid = []
for y in range(10):
    farming_row = []
    for x in range(8):
        farming_row.append('empty')
    farming_grid.append(farming_row)

CROP_DATA = {
    'carrot': {
        'growth_stages': [10,20,30],
        'sell_price': 5,
        'seed_cost': 2,
        'display_name': 'carrot',
        'max_stage': 3,
        'renewable': False,
        },
    }

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
        farming_grid[y][x] = crop_instance

def crop_growth(x,y):
    crop = farming_grid[y][x]
    
    print(crop)
    
    if crop == 'empty':
        return None
    
    if crop['mature'] == True:
        return False
    
    if not crop['mature']:
        crop['growth_timer'] += 1
        if crop['growth_timer'] == crop['growth_stages'][crop['growth_stage']]:
            crop['growth_stage'] += 1        
        
    if crop['growth_stage'] == crop['max_stage']:
        crop['mature'] = True            
    
    return True   
