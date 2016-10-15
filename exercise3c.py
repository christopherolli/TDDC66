figures = {}
sizeX = 100000
sizeY = 100000

def place_piece(posX, posY, key):
    if key in figures:
        return False
    if posX > sizeX or posY > sizeY or posX < 0 or posY < 0:
        return False
    for figure in figures:
        if figure[0] == posX and figure[1] == posY:
            return False
    figures[str(key)] = [posX, posY]

def is_free(posX, posY):
    for key, figure in figures.items():
        if figure[0] == posX and figure[1] == posY:
            return False
    return True

def get_piece(posX, posY):
    for key, figure in figures.items():
        if figure[0] == posX and figure[1] == posY:
            return key
    return False
