import pygame
from pygame.locals import*

pygame.init()
window_width = 500
window_height = 500
window_dim = (window_width,window_height)
window = pygame.display.set_mode(window_dim)
image = pygame.image.load("chess.jpg")


while True:
    window.blit(image,(0,0))
    pygame.display.flip()
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

pygame.quit()
quit()
