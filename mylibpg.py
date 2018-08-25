import pygame
import math

# PyGame reusable modules

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 116, 217)
COLOR_NAVY = (0, 31, 63)
COLOR_RED = (255, 65, 54)

KEY_UP = 273
KEY_DOWN = 274
KEY_RIGHT = 275
KEY_LEFT = 276
KEY_A = 97
KEY_Q = 113


class Positionable:
    x = 0
    y = 0

    def move(self, x_y):
        self.x, self.y = x_y
        return self

    def position(self):
        return self.x, self.y


class Presentable(Positionable):
    screen = None

    def set_screen(self, screen):
        self.screen = screen
        return self

    def visualize(self):
        pass


class Locator:
    source = None
    destination = None

    def __init__(self, source: Positionable, destination: Positionable):
        self.source = source
        self.destination = destination

    def distance(self):
        sx, sy = self.source.position()
        dx, dy = self.destination.position()
        return math.sqrt((dx - sx) ** 2 + (dy - sy) ** 2)

    def angle(self):
        sx, sy = self.source.position()
        dx, dy = self.destination.position()

        co = dy - sy
        ca = dx - sx

        if ca == 0 or co == 0:
            # Its a cardinal point
            if ca == 0:
                return 90 if co > 0 else 270
            if co == 0:
                return 180 if ca > 0 else 0

        if co < 0:
            if ca > 0:
                zone = 1
            else:
                zone = 4
        else:
            if ca > 0:
                zone = 2
            else:
                zone = 3

        if zone == 1:
            co = abs(co)
            return 90 - math.degrees(math.atan2(co, ca))
        elif zone == 2:
            return 90 + math.degrees(math.atan2(co, ca))
        elif zone == 3:
            ca = abs(ca)
            return 270 - math.degrees(math.atan2(co, ca))
        elif zone == 4:
            co = abs(co)
            ca = abs(ca)
            return 270 + math.degrees(math.atan2(co, ca))


class SimpleText(Presentable):
    text = ''
    size = 20
    color = COLOR_BLACK
    fontFace = 'freesansbold.ttf'
    font = None

    surface = None

    def __init__(self, screen, text, x_y, size=20, color=COLOR_BLACK):
        self.set_screen(screen)
        self.move(x_y)
        self.text = text
        self.size = size
        self.color = color
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


class StaticAsset(Presentable):
    width = 0
    height = 0
    source = None

    def __init__(self, screen, path, x_y=(0, 0)):
        source = pygame.image.load(path)
        self.set_screen(screen)
        self.source = source
        self.width, self.height = source.get_rect().size
        self.move(x_y)

    def scale(self, times):
        self.width = self.width * times
        self.height = self.height * times
        self.source = pygame.transform.scale(self.source, (int(self.width), int(self.height)))
        return self

    def visualize(self):
        x = self.x - (self.width / 2)
        y = self.y - (self.height / 2)
        self.screen.blit(self.source, (x, y))
        return self


class Vector(Presentable):
    res_x = 0
    res_y = 0

    length = 0
    angle = 0
    color = COLOR_RED
    screen = None

    def __init__(self, screen, x_y, length, angle, color=COLOR_NAVY):
        self.move(x_y)
        self.set_screen(screen)
        self.length = length
        self.angle = angle
        self.color = color
        self.update()

    def set_angle(self, angle):
        self.angle = angle
        self.update()
        return self

    def set_length(self, length):
        self.length = length
        self.update()
        return self

    def des(self):
        return self.res_x, self.res_y

    def update(self):
        self.res_x = self.x + (round(math.sin(math.radians(self.angle)), 6) * self.length)
        self.res_y = self.y + (round(math.cos(math.radians(self.angle)), 6) * self.length) * -1
        return self

    def calculate(self, x_y, length, angle):
        self.move(x_y)
        self.length = length
        self.set_angle(angle)
        return self.des()

    def visualize(self):
        if self.length > 0:
            pygame.draw.circle(self.screen, self.color, (int(self.res_x), int(self.res_y)), 4)
            pygame.draw.line(self.screen, self.color, self.position(), self.des(), 1)
