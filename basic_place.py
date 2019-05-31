import pygame
import mylibpg
import math

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing game")

clock = pygame.time.Clock()
timer = 0

ended = False

# Elements
system = mylibpg.ReferenceSystem(screen, (WIDTH / 2, HEIGHT /2), (WIDTH, HEIGHT))

world = mylibpg.SystemParticle((0, 0), 5.972e24, mylibpg.EARTH_RADIUS, (0, 0), (0, 0), True).set_asset(mylibpg.StaticAsset(screen, './assets/world_70.png', (0, 0)))

orbitalv = (math.sqrt((mylibpg.G * mylibpg.EARTH_MASS) / ((200 / 35) * mylibpg.EARTH_RADIUS)))
orbitalv = (orbitalv / (mylibpg.EARTH_RADIUS / 35)) * 1.05

asteroid = mylibpg.SystemParticle((0, 200), 100, 20, (0, 0), (orbitalv, 0), False).set_asset(mylibpg.StaticAsset(screen, './assets/asteroid.png', (0, 0)).scale(0.5))

system.add_particle(world).add_particle(asteroid)

while not ended:

    elapsed = clock.get_time()

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == mylibpg.KEY_Q:
                ended = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.QUIT:
            ended = True

    screen.fill(mylibpg.COLOR_BLACK)

    system.tick(elapsed / 1000)
    system.visualize()

    pygame.display.update()
    timer += clock.get_time()
    clock.tick(60)

pygame.quit()
quit()
