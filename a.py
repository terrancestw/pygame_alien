import pygame
import sys

white = (255,255,255)
black = (0,0,0)


def run():
    pygame.init()

    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption('a game')


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(white)

        pygame.display.flip()



run()
