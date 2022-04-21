#Import libraries
import pygame
import random

board = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]

window = pygame.display.set_mode((1280, 720))


def main(): 
    run = True 
    while run: 
        color = (255,0,0)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        xmove = 0
        ymove = 0
        for y in board:
            for x in y:
                pygame.draw.rect(window, color, pygame.Rect(0 + xmove, 0 + ymove, 60, 60))
                xmove += 120
            ymove += 120
            xmove = 0
            



        pygame.display.update()
        
    pygame.quit()
main()