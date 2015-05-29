from pieces import *
from helpers import *
import operator

class Board(object):

    def __init__(self):
        self.board = [False]*79
        self.populate()

    def populate(self):
        for i in range(11,19):
            self.board[i] = Pawn(i)
        for i in [3,6]:
            self.board[i] = Bishop(i)
        for i in [1,8]:
            self.board[i] = Rook(i)
        for i in [2,7]:
            self.board[i] = Knight(i)
        self.board[4]     = Queen(4)
        self.board[5]     = King(5)
        self.mirror_black( 70, range(1,9) )
        self.mirror_black( 50, range(11,19) )


    def mirror_black(self, offset, rang):
        for i in rang:
            j = i + offset
            self.board[j] = self.board[i].__class__(j)
            self.board[j].color = "black"


    def direct_path(self, origin, destination, piece):
        for x in piece.moves:
            if destination in x:
                return list_split(x, destination):


    def legal_move(self, a, b):
        piece = self.board[a]
        conditions =[
        (piece),
        (b in reduce ( operator.add, piece.moves())),
        (not set(self.direct_path()[1:-1])-set([False])]),
        ((not self.board[b]) or (self.board[b].color != piece.color)) ]

        for x in conditions:
            if not x
                return False
        return True
