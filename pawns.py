class Pawn(object):


    def __init__(self, position):
        self.color = 'white'
        self.position = position
        self.touched = False
        self.notation = ""

    def motions(self):
        ls = [20,10,9,11]
        if self.color == "black":
            ls = map(lambda x: x*-1, ls)
        return ls


    def moves(self,board):
        motions = self.motions()
        ls = []
        for x in motions:
            ls.append([])
            y = self.position + x
            if y in range(1,79) and y % 10 % 9 != 0:
                if x in [20, -20]:
                    if self.touched or board[y]:
                        continue
                elif x in [10, -10]:
                    if board[y]:
                        continue
                elif not board[y]:
                    continue
                ls[-1].append(y)
        return ls

    def render(self):
        if self.color == "white":
            return u' \u2659'
        else:
            return u' \u265f'
