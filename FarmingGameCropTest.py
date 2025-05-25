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
        'display_name': 'Carrot',
        'max_stage': 3,
        'renewable': False,
        },
    }

def plant_crop(x,y,crop_type,farming_grid):
    if farming_grid[y][x] == 'empty':
        crop_instance = {
            'type' : crop_type,
            'growth_stage' : 0,
            'growth_timer' : 0,
            'growth_stages': CROP_DATA[crop_type]['growth_stages'][:],
            'max_stage': CROP_DATA[crop_type]['max_stage'],
            'mature': False
            }
        farming_grid[y][x] = crop_instance
    return farming_grid

farming_grid = plant_crop(1,2,'carrot',farming_grid)

for i in range(100):
    crop = farming_grid[2][1]
    
    print(crop)
    
    if crop['mature'] == True:
        break    
    
    if not crop['mature']:
        crop['growth_timer'] += 1
        if crop['growth_timer'] == crop['growth_stages'][crop['growth_stage']]:
            crop['growth_stage'] += 1        
        
    if crop['growth_stage'] == crop['max_stage']:
        crop['mature'] = True            
        
    time.sleep(0.5)
    

print("Ready for harvest!")