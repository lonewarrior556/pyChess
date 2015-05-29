class Pawn(object):

    MOTIONS = [10,20,9,11]


    def __init__(self, position):
        self.color = 'white'
        self.position = position
        self.touches = False


    def moves(self):
        moves = self.MOTIONS
        if self.color == "black":
            moves = map(lambda x: x*-1, moves)
        return moves
