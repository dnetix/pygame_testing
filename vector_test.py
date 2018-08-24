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
angle = 0

v = mylibpg.Vector(screen, (WIDTH / 2, HEIGHT / 2), WIDTH * 0.35, 90, mylibpg.COLOR_WHITE)
t = mylibpg.SimpleText(screen, str(angle), (10, 10), 20, mylibpg.COLOR_RED)

while not ended:

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == 273:
                angle += 5
            elif event.key == 274:
                angle -= 5

        if event.type == pygame.QUIT:
            ended = True

    screen.fill(mylibpg.COLOR_BLACK)

    v.set_angle(angle).visualize()
    t.set_text('Angle: ' + str(angle)).visualize()

    pygame.display.update()
    timer += clock.get_time()
    clock.tick(10)
    # pygame.display.flip()


pygame.quit()
quit()
