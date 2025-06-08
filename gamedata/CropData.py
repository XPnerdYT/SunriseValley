import pygame


def image_load(image_path):
    image = pygame.image.load('crops/' + image_path)
    image = pygame.transform.scale(image,[64,38])
    return image

CROP_DATA = {
    'carrot': {
        'growth_stages': [60,120,180],
        'sell_price': 3,
        'seed_cost': 2,
        'display_name': 'carrot',
        'max_stage': 3,
        'renewable': False,
        'image_path': 'Carrot.png',
        'image_stages': [image_load('Carrot0.png'),image_load('Carrot1.png'),image_load('Carrot2.png'),image_load('Carrot3.png')]
        },
    'potato': {
        'growth_stages': [240,480],
        'sell_price' : 40,
        'seed_cost': 20,
        'display_name': 'potato',
        'max_stage': 2,
        'renewable': False,
        'image_path': 'Potato.png',
        'image_stages': [image_load('Potato0.png'),image_load('Potato1.png'),image_load('Potato2.png')]
        },
    'tomato': {
        'growth_stages': [200,600,1020],
        'sell_price': 20,
        'seed_cost': 200,
        'display_name': 'tomato',
        'max_stage': 3,
        'renewable': True,
        'image_path': 'crop.png',
        'image_stages': [image_load('Tomato0.png'),image_load('Tomato1.png'),image_load('Tomato2.png'),image_load('Tomato3.png')]
        },
    'wheat':{
        'growth_stages': [80,160,240],
        'sell_price': 750,
        'seed_cost': 500,
        'display_name': 'wheat',
        'max_stage': 3,
        'renewable': False,
        'image_path': 'Wheat.png',
        'image_stages': [image_load('Wheat0.png'),image_load('Wheat1.png'),image_load('Wheat2.png'),image_load('Wheat3.png')]
        },
    'blueberry': {
        'growth_stages': [420,840,1260,1380],
        'sell_price': 500,
        'seed_cost':10000,
        'display_name': 'blueberry',
        'max_stage': 4,
        'renewable': True,
        'image_path': 'Blueberry.png',
        'image_stages': [image_load('Blueberry0.png'),image_load('Blueberry1.png'),image_load('Blueberry2.png'),image_load('Blueberry3.png'),image_load('Blueberry4.png')]
        },
    'corn': {
        'growth_stages': [240,480,720,1440],
        'sell_price': 2000,
        'seed_cost': 50000,
        'display_name': 'corn',
        'max_stage': 4,
        'renewable': True,
        'image_path': 'Corn.png',
        'image_stages': [image_load('Corn0.png'),image_load('Corn1.png'),image_load('Corn2.png'),image_load('Corn3.png'),image_load('Corn4.png')]
        },
    'pumpkin': {
        'growth_stages': [600,1200,1800],
        'sell_price': 100000,
        'seed_cost': 40000,
        'display_name': 'pumpkin',
        'max_stage': 3,
        'renewable': False,
        'image_path': 'Pumpkin.png',
        'image_stages': [image_load('Pumpkin0.png'),image_load('Pumpkin.png'),image_load('Pumpkin.png'),image_load('Pumpkin3.png')]
        },
    'd': {
        'growth_stages': [240,480,720,780],
        'sell_price': 20,
        'seed_cost':250,
        'display_name': 'blueberry',
        'max_stage': 4,
        'renewable': True,
        'image_path': 'Blueberry.png',
        'image_stages': [image_load('Blueberry0.png'),image_load('Blueberry1.png'),image_load('Blueberry2.png'),image_load('Blueberry3.png'),image_load('Blueberry4.png')]
        },
    'c': {
        'growth_stages': [240,480,720,780],
        'sell_price': 20,
        'seed_cost':250,
        'display_name': 'blueberry',
        'max_stage': 4,
        'renewable': True,
        'image_path': 'Blueberry.png',
        'image_stages': [image_load('Blueberry0.png'),image_load('Blueberry1.png'),image_load('Blueberry2.png'),image_load('Blueberry3.png'),image_load('Blueberry4.png')]
        },
    'mushroom': {
        'growth_stages': [600,1200,1800,2400],
        'sell_price': 5000000,
        'seed_cost': 1000000,
        'display_name': 'mushroom',
        'max_stage': 4,
        'renewable': False,
        'image_path': 'Mushroom.png',
        'image_stages': [image_load('Mushroom0.png'),image_load('Mushroom1.png'),image_load('Mushroom2.png'),image_load('Mushroom3.png'),image_load('Mushroom4.png')]
        },
    'rgbberry': {
        'growth_stages': [600,1200,1800,2000],
        'sell_price': 1000000,
        'seed_cost':10000000,
        'display_name': 'rgbberry',
        'max_stage': 4,
        'renewable': True,
        'image_path': 'Rgbberry.png',
        'image_stages': [image_load('Rgbberry0.png'),image_load('Rgbberry1.png'),image_load('Rgbberry2.png'),image_load('Rgbberry3.png'),image_load('Rgbberry4.png')]
    
    }
}

