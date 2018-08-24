import pygame
import mylibpg
import math

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Testing game")

clock = pygame.time.Clock()
timer = 0

ended = False

t = mylibpg.SimpleText(screen, 'Testing', (30, 30), 20, mylibpg.COLOR_RED)
t.visualize()

while not ended:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ended = True

    screen.fill(mylibpg.COLOR_BLACK)

    # t.set_text('Time elapsed: ' + str(math.floor(timer / 1000))).visualize()
    t.set_text('Time elapsed: ' + str(timer / 1000)).visualize()

    pygame.display.update()
    timer += clock.get_time()
    clock.tick(10)

pygame.quit()
quit()
