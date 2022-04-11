#Import libraries
import pygame
import random



def main(): 
    run = True 
    while run: 
        Win = pygame.display.set_mode((400, 800))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        pygame.quit()

main()