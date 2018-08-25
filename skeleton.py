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

while not ended:

    elapsed = clock.get_time()

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == mylibpg.KEY_UP:
                pass

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.QUIT:
            ended = True

    screen.fill(mylibpg.COLOR_BLACK)

    pygame.display.update()
    timer += clock.get_time()
    clock.tick(24)

pygame.quit()
quit()
