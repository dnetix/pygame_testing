import pygame
import mylibpg

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing game")

clock = pygame.time.Clock()
timer = 0

ended = False
speed = 0
angle = 90

w = mylibpg.StaticAsset(screen, './assets/world_70.png', (50, 200))
ts = mylibpg.SimpleText(screen, 'Vel: 0', (WIDTH - 120, HEIGHT - 90), 20, mylibpg.COLOR_RED)
ta = mylibpg.SimpleText(screen, 'Angle: 90', (WIDTH - 120, HEIGHT - 50), 20, mylibpg.COLOR_RED)
v = mylibpg.Vector(screen, (0, 0), 0, 90)

while not ended:

    elapsed = clock.get_time()

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == mylibpg.KEY_UP:
                speed += 1
            elif event.key == mylibpg.KEY_DOWN:
                speed -= 1
            elif event.key == mylibpg.KEY_RIGHT:
                angle += 5
            elif event.key == mylibpg.KEY_LEFT:
                angle -= 5

        if event.type == pygame.QUIT:
            ended = True

    screen.fill(mylibpg.COLOR_BLACK)

    # Calculate the next position
    if speed != 0:
        w.move(v.calculate(w.position(), speed * (elapsed / 1000), angle))

    ts.set_text('Vel: ' + str(speed) + ' px/s').visualize()
    ta.set_text('Angle: ' + str(angle) + 'º').visualize()
    w.visualize()

    v.set_length(speed)
    v.visualize()

    pygame.display.update()
    timer += clock.get_time()
    clock.tick(24)
    # pygame.display.flip()


pygame.quit()
quit()
