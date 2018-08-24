import pygame
import mylibpg

pygame.init()

WIDTH = 500
HEIGHT = 500

worldImage = pygame.image.load('./assets/world_70.png')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Testing game")

clock = pygame.time.Clock()

ended = False

x = mylibpg.StaticAsset('./assets/world_70.png', (100, 100))
x.visualize()

while not ended:
    screen.fill(mylibpg.COLOR_BLACK)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x.placeMiddle(event.pos)
            # visualize(event.pos[0], event.pos[1])

        if event.type == pygame.QUIT:
            ended = True

    x.visualize()
    pygame.display.update()
    # pygame.display.flip()

    clock.tick(24)


pygame.quit()
quit()
