import pygame

BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 512
SQUARE_WIDTH = WINDOW_WIDTH/8
SQUARE_HEIGHT = WINDOW_HEIGHT/8

class Piece:
    def __init__(self, name = 'pawn_0_U', str_loc = 'A1', mov_count = 0):
        self.name = name
        self.loc = str_loc
        self.mov_count = mov_count
        self.sprite_width = 50
        self.sprite_height = 50
        self.sprites = self.__sprite_set__()
        self.pixel_loc_centered = None
        self.get_pixel_loc(SQUARE_WIDTH, SQUARE_HEIGHT)

    def __sprite_set__(self):
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
                                              SPRT_RECT_Y + self.sprite_height*i,
                                              LEN_SPRT_X,
                                              LEN_SPRT_Y))
            white[i] = sprite_sheet.subsurface(sprite_sheet.get_clip())
            sprite_sheet.set_clip(pygame.Rect(SPRT_RECT_X + self.sprite_width,
                                              SPRT_RECT_Y + self.sprite_width*i,
                                              LEN_SPRT_X,
                                              LEN_SPRT_Y))
            black[i] = sprite_sheet.subsurface(sprite_sheet.get_clip())
        return (white, black)

    def piece_move(self, window, B):
            finish = False
            while(not finish):
                #--- Wait for user to select a new square
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:  # If user clicked close
                        #done = True  # Flag that we are done so we exit this loop
                        pygame.quit()
                        quit
                    if event.type == pygame.MOUSEBUTTONDOWN: 
