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
        'growth_stages': [120,240],
        'sell_price' : 25,
        'seed_cost': 10,
        'display_name': 'potato',
        'max_stage': 2,
        'renewable': False,
        'image_path': 'Potato.png',
        'image_stages': [image_load('Potato0.png'),image_load('Potato1.png'),image_load('Potato2.png')]
        },
    'tomato': {
        'growth_stages': [180,360,600,780],
        'sell_price': 10,
        'seed_cost': 100,
        'display_name': 'tomato',
        'max_stage': 4,
        'renewable': True,
        'image_path': 'crop.png',
        #'image_stages': [image_load('Tomato0.png'),image_load('Tomato1.png'),image_load('Tomato2.png'),image_load('Tomato3.png'),image_load('Tomato4.png')]
        },
    'blueberry': {
        'growth_stages': [240,480,720,780],
        'sell_price': 20,
        'seed_cost':250,
        'display_name': 'blueberry',
        'max_stage': 4,
        'renewable': True,
        'image_path': 'Blueberry.png',
        'image_stages': [image_load('Blueberry0.png'),image_load('Blueberry1.png'),image_load('Blueberry2.png'),image_load('Blueberry3.png'),image_load('Blueberry4.png')]
    }
}

