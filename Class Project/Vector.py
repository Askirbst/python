import pygame # type: ignore
import math

class Vector:
    def __init__(self, x, y):
        self.vector = pygame.math.Vector2(x, y)
        # returns a vector for x and y

    def mult(self, scalar):
        
        # scales the vector
        
        self.vector *= scalar

    def add(self, x, y):
        # adds x and y to the vector allowing placement of drop where mouse clicked
        other = [x, y]
        self.vector += other

    def getX(self):
        # Get the x coordinate of the vector
        return self.vector.x

    def getY(self):
        # Get the y coordinate of the vector
        return self.vector.y
    
    def mag(self, x1, y1, x2, y2):
        # Get the magnitude of two coordinates
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


    def __str__(self):
        return str(self.vector)
