#Julie Cestaro
#11 August 2018

import random

def generateBoard(corners, middles, center):
    print(" %s | %s | %s\n ---------\n %s | %s | %s\n ---------\n %s | %s | %s\n" % (corners[0], middles[0], corners[1], middles[1], center, middles[2], corners[2], middles[3], corners[3]))

# def setNonSpec(thingToSet, mode, where):
#     if mode == "corners":
#         setCorners(thingToSet, where)
#     elif mode == "middles":
#         setMiddles(thingToSet, where)
#     elif mode == "center":
#         thingToSet = "x"
#     else:
#         print("Error: no valid case")

def setCorners(corners, where):
    if where == "ul" and canPlace(corners, 0):
        corners[0] = "x"
    elif where == "ur" and canPlace(corners, 0):
        corners[1] = "x"
    elif where == "ll" and canPlace(corners, 0):
        corners[2] = "x"
    elif where == "lr" and canPlace(corners, 0):
        corners[3] = "x"
    else:
        print("Error: no valid case")

def setMiddles(middles, where):
    if where == "u" and canPlace(middles, 0):
        middles[0] = "x"
    elif where == "l" and canPlace(middles, 0):
        middles[1] = "x"
    elif where == "r" and canPlace(middles, 0):
        middles[2] = "x"
    elif where == "b" and canPlace(middles, 0):
        middles[3] = "x"
    else:
        print("Error: no valid case")

def canPlace(array, index):
    if array[index] == " ":
        return True
    else:
        return False

def computerPlace(corners, middles, center):
    location = random.randint(0,3)
    subsetOfLocation = random.randint(0,4)

    if location == 0:
        corners[subsetOfLocation] = "o"
    elif location == 1:
        middles[subsetOfLocation] = "o"
    else:
        center = "o"

    return corners, middles, center

stop = ""

#where 0 is upper left, 1 is upper right, 2 is lower left, 3 is lower right
corners = []
#initialize corners
for i in range(0, 4):
    corners.append(" ")

#where 0 is upper row center, 1 is left column center, 2 is right column center, 3 is bottom row center
middles = []
#initialize middles
for i in range(0, 4):
    middles.append(" ")

#square in the center of the board
center = " "
location = ""

generateBoard(corners, middles, center)

while(True):

    location = input("Where would you like to place? ")

    if location == "ul" or location == "ur" or location == "ll" or location == "lr":
        setCorners(corners, location)
    elif location == "u" or location == "r" or location == "l" or location == "b":
        setMiddles(middles, location)
    elif location == "center":
        center = "x"
    else:
        print("Error: no valid case")

    generateBoard(corners, middles, center)

    stop = input("Would you like to stop? (y/n) ")

    if stop == "y":
        break

    corners, middles, center = computerPlace(corners, middles, center)
    generateBoard(corners, middles, center)
