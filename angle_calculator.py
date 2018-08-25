import pygame
import mylibpg

pygame.init()

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing game")

clock = pygame.time.Clock()
timer = 0

ended = False
speed = 0
angle = 90

ts = mylibpg.SimpleText(screen, 'Vel: 0', (WIDTH - 120, HEIGHT - 90), 20, mylibpg.COLOR_RED)
ta = mylibpg.SimpleText(screen, 'Angle: 90', (WIDTH - 120, HEIGHT - 50), 20, mylibpg.COLOR_RED)

w = mylibpg.StaticAsset(screen, './assets/world_70.png', (WIDTH / 2, HEIGHT / 2))
asteroid = mylibpg.StaticAsset(screen, './assets/asteroid.png', (WIDTH / 2, HEIGHT * 0.1))
v = mylibpg.Vector(screen, (0, 0), 0, 90)

world_asteroid = mylibpg.Locator(w, asteroid)

while not ended:

    elapsed = clock.get_time()

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == mylibpg.KEY_UP:
                speed += 1
            elif event.key == mylibpg.KEY_DOWN:
                speed -= 1
            elif event.key == mylibpg.KEY_Q:
                ended = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Allows to place the asset where the mouse clicks
            angle = mylibpg.Locator.calculate_angle(asteroid.position(), event.pos)
            # visualize(event.pos[0], event.pos[1])

        if event.type == pygame.QUIT:
            ended = True

    # Calculate the next position
    if speed != 0:
        asteroid.move(v.calculate(asteroid.position(), speed * (elapsed / 1000), angle))

    screen.fill(mylibpg.COLOR_BLACK)

    w.visualize()
    asteroid.visualize()

    ts.set_text('Vel: ' + str(speed) + ' px/s').visualize()
    ta.set_text('Angle: ' + str(angle) + 'º').visualize()
    print(world_asteroid.distance(), world_asteroid.angle())

    pygame.display.update()
    timer += clock.get_time()
    clock.tick(24)
    # pygame.display.flip()


pygame.quit()
quit()
