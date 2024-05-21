import pygame # type: ignore
import math
import copy
from Vector import Vector

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

TWO_PI = math.pi * 2

drops = []
circleDetail = 100
radius = 50

angle_increment = 2 * math.pi / circleDetail

def mapValue(value, start1, stop1, start2, stop2):
    """
    Maps a value from one range to another.
    
    Parameters:
    - value: The value to be mapped.
    - start1, stop1: The range in which the value currently lies.
    - start2, stop2: The range in which the value should be mapped.

    """
    return ((value-start1)/(stop1-start1))*(stop2-start2)+start2


class Drop:

    def __init__(self, x, y, r, s): # Initialize a Class object with parameters (x, y, r, s) x and y are coordinates, r is the radius, and s is smoothing of circle (number of sides of polygon)
        self.center = Vector(x,y)
        self.r = r
        self.s = s

        self.vertices = []

        for i in range(s):
            angle = mapValue(i, 0, s, 0, TWO_PI)
            vector = Vector(math.cos(angle), math.sin(angle)) # Confusing math I don't quite understand yet but its works so...
            vector.mult(self.r) # Multiplies the points in vector to the radius to scale the drop
            vector.add(x, y) # Add the value of the x, y coordinate where the mouse clicked to the values in vector
            self.vertices.append((vector.getX(), vector.getY()))

    def drawDrop(self):
        pygame.draw.polygon(screen, 'black', self.vertices)

    def marble(self, other):
        for v in self.vertices:
            c = other.center
            r = other.r
            p = copy.deepcopy(self.vertices)
            m = Vector.mag(self.vertices, p)

    
def createDrop(x, y):
    drop = Drop(x, y, radius, circleDetail)
    for other in drops:
        other.marble(drops)
    drops.append(drop)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the left mouse button is clicked
            if event.button == 1:  # Left mouse button
                # Get the position of the mouse click
                mouseX, mouseY = pygame.mouse.get_pos()
                createDrop(mouseX, mouseY)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")


    for drop in drops:
        drop.drawDrop()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()