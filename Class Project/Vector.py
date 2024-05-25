import pygame # type: ignore
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vector = pygame.math.Vector2(x, y)
        # returns a vector for x and y

    def mult(self, scalar):
        
        # scales the vector
        
        self.vector *= scalar

    def add(self, x=None, y=None, vec=None):
        # adds x and y to the vector allowing placement of drop where mouse clicked
        if vec is not None:
            self.x = vec.x
            self.y = vec.y
        else:
            if x is not None:
                self.x = x
            if y is not None:
                self.y = y
        other = pygame.math.Vector2(self.x, self.y)
        self.vector += other

    def sub(self, x=None, y=None, vec=None):
        # subtracts another vector or x and y components from the current vector.
        if vec is not None:
            self.x = vec.x
            self.y = vec.y
        else:
            if x is not None:
                self.x = x
            if y is not None:
                self.y = y
        other = pygame.math.Vector2(self.x, self.y)
        self.vector -= other
    
    def set(self, x=None, y=None, vec=None):
        if vec is not None:
            self.x = vec.x
            self.y = vec.y
        else:
            if x is not None:
                self.x = x
            if y is not None:
                self.y = y

    def getX(self):
        # Get the x coordinate of the vector
        return self.vector.x

    def getY(self):
        # Get the y coordinate of the vector
        return self.vector.y
    
    def mag(self):
        # Get the magnitude of the coordinate
        return math.sqrt(self.x**2 + self.y**2)


    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