#                        print(pos[0],pos[1])
#                        print(int(self.pixel_loc_centered[0])//int(WINDOW_WIDTH/8.0), int(pos[1])//int(WINDOW_HEIGHT/8.0))
                        pos = pygame.mouse.get_pos()
                        print(pos[0] // (WINDOW_WIDTH/8.0) + pos[1] // (WINDOW_WIDTH/8.0) % 2 == 1)
                        if not((pygame.mouse.get_pos()[0] >= self.pixel_loc_centered[0]) and
                               (pygame.mouse.get_pos()[0] <= self.pixel_loc_centered[0]+SQUARE_WIDTH) and
                               (pygame.mouse.get_pos()[1] >= self.pixel_loc_centered[1]) and
                               (pygame.mouse.get_pos()[1] <= self.pixel_loc_centered[1]+SQUARE_HEIGHT)):
                            
                            x = int(pygame.mouse.get_pos()[0]) // (WINDOW_WIDTH/8)
                            y = int(pygame.mouse.get_pos()[1]) // (WINDOW_HEIGHT/8)
#                            print(x, y)
#                            print(x+(SQUARE_WIDTH - self.sprite_width)/2)
#                            print(y+(SQUARE_HEIGHT - self.sprite_height)/2)
                            # x2 = int(pos2[0] // (WINDOW_WIDTH/8))
                            # y2 = int(pos2[1] // (WINDOW_HEIGHT/8))
                            window.blit(self.sprite,
                                       (int(x * (WINDOW_WIDTH/8) + (SQUARE_WIDTH - self.sprite_width)/2),
                                       int(y * (WINDOW_WIDTH/8) + (SQUARE_HEIGHT - self.sprite_height)/2)))
                            if (int(pos[0]) // int(WINDOW_WIDTH/8.0) + int(pos[1]) // int(WINDOW_WIDTH/8.0)) % 2 == 0:
                                print("White")
                                pygame.draw.rect(window, WHITE,
                                                 ((int(self.get_pixel_loc(SQUARE_WIDTH, SQUARE_HEIGHT)[0]) // int(WINDOW_WIDTH/8.0) * (WINDOW_WIDTH/8.0)),
                                                  (int(self.get_pixel_loc(SQUARE_WIDTH, SQUARE_HEIGHT)[1]) // int(WINDOW_WIDTH/8.0) * (WINDOW_HEIGHT/8.0)),
                                                  WINDOW_WIDTH/8.0,
                                                  WINDOW_HEIGHT/8.0)
                                                 )
                            else:
                                print("Black")
                                pygame.draw.rect(window, BLACK,
                                                 ((int(self.get_pixel_loc(SQUARE_WIDTH, SQUARE_HEIGHT)[0]) // int(WINDOW_WIDTH/8.0) * (WINDOW_WIDTH/8.0)),
                                                  (int(self.get_pixel_loc(SQUARE_WIDTH, SQUARE_HEIGHT)[1]) // int(WINDOW_WIDTH/8.0) * (WINDOW_HEIGHT/8.0)),
                                                  WINDOW_WIDTH/8.0,
                                                  WINDOW_HEIGHT/8.0)
                                                 )
                            # print (x)
                            # print (y)
                            pygame.display.flip()
                            select_row_B = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'][pos[0]
                             // int(WINDOW_WIDTH/8)]
                            select_col_B = 8 -  pos[1] // int(WINDOW_HEIGHT/8)
                            print(self.get_loc())
                            B.board[self.get_loc()]=0
                            self.set_loc(select_row_B+str(select_col_B))
                            B.board[self.get_loc()]=1
                            print(self.get_loc())
                            finish = True
                            #return ((x * (WINDOW_WIDTH/8), y * (WINDOW_WIDTH/8)))
                            

    def __str__(self):
        return self.name
    def set_mov_count(self,mov_count):
        self.mov_count = mov_count

    def get_mov_count(self):
        return self.mov_count

    def set_loc(self,str_loc):
        self.loc = str_loc
#----- This returns the pieces location-----
    def get_loc(self):
        return self.loc
    
    def get_pixel_loc(self, SQUARE_WIDTH, SQUARE_HEIGHT):
        x_loc = ord(self.loc[0]) - 65
        # This is a quick fix, but it works
        y_loc = abs(int(self.loc[1]) - 8)
        self.pixel_loc_centered = (x_loc * SQUARE_WIDTH + (SQUARE_WIDTH - self.sprite_width)/2,
               y_loc * SQUARE_HEIGHT + (SQUARE_HEIGHT - self.sprite_height)/2)
        return self.pixel_loc_centered

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Pawn(Piece):
    def __init__(self, name = 'pawn_0_U', str_loc = 'D5', mov_count = 0):
        super(Pawn, self).__init__(name, str_loc, mov_count)
        self.sprite = (self.sprites[0][5], self.sprites[1][5])
        self.sprites = None
        
    def move(self, candidate):
#----- Two space movement for initial pawn location-0----
        if(self.mov_count == 0 and candidate[1] == self.loc[1] and candidate[2] == int(self.loc[2])+2):
            self.set_loc(candidate)
            return

#-----basic forward movement only-----
        if(candidate[1] == self.loc[1] and candidate[2] == int(self.loc[2])+1):
            self.set_loc(candidate)
            return
        
        print("invalid location")
        

class Rook(Piece):  
    def __init__(self, name = 'pawn_0_U', str_loc = 'D5', mov_count = 0):
        super(Rook, self).__init__(name, str_loc, mov_count)
        self.sprite = (self.sprites[0][4], self.sprites[1][4])
        self.sprites = None    

class Knight(Piece):    
    def __init__(self, name = 'pawn_0_U', str_loc = 'D5', mov_count = 0):
        super(Knight, self).__init__(name, str_loc, mov_count)
        self.sprite = (self.sprites[0][3], self.sprites[1][3])
        self.sprites = None
class Bishop(Piece):    
    def __init__(self, name = 'pawn_0_U', str_loc = 'D5', mov_count = 0):
        super(Bishop, self).__init__(name, str_loc, mov_count)
        self.sprite = (self.sprites[0][2], self.sprites[1][2])
        self.sprites = None 

class Queen(Piece):
    def __init__(self, name = 'pawn_0_U', str_loc = 'D5', mov_count = 0):
        super(Queen, self).__init__(name, str_loc, mov_count)
        self.sprite = (self.sprites[0][1], self.sprites[1][1])
        self.sprites = None  

class King(Piece):
    def __init__(self, name = 'pawn_0_U', str_loc = 'D5', mov_count = 0):
        super(King, self).__init__(name, str_loc, mov_count)
        self.sprite = (self.sprites[0][0], self.sprites[1][0])
        self.sprites = None
class Board:
    def __init__(self):

        # Initialize empty board
# ------ This tracks where the pieces are -----
        self.board = dict()
        for j in ['A','B','C','D','E','F','G','H']:
            for i in range(1,9,1):
                self.board[j+str(i)] = 0

        #Initialize two rows of pieces on either end of the board
        for j in ['A','B','C','D','E','F','G','H']:
            for i in range(1,9,6):
                self.board[j+str(i)] = 1
                self.board[j+str(i+1)] = 1
# --------Literally checks for pieces-----
    def piece_check(self, row, col):
        if self.board[row+str(col)] == 1:
            return(True)
        if self.board[row+str(col)] == 0:
            return(False)
        else:
            raise
        
def Boardset(window):
    B = Board()

    Black = [0]*16
    White = [0]*16
  
    Black[0] = Rook("rook_1_B","H8") 
    White[0] = Rook("rook_1_W","H1")
    Black[1] = Rook("rook_2_B","A8") 
    White[1] = Rook("rook_2_W","A1")
    Black[2] = Knight("knight_1_B","B8") 
    White[2] = Knight("knight_1_W","B1")
    Black[3] = Knight("knight_2_B","G8") 
    White[3] = Knight("knight_2_W","G1")
    Black[4] = Bishop("bishop_1_B","C8") 
    White[4] = Bishop("bishop_1_W","C1")
    Black[5] = Bishop("bishop_2_B","F8") 
    White[5] = Bishop("bishop_2_W","F1")
    Black[6] = King("king_1_B","E8")
    White[6] = King("king_1_W","E1")
    Black[7] = Queen("queen_1_B","D8")
    White[7] = Queen("queen_1_W","D1")

    for i in range(1,9,1):
        Black[i+7] = Pawn("pawn_"+str(i)+"_B",chr(64+i)+str(7))
        White[i+7] = Pawn("pawn_"+str(i)+"_W",chr(64+i)+str(2))
               
    for i in range(0,16,1):
        black_loc = Black[i].get_loc()
        white_loc = White[i].get_loc()
        Black[i].sprite = Black[i].sprite[1]
        White[i].sprite = White[i].sprite[0]
        window.blit(Black[i].sprite, Black[i].pixel_loc_centered)
        window.blit(White[i].sprite, White[i].pixel_loc_centered)
        print(black_loc)
        print(white_loc)
        pygame.display.flip()
    return(B, Black, White)    
            
    

if __name__ == "__main__":
    pass

