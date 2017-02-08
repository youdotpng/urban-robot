import pygame

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

def square_print(pos,pos2):
        x = int(pos[0] // (window_width/8))
        y = int(pos[1] // (window_height/8))
        x2 = int(pos2[0] // (window_width/8))
        y2 = int(pos2[1] // (window_height/8))
        pygame.draw.rect(window,RED,(x*(window_width/8.0),y*(window_height/8.0),window_width/8.0,window_height/8.0))
        #print (x)
        #print (y)
        return (pos)
        



#Make a window
pygame.init()
window_width = 500
window_height = 500
window_dim = (window_width,window_height)
window = pygame.display.set_mode(window_dim)
window.fill(BLUE)
for i in range(0,8):
        for j in range(0,8):
            if j%2 ==i%2:
                pygame.draw.rect(window,BLACK,(i*(window_width/8),j*(window_height/8),window_width/8,window_height/8))
            else:
                pygame.draw.rect(window,WHITE,(i*(window_width/8),j*(window_height/8),window_width/8,window_height/8))



# Loop until the user clicks the close button.
done = False

# Used to manage how fast the window updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here
		#--- Get mouse movement
    #d_mouse_pos = pygame.mouse.get_pos()
    #print(d_mouse_pos)
    # --- Drawing code should go here

    # First, clear the window to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
   ## window.fill(BLUE)

##    for i in range(0,8):
##
##        for j in range(0,8):
##            if j%2 ==i%2:
##                pygame.draw.rect(window,BLACK,(i*(window_width/8),j*(window_height/8),window_width/8,window_height/8))
##            else:
##                pygame.draw.rect(window,WHITE,(i*(window_width/8),j*(window_height/8),window_width/8,window_height/8))

    # --- Go ahead and update the window with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

   
	
    #for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("User asked to quit.")
    elif event.type == pygame.KEYDOWN:
      print("User pressed a key.")
    elif event.type == pygame.KEYUP:
      print("User let go of a key.")
    elif event.type == pygame.MOUSEBUTTONDOWN:
      print("User pressed a mouse button")
      select_mouse_pos = pygame.mouse.get_pos()
      square_print(select_mouse_pos,previous_mouse_pos)
pygame.quit()
quit()
