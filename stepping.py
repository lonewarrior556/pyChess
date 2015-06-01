class SteppingPiece(object):
    MOTIONS = {"Knight": (8,12,19,21,-8,-12,-19,-21),
             "King": (1,9,10,11,-1,-9,-10,-11)}

    DISPLAY_PIECES = {"blackKnight": u' \u265e', "blackKing": u' \u265a',
                      "whiteKnight": u' \u2658', "whiteKing": u' \u2654'}


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
            if y in range(1,79) and y % 10 % 9 != 0:
                ls[-1].append(y)
        return ls

    def render(self):
        return self.DISPLAY_PIECES[self.color + type(self).__name__]

class Knight(SteppingPiece):
    def __init__(self, position):
        self.notation = 'K'
        super(Knight, self).__init__(self,position)

class King(SteppingPiece):
    def __init__(self, position):
        self.notation = 'N'
        super(King, self).__init__(self,position)
