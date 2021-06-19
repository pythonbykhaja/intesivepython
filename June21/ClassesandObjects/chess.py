class Piece:
    """
    This represents a piece in the chess game
    """
    def __init__(self,color,board): 
        """
        Initializer for the piece
        """
        self._color = color
        self._board = board

    def move(self):
        """
        This method defines the movement of chess piece
        """
        print("No movement defined")


class Pawn(Piece):
    def move(self):
        print("Single positon forward or cross")

class Bishop(Piece):
    def move(self):
        print("Move Cross in any direction by any number of steps")


class Board:
    pass
my_chess_board = Board()

bb1 = Bishop(color='Black', board=my_chess_board)
bb2 = Bishop(color='Black', board=my_chess_board)
wb1 = Bishop(color='White', board=my_chess_board)
wb2 = Bishop(color='White', board=my_chess_board)
bb1.move()

bp1 = Pawn(color='Black', board=my_chess_board)
bp1.move()