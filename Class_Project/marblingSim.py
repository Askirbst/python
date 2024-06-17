import pygame
import math
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

TWO_PI = math.pi * 2
MAX_DROPS = 250

drops = []
circleDetail = 300
radius = 50

drag = False
left_clicked = False
right_clicked = False

color = ["black", "green", "purple", "yellow", "red", "violet", "orange", "indigo"]

angle_increment = 2 * math.pi / circleDetail

def mapValue(value, start1, stop1, start2, stop2):
    
    # Maps a value from one range to another.
    
    return ((value-start1)/(stop1-start1))*(stop2-start2)+start2

class Drop:

    def __init__(self, x, y, r, s, pick): # Initialize a Class object with parameters (x, y, r, s) x and y are coordinates, r is the radius, and s is smoothing of circle (number of sides of polygon)
        self.center = pygame.Vector2(x,y)
        self.r = r
        self.s = s

        self.dropColor = color[pick]


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
        
        pygame.draw.polygon(screen, self.dropColor, self.vertices)

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

    def tine(self, m, x, y, z, c):
        u = 1 / math.pow(2, 1 / c)
        b = pygame.math.Vector2(x, y)
        for v in self.vertices:
            pb = v - b
            n = pygame.Vector2.copy(m).rotate(90)
            d = abs(pb.dot(n))
            mag = z * math.pow(u, d)
            v += pygame.Vector2.copy(m) * mag

def tineLine(m, x, y, z, c):
    for drop in drops:
        drop.tine(m, x, y, z, c)

def createDrop(x, y, pick):
    drop = Drop(x, y, radius, circleDetail, pick)
    for other in drops:
        other.marble(drop)
    if len(drops) >= MAX_DROPS:
        drops.append(drop)
        drops.pop(0)
    else:    
        drops.append(drop)

def direction_unit_vector(coord1, coord2):
  x1, y1 = coord1
  x2, y2 = coord2
  dx = x2 - x1
  dy = y2 - y1
  magnitude = (dx**2 + dy**2)**0.5
  if magnitude == 0:  # Handle coincident points (avoid division by zero)
    return (0, 0)
  else:
    return (dx / magnitude, dy / magnitude)

start_posXY = []
end_posXY = []

buttonWidth = 100
buttonHeight = 50
buttonOffset = 10
pick = 2

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close the window
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the left mouse button is clicked
            if event.button == 1: 
                mouseX, mouseY = pygame.mouse.get_pos()
                if buttonWidth + buttonOffset >= mouseX >= buttonOffset and buttonHeight + buttonOffset >= mouseY >= buttonOffset:
                    if pick >= 7:
                        pick = 0
                    else:
                        pick += 1
                else:
                    left_clicked = True  
            if event.button == 3:
                start_posXY = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                left_clicked = False
            if event.button == 3:
                end_posXY = pygame.mouse.get_pos()

                directX, directY = direction_unit_vector(start_posXY, end_posXY)
                v = pygame.math.Vector2(directX, directY)
                
                tineLine(v, start_posXY[0], start_posXY[1], 50, 20)

        if event.type == pygame.QUIT:
            running = False

    if left_clicked:
        mouseX, mouseY = pygame.mouse.get_pos()
        createDrop(mouseX, mouseY, pick)  
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # draws all drops in the drops list
    for drop in drops:
        drop.drawDrop()

    # draws a button to change color of drops
    pygame.draw.rect(screen, color[pick], pygame.Rect(buttonOffset, buttonOffset, buttonWidth, buttonHeight))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(30) / 1000

pygame.quit()