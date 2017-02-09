import pygame
from pygame.locals import*

pygame.init()
window_width = 500
window_height = 500
window_dim = (window_width,window_height)
window = pygame.display.set_mode(window_dim)
sprite_sheet = pygame.image.load("chess.jpg")
done = False


SPRT_RECT_X=0  
SPRT_RECT_Y=0
#This is where the sprite is found on the sprite_sheet

LEN_SPRT_X=50
LEN_SPRT_Y=50
#This is the length of the sprite

 #Locate the sprite you want
white=[0]*6
black=[0]*6

for i in range(0,6):
    sprite_sheet.set_clip(pygame.Rect(SPRT_RECT_X, SPRT_RECT_Y + 50*i, LEN_SPRT_X, LEN_SPRT_Y))
    white[i] = sprite_sheet.subsurface(sprite_sheet.get_clip())
    sprite_sheet.set_clip(pygame.Rect(SPRT_RECT_X + 50, SPRT_RECT_Y + 50*i, LEN_SPRT_X, LEN_SPRT_Y))
    black[i] = sprite_sheet.subsurface(sprite_sheet.get_clip()) #Extract the sprite you want

something = True

x = y = 0

while not done:
    if something:
        for i in range(0,6):
            something = False
            window.blit(white[i],(x,y))
            window.blit(black[i],(x,y+450))
            x += 50
            pygame.display.flip()

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

pygame.quit()
quit()
