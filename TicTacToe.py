#Julie Cestaro
#11 August 2018

def generateBoard(corners, middles, center):
    #someInt = 0
    #print("hello\nworld %d" % someInt)
    print(" %s | %s | %s\n ---------\n %s | %s | %s\n ---------\n %s | %s | %s\n" % (corners[0], middles[0], corners[1], middles[1], center, middles[2], corners[2], middles[3], corners[3]))
    #print("%s|%s" % (boardArray[0], boardArray[1]))

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
    if where == "ul":
        corners[0] = "x"
    elif where == "ur":
        corners[1] = "x"
    elif where == "ll":
        corners[2] = "x"
    elif where == "lr":
        corners[3] = "x"
    else:
        print("Error: no valid case")

def setMiddles(middles, where):
    if where == "u":
        middles[0] = "x"
    elif where == "l":
        middles[1] = "x"
    elif where == "r":
        middles[2] = "x"
    elif where == "b":
        middles[3] = "x"
    else:
        print("Error: no valid case")


stop = ""

#where positions 0-2 are the top row, 3-5 are the middle, 6-8 are bottom
#boardState = []
#initialize boardState
# for i in range(0, 9):
#     boardState.append(" ")

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

#generateBoard(corners, middles, center)

while(True):
    # stop = input("Would you like to stop? (y/n) ")
    #
    # if stop == "y":
    #     break

    generateBoard(corners, middles, center)
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
