from InventoryManagement import *
from gamedata.CropData import CROP_DATA

def sell(crop, amount):
    price = CROP_DATA[crop]['sell_price']
    total = price * amount
    return total


print(sell('carrot',5))
print(sell('potato',5))
