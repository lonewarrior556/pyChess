class SlidingPieces(object):

    MOTIONS = {'Rook': (1,10,-1,-10),
             'Bishop': (9,11,-9,-11),
             'Queen': (1,10,-1,-10)+(9,11,-9,-11)}

    DISPLAY_PIECES = {"blackQueen": u' \u265b',  "whiteQueen": u' \u2655',
                      "blackBishop": u' \u265d', "whiteBishop": u' \u2657',
                      "blackRook": u' \u265c',   "whiteRook": u' \u2656'}



    def __init__(self, piece, position):
        self.motion = self.MOTIONS[type(piece).__name__]
        self.color = 'white'
        self.position = position
        self.touched = False

    def moves(self,board):
        ls = []
        for x in self.motion:
            ls.append([])
            y = self.position + x
            while True:
                if y in range(1,79) and y % 10 % 9 != 0:
                    ls[-1].append(y)
                    y += x
                else:
                    break
        return ls

    def render(self):
        return self.DISPLAY_PIECES[self.color + type(self).__name__]


class Rook(SlidingPieces):
    def __init__(self, position):
        self.notation = 'R'
        super(Rook, self).__init__(self, position)

class Bishop(SlidingPieces):
    def __init__(self, position):
        self.notation = 'B'
        super(Bishop, self).__init__(self, position)

class Queen(SlidingPieces):
    def __init__(self, position):
        self.notation ="Q"
        super(Queen, self).__init__(self, position)
