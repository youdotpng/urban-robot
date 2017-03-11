

class Piece:
    def __init__(self, name = 'pawn_0_U', str_loc = 'A2', mov_count = 0):
        self.name = name
        self.loc = str_loc
        self.mov_count = mov_count

    def set_mov_count(self,mov_count):
        self.mov_count = mov_count

    def get_mov_count(self):
        return self.mov_count

    def set_loc(self,str_loc):
        self.loc = str_loc

    def get_loc(self):
        return self.loc

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Pawn(Piece):  
    def move(self, candidate):
        self.candidate = candidate

        if(self.mov_count == 0 and candidate[1] == self.loc[1] and candidate[2] == int(self.loc[2])+2):
            self.set_loc(candidate)

        #basic forward movement only

        if(candidate[1] == self.loc[1] and candidate[2] == int(self.loc[2])+1):
            self.set_loc(candidate)
            

class Rook(Piece):  
    print('f')      

class Knight(Piece):    
    print('f')  

class Bishop(Piece):    
    print('f')  

class Queen(Piece):
    print('f')  

class King(Piece):
    print('f')  

class Board:
    def __init__(self):

        # Initialize empty board
        self.board = dict()
        for j in ['A','B','C','D','E','F','G','H']:
            for i in range(1,9,1):
                self.board[j+str(i)] = 0

        #Initialize two rows of pieces on either end of the board
        for j in ['A','B','G','H']:
            for i in range(1,9,1):
                self.board[j+str(i)] = 1

    def piece_check(self, row, col):
        if self.board[row+str(col)] == 1:
            return(True)
        if self.board[row+str(col)] == 0:
            return(False)
        else:
            raise
        
def Boardset():
    B = Board()

    Black = [0]*16
    White = [0]*16
  
    Black[0] = Rook("rook_1_B","H1") 
    White[0] = Rook("rook_1_W","A1")
    Black[1] = Rook("rook_2_B","H8") 
    White[1] = Rook("rook_2_W","A8")
    Black[2] = Knight("knight_1_B","H2") 
    White[2] = Knight("knight_1_W","A2")
    Black[3] = Knight("knight_2_B","H7") 
    White[3] = Knight("knight_2_W","A7")
    Black[4] = Bishop("bishop_1_B","H3") 
    White[4] = Bishop("bishop_1_W","A3")
    Black[5] = Bishop("bishop_2_B","H6") 
    White[5] = Bishop("bishop_2_W","A6")
    Black[6] = King("king_1_B","H5")
    White[6] = King("king_1_W","A5")
    Black[7] = Queen("queen_1_B","H4")
    White[7] = Queen("queen_1_W","A4")

    for i in range(1,9,1):
        Black[i+7] = Pawn("pawn_"+str(i)+"_B","G"+str(i))
        White[i+7] = Pawn("pawn_"+str(i)+"_W","B"+str(i))
               
    for i in range(0,16,1):
        black_loc = Black[i].get_loc()
        white_loc = White[i].get_loc()
        print(black_loc)
        print(white_loc)
    return(B, Black, White)    
            
    

if __name__ == "__main__":
    main()

