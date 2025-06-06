from InventoryManagement import *
from gamedata.CropData import CROP_DATA



def sell(crop, amount):
    price = CROP_DATA[crop]['sell_price']
    total = price * amount
    inventory[crop] -= amount
    return total