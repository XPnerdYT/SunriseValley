from CropData import CROP_DATA
from Variables import *
import json


### IMPORT / SAVE INVENTORY ###
with open('Inventory.json', 'r') as invJson:
    inventory = json.load(invJson)
def save_inventory():
    with open('Inventory.json', 'w') as invJson:
        json.dump(inventory, invJson)


### INVENTORY MANAGEMENT ADD / REMOVE / SUBTRACT ITEMS FUNCTIONS ###
def change_inventory(action, item, count = 0):
    
    if action == "add":
        if item not in inventory:
            inventory[item] = count
        elif item in inventory:
            inventory[item] += count
        else:
            return "Error: Could not add item"
        
    elif action == "subtract":
        if item in inventory:
            if inventory[item] >= count:
                inventory[item] -= count
                if inventory[item] == 0:
                    inventory.pop(item)
            elif inventory[item] < count:
                return "Error: Subtract amount is larger than amount in inventory."
        else:
            return "Error: Could not subtract item"
    
    elif action == "remove":
        if item in inventory:
            inventory.pop(item)
        else:
            return "Error: Could not remove specified item."
    return 'Success'

def get_inventory():
    items = []
    for item in inventory:
        items.append(item)
    return items

def get_inventory_images():
    paths = []
    for item in inventory:
        paths.append(CROP_DATA[item]['image_path'])
    return paths

def get_item_info(item):
    if item in inventory:
        return inventory[item]
    elif item not in inventory:
        return 0

def get_item_image(item):
    if item in CROP_DATA:
        return CROP_DATA[item]['image_path']
    
print(change_inventory("add", 'tomato', 4))
print(get_item_info('reags'))
print(get_inventory())
print(get_item_image('carrot'))
print(get_inventory_images())
save_inventory()

if debug:
    print(inventory)