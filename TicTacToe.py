#Julie Cestaro
#11 August 2018

import random

def generateBoard(corners, middles, center):
    print(" {} | {} | {}".format(corners[0], middles[0], corners[1]))
    print(" ---------")
    print(" {} | {} | {}".format(middles[1], center, middles[2]))
    print(" ---------")
    print(" {} | {} | {}".format(corners[2], middles[3], corners[3]))

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


#Default index to -1, so I can leave out that when doing center
def canPlace(array, index=-1):
    print("array size: {}" .format(len(array)))
    print("index: {}".format(index))
    if index == -1:
        return array == " "
    return array[index] == " "

def computerPlace(corners, middles, center):
    placed = False

    while(not placed):
        location = random.randint(0,2)
        subsetOfLocation = random.randint(0,3)

        if location == 0 and canPlace(corners, subsetOfLocation):
            corners[subsetOfLocation] = "o"
            placed = True
        elif location == 1 and canPlace(middles, subsetOfLocation):
            middles[subsetOfLocation] = "o"
            placed = True
        elif location == 2 and canPlace(center):
            center = "o"
            placed = True
        else:
            print("Error: no valid case")

    return corners, middles, center

stop = ""

#initialize corners
#where 0 is upper left, 1 is upper right, 2 is lower left, 3 is lower right
corners = [" " for i in range(0, 4)]

#initialize middles
#where 0 is upper row center, 1 is left column center, 2 is right column center, 3 is bottom row center
middles = [" " for i in range(0, 4)]

#square in the center of the board
center = " "
location = ""

generateBoard(corners, middles, center)

while(True):

    placed = False

    while(not placed):
        location = input("Where would you like to place? ")

        if location == "ul" or location == "ur" or location == "ll" or location == "lr":
            setCorners(corners, location)
            placed = True
        elif location == "u" or location == "r" or location == "l" or location == "b":
            setMiddles(middles, location)
            placed = True
        elif location == "center" and canPlace(center):
            center = "x"
            placed = True
        else:
            print("Error: cannot place there, please try again")

    generateBoard(corners, middles, center)

    stop = input("Would you like to stop? (y/n) ")

    if stop == "y":
        break

    corners, middles, center = computerPlace(corners, middles, center)
    generateBoard(corners, middles, center)
