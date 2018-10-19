from map import rooms
from player import *
from items import *
from gameparser import *

room = rooms["Reception"]

item_here = list_of_items(room["items"])

if item_here:
    print("There is " + item_here + " here.")
    print("")
