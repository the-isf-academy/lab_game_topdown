from math import sqrt 

def scale(vector, magnitude):
    vx, vy = vector
    old_magnitude = sqrt(vx * vx + vy * vy) if vx * vx + vy * vy else 0
    factor = magnitude / old_magnitude
    return vx * factor, vy * factor