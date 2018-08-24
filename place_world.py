import pygame
import mylibpg

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing game")

clock = pygame.time.Clock()

ended = False

w = mylibpg.StaticAsset(screen, './assets/world_70.png', (100, 100))

while not ended:
    screen.fill(mylibpg.COLOR_BLACK)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Allows to place the asset where the mouse clicks
            w.place_middle(event.pos)
            # visualize(event.pos[0], event.pos[1])

        if event.type == pygame.QUIT:
            ended = True

    w.visualize()
    pygame.display.update()

    clock.tick(24)


pygame.quit()
quit()
