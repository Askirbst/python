import pygame # type: ignore
import math
import random

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
    
    # Maps a value from one range to another.
    
    return ((value-start1)/(stop1-start1))*(stop2-start2)+start2

class Drop:

    def __init__(self, x, y, r, s): # Initialize a Class object with parameters (x, y, r, s) x and y are coordinates, r is the radius, and s is smoothing of circle (number of sides of polygon)
        self.center = pygame.Vector2(x,y)
        self.r = r
        self.s = s

        # Randomize a color for each drop
        self.colorR = random.randint(0, 255)
        self.colorG = random.randint(0, 255)
        self.colorB = random.randint(0, 255)

        self.vertices = []

        for i in range(s):
            self.angle = mapValue(i, 0, s, 0, TWO_PI)
            self.vector = pygame.Vector2(float(math.cos(self.angle)), float(math.sin(self.angle)))
            self.vector.scale_to_length(self.r)
            self.vector.xy += self.center.xy
            self.vertices.append(self.vector)

    def drawDrop(self):

        pygame.draw.polygon(screen, (self.colorR, self.colorG, self.colorB), self.vertices)

    def marble(self, other):
        for v in self.vertices:
            c = other.center
            r = other.r
            p = pygame.Vector2.copy(v)
            p -= c
            root = math.sqrt(1 + (r * r) / (p.magnitude_squared()))
            p *= root
            p += c
            v.update(p)   

def createDrop(x, y):
    drop = Drop(x, y, radius, circleDetail)
    for other in drops:
        other.marble(drop)

    drops.append(drop)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the left mouse button is clicked
            if event.button == 1:  
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