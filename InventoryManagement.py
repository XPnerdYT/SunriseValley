from gamedata.CropData import CROP_DATA
from Variables import *
import json


reloadInv = True

### IMPORT / SAVE INVENTORY ###
with open('gamedata/Inventory.json', 'r') as invJson:
    inventory = json.load(invJson)
with open('gamedata/Gold.json', 'r') as goldJson:
    gold = json.load(goldJson)
def save_gold():
    with open('gamedata/Gold.json', 'w') as goldJson:
        json.dump(gold, goldJson)
def save_inventory():
    with open('gamedata/Inventory.json', 'w') as invJson:
        json.dump(inventory, invJson)


### TRIGGERING RELOAD OF ITEMS ###
def trigger_reload():
    global reloadInv
    reloadInv = True
    save_inventory()
    save_gold()    


### INDICATE RELOAD FINISHED ###
def reload_done():
    global reloadInv
    reloadInv = False


### CHECK RELOAD STATUS ###
def reload_check():
    return reloadInv

    
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
    trigger_reload()
    return 'Success'

### RETRIEVE INVENTORY ITEMS ###
def get_inventory():
    items = []
    for item in inventory:
        items.append(item)
    return items


### RETRIEVE ALL IMAGES FOR ALL ITEMS IN INVENTORY ###
def get_inventory_images():
    paths = []
    for item in inventory:
        paths.append(CROP_DATA[item]['image_path'])
    return paths

### RETRIEVE AMOUNT OF ITEM IN INVENTORY ###
def get_item_info(item):
    if item in inventory:
        return inventory[item]
    elif item not in inventory:
        return 0


### RETRIEVE IMAGE OF ANY ITEM ###
def get_item_image(item):
    if item in CROP_DATA:
        return CROP_DATA[item]['image_path']
    

### RETRIEVE TOTAL GOLD AMOUNT ###
def get_gold():
    return gold['gold']


### CHANGE GOLD AMOUNT ###
def change_gold(action, amount):
    if action == "subtract":
        gold['gold'] -= amount
    elif action == "add":
        gold['gold'] += amount
    trigger_reload()
    return gold



### DEBUGGING ###
if inventoryDebug:
    print(change_inventory("add", 'tomato', 4))
    print(get_item_info('reags'))
    print(get_inventory())
    print(get_item_image('carrot'))
    print(get_inventory_images())
    print(get_gold())
    print(change_gold('add', 100))
    ###########################################
    print(inventory)