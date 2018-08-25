import pygame
import math
import numpy as np

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

G = 6.674e-11
EARTH_MASS = 5.972e24
EARTH_RADIUS = 6.731e6

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
        return self.calculate_angle(self.source.position(), self.destination.position())

    @staticmethod
    def calculate_angle(sx_sy, dx_dy):
        sx, sy = sx_sy
        dx, dy = dx_dy

        co = dy - sy
        ca = dx - sx

        if ca == 0 or co == 0:
            # Its a cardinal point
            if ca == 0:
                return 180 if co > 0 else 0
            if co == 0:
                return 270 if ca > 0 else 90

        if co < 0:
            zone = 1 if ca > 0 else 4
        else:
            zone = 2 if ca > 0 else 3

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


class SystemParticle(Positionable):
    mass = 1
    radius = 1
    acceleration = (0, 0)
    velocity = (0, 0)
    static = False
    asset = None

    def __init__(self, x_y, mass, radius, a, v, static = False):
        self.move(x_y)
        self.set_radius(radius)
        self.set_mass(mass)
        self.set_acceleration(a)
        self.set_velocity(v)
        self.static = static

    def set_mass(self, mass):
        self.mass = mass
        return self

    def set_acceleration(self, a):
        self.acceleration = a
        return self

    def set_velocity(self, v):
        self.velocity = v
        return self

    def set_radius(self, radius):
        self.radius = radius
        return self

    def set_asset(self, asset):
        self.asset = asset
        return self

    def play(self, elapsed):
        if elapsed != 0:
            # 2000X Faster
            elapsed *= 2000
            self.velocity = np.add(self.velocity, np.multiply(self.acceleration, elapsed))
            self.x += self.velocity[0] * elapsed
            self.y += self.velocity[1] * elapsed

    def visualize(self, screen):
        if self.asset is None:
            pygame.draw.circle(screen, COLOR_RED, self.position(), 2)
        else:
            self.asset.move(self.position())
            self.asset.visualize()


class ReferenceSystem(Presentable):
    size_x = 800
    size_y = 800

    # How many meters represents a pixel
    scale = EARTH_RADIUS / 35
    time = 0

    display_line = True

    particles = []

    def __init__(self, screen, x_y, sizes):
        self.set_screen(screen)
        self.move(x_y)
        self.size_x, self.size_y = sizes

    def set_scale(self, scale):
        self.scale = scale
        return self

    def add_particle(self, particle):
        pos = self.relative_position(particle.position())
        particle.move(pos)
        self.particles.append(particle)
        return self

    def relative_position(self, x_y):
        return self.x + x_y[0], self.y - x_y[1]

    def tick(self, elapsed):
        p1 = self.particles[0]
        p2 = self.particles[1]

        x = Locator(p2, p1)
        r = (x.distance() * self.scale)

        # I have the magnitude of the acceleration
        a = (G * p1.mass) / (r ** 2)
        # and the angle
        angle = x.angle()

        acceleration = (a * round(math.sin(math.radians(angle)), 2), a * round(math.cos(math.radians(angle)), 2) * -1)
        acceleration = np.multiply(acceleration, 1 / self.scale)
        p2.set_acceleration(acceleration)
        p2.play(elapsed)

    def visualize(self):
        if self.display_line:
            pygame.draw.line(self.screen, COLOR_WHITE, (0, self.y), (self.size_x, self.y), 1)
            pygame.draw.line(self.screen, COLOR_WHITE, (self.x, 0), (self.x, self.size_y), 1)

        for particle in self.particles:
            # Particle visualization
            particle.visualize(self.screen)
