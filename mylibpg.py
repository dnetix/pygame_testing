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

    def __init__(self, screen, text, x_y, size=20, color=COLOR_BLACK):
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
        self.screen = screen
        self.place_middle(x_y)
        self.source = source
        self.width, self.height = source.get_rect().size

    def place_middle(self, x_y):
        x, y = x_y
        self.x = x - (self.width / 2)
        self.y = y - (self.height / 2)

    def pos(self):
        return self.x, self.y

    def scale(self, times):
        self.width = self.width * times
        self.height = self.height * times
        self.source = pygame.transform.scale(self.source, (self.width, self.height))

    def move(self, x_y):
        self.x, self.y = x_y

    def visualize(self):
        self.screen.blit(self.source, (self.x, self.y))


class Vector:
    x = 0
    y = 0

    res_x = 0
    res_y = 0

    length = 0
    angle = 0
    color = COLOR_RED
    screen = None

    def __init__(self, screen, x_y, length, angle, color=COLOR_NAVY):
        self.x, self.y = x_y
        self.length = length
        self.angle = angle
        self.screen = screen
        self.color = color
        self.update()

    def set_angle(self, angle):
        self.angle = angle
        self.update()
        return self

    def pos(self):
        return self.x, self.y

    def des(self):
        return self.res_x, self.res_y

    def update(self):
        self.res_x = self.x + (round(math.sin(math.radians(self.angle)), 6) * self.length)
        self.res_y = self.y + (round(math.cos(math.radians(self.angle)), 6) * self.length) * -1
        return self

    def calculate(self, x_y, length, angle):
        self.x, self.y = x_y
        self.length = length
        self.angle = angle
        self.update()
        return self.des()

    def visualize(self):
        pygame.draw.circle(self.screen, self.color, (int(self.res_x), int(self.res_y)), 4)
        pygame.draw.line(self.screen, self.color, self.pos(), self.des(), 1)
