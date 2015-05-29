class SlidingPieces(object):

    MOTIONS = {'Rook': (1,10,-1,-10),
             'Bishop': (9,11,-9,-11),
             'Queen': (1,10,-1,-10)+(9,11,-9,-11)
             }


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
            while True:
                if y in range(1,79) and y % 10 % 9 != 0:
                    ls[-1].append(y)
                    y += x
                else:
                    break
        return ls



class Rook(SlidingPieces):
    def __init__(self, position):
        super(Rook, self).__init__(self, position)

class Bishop(SlidingPieces):
    def __init__(self, position):
        super(Bishop, self).__init__(self, position)

class Queen(SlidingPieces):
    def __init__(self, position):
        super(Queen, self).__init__(self, position)
