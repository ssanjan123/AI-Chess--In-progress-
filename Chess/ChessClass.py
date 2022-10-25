import random



class chessBoard:
    def __init__(self, board):
        self.board = board
    def getBoard(self):
        return self.board
    def setBoard(self, board):
        self.board = board
    def printBoard(self):
        for i in range(8):
            for j in range(8):
                if j<7:
                    try:
                        print(self.board[i][j].name, self.board[i][j].color, end = " ")
                    except:
                        print("Empty", end = " ")
                else:
                    try:
                        print(self.board[i][j].name, self.board[i][j].color)
                    except:
                        print("Empty")
        print()        
            
    def move(self, start, end):
        self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = 0
    def pointsWhite(self):
        points = 0
        for i in range(8):
            for j in range(8):
                try:
                    if self.board[i][j].color == "White":
                        points += self.board[i][j].value
                except:
                    pass
        return points
    

class chessPiece:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def getName(self):
        return self.name
    def getColor(self):
        return self.color
    def setName(self, name):
        self.name = name
    def setColor(self, color):
        self.color = color

class pawn(chessPiece):
    def __init__(self, name, color):
        super().__init__(name, color)
    def move(self, start, end):
        if self.color == 'white':
            if start[0] == 1:
                if end[0] == 3:
                    return True
            if start[0] + 1 == end[0]:
                return True
        if self.color == 'black':
            if start[0] == 6:
                if end[0] == 4:
                    return True
            if start[0] - 1 == end[0]:
                return True
        return False

class rook(chessPiece):
    def __init__(self, name, color):
        super().__init__(name, color)
    def move(self, start, end):
        if start[0] == end[0] or start[1] == end[1]:
            return True
        return False

class knight(chessPiece):
    def __init__(self, name, color):
        super().__init__(name, color)
    def move(self, start, end):
        if abs(start[0] - end[0]) == 2 and abs(start[1] - end[1]) == 1:
            return True
        if abs(start[0] - end[0]) == 1 and abs(start[1] - end[1]) == 2:
            return True
        return False

class bishop(chessPiece):
    def __init__(self, name, color):
        super().__init__(name, color)
    def move(self, start, end):
        if abs(start[0] - end[0]) == abs(start[1] - end[1]):
            return True
        return False

class queen(chessPiece):
    def __init__(self, name, color):
        super().__init__(name, color)
    def move(self, start, end):
        if start[0] == end[0] or start[1] == end[1]:
            return True
        if abs(start[0] - end[0]) == abs(start[1] - end[1]):
            return True
        return False

class king(chessPiece):
    def __init__(self, name, color):
        super().__init__(name, color)
    def move(self, start, end):
        if abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1:
            return True
        return False
def kingInCheck(board, color):
    for i in range(8):
        for j in range(8):
            if board[i][j] != 0:
                if board[i][j].name == 'king' and board[i][j].color == color:
                    kingPos = [i, j]
    for i in range(8):
        for j in range(8):
            if board[i][j] != 0:
                if board[i][j].color != color:
                    if board[i][j].move([i, j], kingPos):
                        return True
    return False

def checkMate(board, color):
    for i in range(8):
        for j in range(8):
            if board[i][j] != 0:
                if board[i][j].color == color:
                    for k in range(8):
                        for l in range(8):
                            if board[i][j].move([i, j], [k, l]):
                                if kingInCheck(board, color):
                                    return False
    return True

def staleMate(board, color):
    for i in range(8):
        for j in range(8):
            if board[i][j] != 0:
                if board[i][j].color == color:
                    for k in range(8):
                        for l in range(8):
                            if board[i][j].move([i, j], [k, l]):
                                return False
    return True

def pawnPromotion(board, color):
    if color == 'white':
        for i in range(8):
            if board[7][i] != 0:
                if board[7][i].name == 'pawn':
                    return True
    if color == 'black':
        for i in range(8):
            if board[0][i] != 0:
                if board[0][i].name == 'pawn':
                    return True
    return False

def pawnPromotionChoice(board, color):
    if color == 'white':
        for i in range(8):
            if board[7][i] != 0:
                if board[7][i].name == 'pawn':
                    board[7][i].setName('queen')
    if color == 'black':
        for i in range(8):
            if board[0][i] != 0:
                if board[0][i].name == 'pawn':
                    board[0][i].setName('queen')

def kill(board, start, end):
    if board[end[0]][end[1]] != 0:
        if board[end[0]][end[1]].color != board[start[0]][start[1]].color:
            board[end[0]][end[1]] = 0
            return True
    return False

def boardSetup():
    board = [[0 for i in range(8)] for j in range(8)]
    for i in range(8):
        board[1][i] = pawn('pawn', 'white')
        board[6][i] = pawn('pawn', 'black')
    board[0][0] = rook('rook', 'white')
    board[0][7] = rook('rook', 'white')
    board[7][0] = rook('rook', 'black')
    board[7][7] = rook('rook', 'black')
    board[0][1] = knight('knight', 'white')
    board[0][6] = knight('knight', 'white')
    board[7][1] = knight('knight', 'black')
    board[7][6] = knight('knight', 'black')
    board[0][2] = bishop('bishop', 'white')
    board[0][5] = bishop('bishop', 'white')
    board[7][2] = bishop('bishop', 'black')
    board[7][5] = bishop('bishop', 'black')
    board[0][3] = queen('queen', 'white')
    board[7][3] = queen('queen', 'black')
    board[0][4] = king('king', 'white')
    board[7][4] = king('king', 'black')
    return board


def main():
    #create the chess board object
  
    chessBoard1 = chessBoard(boardSetup())
    #print the board
    chessBoard1.printBoard()
    #move a piece
    chessBoard1.move([1, 0], [2, 0])
    #print the board
    chessBoard1.printBoard()

main()




    
        