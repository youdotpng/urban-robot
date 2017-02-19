import pygame

# Define some colors
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)


def square_print(pos):
        finish = False
        print("selected")
        while(not finish):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                    quit
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    print("This works")
                    print(pos[0],pos[1])
                    print(int(pawn_pos[0])//int(window_width/8.0), int(pos[1])//int(window_height/8.0))
                    print(pos[0] // (window_width/8.0) + pos[1] // (window_width/8.0) % 2 == 1)
                    if not((pygame.mouse.get_pos()[0] >= pawn_pos[0]) and
                           (pygame.mouse.get_pos()[0] <= pawn_pos[0]+square_width) and
                           (pygame.mouse.get_pos()[1] >= pawn_pos[1]) and
                           (pygame.mouse.get_pos()[1] <= pawn_pos[1]+square_height)):
                        
                        x = int(pygame.mouse.get_pos()[0]) // (window_width/8)
                        y = int(pygame.mouse.get_pos()[1]) // (window_height/8)
                        print(x, y)
                        print(x+(square_width - sprite_width)/2)
                        print(y+(square_height - sprite_height)/2)
                        # x2 = int(pos2[0] // (window_width/8))
                        # y2 = int(pos2[1] // (window_height/8))
                        window.blit(black[5],
                                   (int(x * (window_width/8) + (square_width - sprite_width)/2),
                                   int(y * (window_width/8) + (square_height - sprite_height)/2)))
                        if (int(pos[0]) // int(window_width/8.0) + int(pos[1]) // int(window_width/8.0)) % 2 == 1:
                            print("White")
                            pygame.draw.rect(window, WHITE,
                                             ((int(pos[0]) // int(window_width/8.0) * (window_width/8.0)),
                                              (int(pos[1]) // int(window_width/8.0) * (window_height/8.0)),
                                              window_width/8.0,
                                              window_height/8.0)
                                             )
                        else:
                            print("Red")
                            pygame.draw.rect(window, BLACK,
                                             ((int(pos[0]) // int(window_width/8.0) * (window_width/8.0)),
                                              (int(pos[1]) // int(window_width/8.0) * (window_height/8.0)),
                                              window_width/8.0,
                                              window_height/8.0)
                                             )
                        # print (x)
                        # print (y)
                        pygame.display.flip()
                        return ((x * (window_width/8), y * (window_width/8)))


# Make a window
pygame.init()
window_width = 512
window_height = 512
window_dim = (window_width, window_height)
window = pygame.display.set_mode(window_dim)
window.fill(BLUE)

square_width = window_width/8
square_height = window_height/8
sprite_width = 50
sprite_height = 50


# for testing
pawn_pos = (5*square_width, 0)
# Board logic x+y%2 == 0 -> black square, x=y%2 ==1  -> white square

for i in range(0, 8):
        for j in range(0, 8):
            # if j%2 ==i%2:
            if (i+j) % 2 == 0:
                pygame.draw.rect(window, BLACK,
                                 (i*(window_width/8),
                                  j*(window_height/8),
                                  window_width/8,
                                  window_height/8)
                                 )
            else:
                pygame.draw.rect(window, WHITE,
                                 (i*(window_width/8),
                                  j*(window_height/8),
                                  window_width/8,
                                  window_height/8)
                                 )

# -------Piece Information
sprite_sheet = pygame.image.load("Chees_piece.png")

SPRT_RECT_X = 0
SPRT_RECT_Y = 0
# This is where the sprite is found on the sprite_sheet

LEN_SPRT_X = 50
LEN_SPRT_Y = 50
# This is the length of the sprite

# Locate the sprite you want
white = [0]*6
black = [0]*6

# --Set Sprites for white and black teams
for i in range(0, 6):
    sprite_sheet.set_clip(pygame.Rect(SPRT_RECT_X,
                                      SPRT_RECT_Y + sprite_height*i,
                                      LEN_SPRT_X,
                                      LEN_SPRT_Y))
    white[i] = sprite_sheet.subsurface(sprite_sheet.get_clip())
    sprite_sheet.set_clip(pygame.Rect(SPRT_RECT_X + sprite_width,
                                      SPRT_RECT_Y + sprite_width*i,
                                      LEN_SPRT_X,
                                      LEN_SPRT_Y))
    black[i] = sprite_sheet.subsurface(sprite_sheet.get_clip())

# --Variables for piece setting conditions
set_pieces = True
x = y = 0

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the window updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    if set_pieces:
        for i in range(0, 6):
            # the x location of the sprite is given by:
            # (x_square + (sq_width - sprite_size)/2)
            set_pieces = False
            window.blit(white[i],
                        (x+(square_width - sprite_width)/2,
                        y+(square_height - sprite_height)/2+7*square_height))
            window.blit(black[i],
                        (x+(square_width - sprite_width)/2,
                        y+(square_height - sprite_height)/2))
            x += square_width
            pygame.display.flip()
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
# --- Game logic should go here
# --- Get mouse movement
# d_mouse_pos = pygame.mouse.get_pos()
# print(d_mouse_pos)
# --- Drawing code should go here

# First, clear the window to white. Don't put other drawing commands
# above this, or they will be erased with this command.
    # window.fill(BLUE)
# for i in range(0,8):

#       for j in range(0,8):
#            if j%2 ==i%2:
#               pygame.draw.rect(window,BLACK,(i*(window_width/8),
#                       #j*(window_height/8),window_width/8,window_height/8))
#           else:
#                pygame.draw.rect(window,WHITE,(i*(window_width/8),
#                        j*(window_height/8),window_width/8,window_height/8))

        # --- Go ahead and update the window with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)
        # for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
            select_mouse_pos = pygame.mouse.get_pos()
            print(select_mouse_pos[0])
            if ((select_mouse_pos[0] >= pawn_pos[0]) and
                    (select_mouse_pos[0] <= pawn_pos[0]+square_width) and
                    (select_mouse_pos[1] >= pawn_pos[1]) and
                    (select_mouse_pos[1] <= pawn_pos[1]+square_height)):
                        pawn_pos = square_print(select_mouse_pos)
            continue
pygame.quit()
quit()
