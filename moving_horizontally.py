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

w = mylibpg.StaticAsset(screen, './assets/world_70.png', (50, 200))
t = mylibpg.SimpleText(screen, 'Vel: 0', (WIDTH - 100, HEIGHT - 50), 20, mylibpg.COLOR_RED)
v = mylibpg.Vector(screen, (0, 0), 0, 90)

while not ended:

    elapsed = clock.get_time()

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == 273:
                speed += 1
            elif event.key == 274:
                speed -= 1

        if event.type == pygame.QUIT:
            ended = True

    screen.fill(mylibpg.COLOR_BLACK)

    # Calculate the next position
    if speed != 0:
        w.move(v.calculate(w.pos(), speed, 90))

    t.set_text('Vel: ' + str(speed)).visualize()
    w.visualize()

    pygame.display.update()
    timer += clock.get_time()
    clock.tick(10)
    # pygame.display.flip()


pygame.quit()
quit()
