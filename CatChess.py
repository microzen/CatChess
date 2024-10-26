# https://www.pygame.org/docs/

import pygame
import chess_board

pygame.init()
pygame.display.set_mode((800, 800))

board = chess_board.Board(pygame)

clock = pygame.time.Clock()
running = True
FPS = 60

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    x, y = pygame.mouse.get_pos()
    board.move_in(int(y/100),int(x/100))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()
