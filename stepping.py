class SteppingPiece(object):
    MOTIONS = {"Knight": (8,12,19,21,-8,-12,-19,-21),
             "King": (1,9,10,11,-1,-9,-10,-11)}

    def __init__(self, piece, position):
        self.motion = self.MOTIONS[type(piece).__name__]
        self.color = 'white'
        self.position = position
        self.touched = False

    def moves(self):
        ls = []
        for x in self.motion:
            ls.append([])
            y = self.position + x
            if y in range(1,79) and y % 10 % 9 != 0:
                ls[-1].append(y)
        return ls


class Knight(SteppingPiece):
    def __init__(self, position):
        super(Knight, self).__init__(self,position)

class King(SteppingPiece):
    def __init__(self, position):
        super(King, self).__init__(self,position)
