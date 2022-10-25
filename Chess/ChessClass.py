import random






    # def movePiece(self, piece, start, end):
    #     if piece.color == "white":
    #         if piece.name == "pawn":
    #             if piece.move(start, end, self.board):
    #                 self.move(start, end)
    #                 return True
    #             else:
    #                 return False
    #         elif piece.name == "rook":
    #             if piece.move(start, end, self.board):
    #                 self.move(start, end)
    #                 return True
    #             else:
    #                 return False
    #         elif piece.name == "knight":
    #             if piece.move(start, end, self.board):
    #                 self.move(start, end)
    #                 return True
    #             else:
    #                 return False
    #         elif piece.name == "bishop":
    #             if piece.move(start, end, self.board):
    #                 self.move(start, end)
    #                 return True
    #             else:
    #                 return False
    #         elif piece.name == "queen":
    #             if piece.move(start, end, self.board):
    #                 self.move(start, end)
    #                 return True
    #             else:
    #                 return False
    #         elif piece.name == "king":
    #             if piece.move(start, end, self.board):
    #                 self.move(start, end)
    #                 return True
    #             else:
    #                 return False
    #     elif piece.color == "black":
    #         if piece.name == "pawn":
    #             if piece.move(start, end, self.board):
    #                 self.move(start, end)
    #                 return True
    #             else:
    #                 return False
    #         elif piece.name == "rook":
    #             if piece.move(start, end, self.board):
    #                 self.move(start, end)
    #                 return True
    #             else:
    #                 return False
    #         elif piece.name == "knight":
    #             if piece.move(start, end, self.board):
    #                 self.move(start, end)
    #                 return True
    #             else:
    #                 return False
    #         elif piece.name == "bishop":
    #             if piece.move(start, end, self.board):
    #                 self.move(start, end)
    #                 return True
    #             else:
    #                 return False
    #         elif piece.name == "queen":
    #             if piece.move(start, end, self.board):
    #                 self.move(start, end)
    #                 return True
    #             else:
    #                 return False
    #         elif piece.name == "king":
    #             if piece.move(start, end, self.board):
    #                 self.move(start, end)
    #                 return True
    #             else:
    #                 return False            


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
    
class emptySpace(chessPiece):
    def __init__(self):
        self.name = "empty"
        self.color = "empty"
    def move(self, start, end):
        return False
    def attack(self, start, end):
        return False
    def castling(self, start, end):
        return False
    def enPassant(self, start, end):
        return False
    def promotion(self, start, end):
        return False
    def check(self, start, end):
        return False
    def checkMate(self, start, end):
        return False
    def staleMate(self, start, end):
        return False

class pawn(chessPiece):
    def __init__(self, name, color):
        super().__init__(name, color)
    def move(self, start, end):
        if self.color == 'white':
            if start[0] == 1:
                if end[0] == 3:
                    return True
            if start[0] + 1 == end[0] and start[1] == end[1]:
                return True
        if self.color == 'black':
            if start[0] == 6:
                if end[0] == 4:
                    return True
            if start[0] - 1 == end[0]:
                return True
        return False
    def attack(self, start, end):
        if self.color == 'white':
            if start[0] + 1 == end[0]:
                if start[1] + 1 == end[1]:
                    return True
                if start[1] - 1 == end[1]:
                    return True
        if self.color == 'black':
            if start[0] - 1 == end[0]:
                if start[1] + 1 == end[1]:
                    return True
                if start[1] - 1 == end[1]:
                    return True
        return False
    def castling(self, start, end):
        if start[0] == end[0] or start[1] == end[1]:
            return True
        return False

class rook(chessPiece):
    def __init__(self, name, color):
        super().__init__(name, color)
    def move(self, start, end):
        if start[0] == end[0] or start[1] == end[1]:
            return True
        return False
    def attack(self, start, end):
        if start[0] == end[0] or start[1] == end[1]:
            return True
        return False
    def castling(self, start, end):
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
    def attack(self, start, end):
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
    def attack(self, start, end):
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
    def attack(self, start, end):
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
    def attack(self, start, end):
        if abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1:
            return True
        return False
    def castling(self, start, end):
        if start[0] == 0 and start[1] == 4:
            if end[0] == 0 and end[1] == 6:
                return True
        if start[0] == 0 and start[1] == 4:
            if end[0] == 0 and end[1] == 2:
                return True
        if start[0] == 7 and start[1] == 4:
            if end[0] == 7 and end[1] == 6:
                return True
        if start[0] == 7 and start[1] == 4:
            if end[0] == 7 and end[1] == 2:
                return True
        return False

##a class that uses the chessPiece class to create a
##chess board with the pieces in their starting positions



class chessBoard():
    def __init__(self, board):
        self.board = board
    def getBoard(self):
        return self.board
    def setBoard(self, board):
        self.board = board
    def findPiece(self, start):
        return self.board[start[0]][start[1]]
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
        i = start[0]
        j = start[1]
        k = end[0]
        l = end[1]
        print (i,j,k,l)
        print()
        print(self.board[i][j].name, self.board[i][j].color)
        print(self.board[k][l].name, self.board[k][l].color)
        if self.board[i][j].color == self.board[k][l].color:
            return False
        if self.board[start[0]][start[1]].move(start, end) == True:
            self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = emptySpace()
        elif self.board[start[0]][start[1]].attack(start, end) == True:
            self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = emptySpace
        elif self.board[start[0]][start[1]].castling(start, end) == True:
            self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = emptySpace()
        else:
            return False
        
    def pointsWhite(self):
        points = 0
        for i in range(8):
            for j in range(8):
                try:
                    if self.board[i][j].color == "white":
                        points += 1
                except:
                    pass
        return points
    def pointsBlack(self):
        points = 0
        for i in range(8):
            for j in range(8):
                try:
                    if self.board[i][j].color == "black":
                        points += 1
                except:
                    pass
        return points
    



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
    #Allocate the empty spaces with emptySpace objects
    for i in range(2,6):
        for j in range(8):
            board[i][j] = emptySpace()
    
    return board

def checkValidMove(chessBoard, start, end):
    if chessBoard.board[start[0]][start[1]].color == chessBoard.board[end[0]][end[1]].color:
        return False
    if chessBoard.board[start[0]][start[1]].move(start, end) == True:
        return True
    if chessBoard.board[start[0]][start[1]].attack(start, end) == True:
        return True
    if chessBoard.board[start[0]][start[1]].castling(start, end) == True:
        return True
    return False
def main():
    #create the chess board object
  
    chessBoard1 = chessBoard(boardSetup())
    #print the board
    chessBoard1.printBoard()
    #move a piece
    chessBoard1.move([1, 0], [2, 0])
    chessBoard1.move([2, 0], [3, 0])
    chessBoard1.move([3, 0], [4, 0])
    chessBoard1.move([4, 0], [5, 0])
    chessBoard1.move([5, 0], [6, 7])
    chessBoard1.move([0, 0], [4,0])
    chessBoard1.move([4,0], [6,7])
    #print the board
    chessBoard1.printBoard()
    # print(chessBoard1.pointsWhite())
    # print(chessBoard1.pointsBlack())

main()




    
        