from InventoryManagement import *
from gamedata.CropData import CROP_DATA



def sell(crop):
    amount = inventory[crop]
    price = CROP_DATA[crop]['sell_price']
    total = price * amount
    inventory[crop] == 0
    
    trigger_reload()
    return total