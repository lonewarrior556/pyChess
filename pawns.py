class Pawn(object):


    def __init__(self, position):
        self.color = 'white'
        self.position = position
        self.touched = False
        self.notation = ""

    def def_motions(self,board):
        ls = [10,9,11]
        if not self.touched:
            ls.insert(0,20)
        if self.color == "black":
            ls = map(lambda x: x*-1, ls)
        for i in range(2):
            x = ls.pop()
            diagnal_piece = board[self.position + x]
            if diagnal_piece and diagnal_piece.color != self.color:
                ls.insert(0,x)
        return ls

    def moves(self,board):
        motions = self.def_motions(board)
        ls = []
        for x in motions:
            ls.append([])
            y = self.position + x
            if y in range(1,79) and y % 10 % 9 != 0:
                ls[-1].append(y)
        return ls

    def render(self):
        if self.color == "white":
            return u' \u2659'
        else:
            return u' \u265f'
