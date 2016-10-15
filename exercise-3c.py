# Global canvas/spelbräde:
canvas = {(xpos, ypos):"player"}

def place_piece(xpos, ypos, "player"):
    if xpos or ypos < 0:
        return False
    elif xpos or ypos > 100000:
        return False
    else:
        canvas = canvas{(xpos, ypos): "player"}
        return canvas

def isfree(xpos, ypos):

    if not xpos, ypos in canvas:
        return True
    else:
        return False
#Mumsigt med bajs, inte sant?
"""def distance(xpos, ypos, xpos1, ypos1):
    lengthx = (xpos)-(xpos1)
    lengthy = (ypos)-(ypos1)

    hypotenuse = ((lengthx**2)+(lengthy**2))

    return hypothenuse
"""
def get_piece(xpos, ypos):
    if xpos, ypos in canvas:
        return "player"

def remove_piece(xpos, ypos):
    del canvas{(xpos, ypos)}
    return canvas

def move_piece(xpos, ypos, new_xpos, new_ypos):
    canvas{(new_xpos, new_ypos)} = canvas.pop{(xpos, ypos)}
    return canvas

def count("direction", pos, "player"):
    res = 0
    if "direction" == "column":
