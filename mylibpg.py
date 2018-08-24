import pygame
import math

# PyGame reusable modules

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 116, 217)
COLOR_NAVY = (0, 31, 63)
COLOR_RED = (255, 65, 54)

class SimpleText:
    x = 0
    y = 0
    text = ''
    size = 20
    color = COLOR_BLACK
    fontFace = 'freesansbold.ttf'
    font = None

    surface = None
    screen = None

    def __init__(self, screen, text, x_y, size = 20, color = COLOR_BLACK):
        self.x, self.y = x_y
        self.text = text
        self.size = size
        self.color = color
        self.screen = screen
        self.update()

    def update(self):
        self.font = pygame.font.Font(self.fontFace, self.size)
        self.surface = self.font.render(self.text, True, self.color)
        return self

    def set_text(self, text):
        self.text = text
        self.update()
        return self

    def set_font(self, font):
        self.fontFace = font
        self.update()
        return self

    def visualize(self):
        self.screen.blit(self.surface, (self.x, self.y))


class StaticAsset:
    x = 0
    y = 0
    width = 0
    height = 0
    source = None
    screen = None

    def __init__(self, screen, path, x_y=(0, 0)):
        source = pygame.image.load(path)
        self.screen = screen;
        self.placeMiddle(x_y)
        self.source = source
        self.width, self.height = source.get_rect().size

    def placeMiddle(self, x_y):
        x, y = x_y
        self.x = x - (self.width / 2)
        self.y = y - (self.height / 2)

    def scale(self, times):
        self.width = self.width * times
        self.height = self.height * times

        self.source = pygame.transform.scale(self.source, (self.width, self.height))

    def visualize(self):
        self.screen.blit(self.source, (self.x, self.y))

class Vector:
    x = 0
    y = 0
    length = 0
    angle = 0
    color = COLOR_RED
    screen = None

    def __init__(self, screen, x_y, length, angle, color = COLOR_NAVY):
        self.x, self.y = x_y
        self.length = length
        self.angle = angle
        self.screen = screen
        self.color = color

    def set_angle(self, angle):
        self.angle = angle
        return self

    def visualize(self):
        x = self.x + (math.sin(math.radians(self.angle)) * self.length)
        y = self.y + (math.cos(math.radians(self.angle)) * self.length) * -1
        pygame.draw.circle(self.screen, self.color, (int(x), int(y)), 5)
        pygame.draw.line(self.screen, self.color, (self.x, self.y), (x, y), 2)
