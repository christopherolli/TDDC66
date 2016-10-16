import math
figures = {}
sizeX = 100000
sizeY = 100000

def place_piece(posX, posY, key):
    if not key in figures:
        figures[key] = []
    if posX > sizeX or posY > sizeY or posX < 0 or posY < 0:
        return False
    if not isfree(posX, posY):
        return False
    figures[str(key)].append([posX, posY])

def isfree(posX, posY):
    for playerKey, player in figures.items():
        if [posX, posY] in player:
            return False
    return True

def get_piece(posX, posY):
    for playerKey, player in figures.items():
        if [posX, posY] in player:
            return playerKey
    return False
    
def remove_piece(posX, posY):
    for playerKey, player in figures.items():
        for index, figure in enumerate(player):
            if figure[0] == posX and figure[1] == posY:
                del figures[playerKey][index]
                return True
    return False

def move_piece(posX, posY, newPosX, newPosY):
    for playerKey, player in figures.items():
        for index, figure in enumerate(player):
            if figure[0] == posX and figure[1] == posY:
                del figures[playerKey][index]
                place_piece(newPosX, newPosY, playerKey)
                return True 
    return False

def count(direction, pos, key):
    counter = 0
    if direction == "column":
        for key, figure in enumerate(figures[key]):
            if figure[0] == pos:
                counter += 1
                
    elif direction == "row":
        for key, figure in enumerate(figures[key]):
            if figure[1] == pos:
                counter += 1
                
    return counter

def nearest_piece(posX, posY):
    dist = None
    closest = {}
    for playerKey, player in figures.items():
        for index, figure in enumerate(player):
            tempDist = distance(posX, posY, figure[0], figure[1]) 
            if dist == None or tempDist < dist:
                dist = tempDist
                closest = figure
                
    return closest

def distance(posX1, posY1, posX2, posY2):
   return math.sqrt(((posX1-posX2)+(posY1-posY2))**2)
    
