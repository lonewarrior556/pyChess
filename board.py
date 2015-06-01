from pieces import *
from helpers import *
import operator
import sys

class Board(object):

    def __init__(self):
        self.board = [False]*79
        self.populate()
        self.player_turn = 'white'
        self.log = [[]]

    def populate(self):
        # for i in range(11,19):
        #     self.board[i] = Pawn(i)
        for i in [3,6]:
            self.board[i] = Bishop(i)
        for i in [1,8]:
            self.board[i] = Rook(i)
        for i in [2,7]:
            self.board[i] = Knight(i)
        self.board[4]     = Queen(4)
        self.board[5]     = King(5)
        self.mirror_black( 70, range(1,9) )
        # self.mirror_black( 50, range(11,19) )

    def mirror_black(self, offset, rang):
        for i in rang:
            j = i + offset
            self.board[j] = self.board[i].__class__(j)
            self.board[j].color = "black"

    def toggle_turn(self):
        if self.player_turn == 'white':
            self.player_turn = 'black'
        else:
            self.player_turn = 'white'

    def log_move(self,b,origin, destination,piece):
        transition = ""
        in_check = " "
        if self.board[destination]:
            transition = 'x'
        self.move(origin,destination)
        if self.check('white') or self.check('black'):
            in_check = u'\u271D '
        self.log[-1].append(piece.notation+transition+b+in_check)
        if len(self.log[-1]) == 2:
            self.log.append([])

    def clear_path(self, origin, destination, piece):
        for x in piece.moves(self.board):
            if destination in x:
                indices = list_split(x, destination)
                return  not set(get_elements(self.board, indices)[:-1]) - set([False])
        return False

    def king_position(self,color):
        for i in range(79):
            piece = self.board[i]
            if piece and piece.color+type(piece).__name__ == str(color)+"King":
                return i

    def check(self,color):
        b = self.king_position(color)
        for i in range(79):
            if self.legal_move(i,b):
                return True
        return False


    def legal_move(self, a, b):
        piece = self.board[a]
        if not piece:
            return False
        elif not self.clear_path(a,b,piece):
            return False
        elif  self.board[b] and self.board[b].color == piece.color:
            return False
        else:
            return True

    def move(self, a, b):
        piece = self.board[a]
        piece.position = b
        piece.touched = True
        self.board[b] = piece
        self.board[a] = False

    def player_move(self, a,b):
        translate = ['Q','a','b','c','d','e','f','g','h']
        origin = translate.index(a[0]) + (int(a[1])-1)*10
        destination = translate.index(b[0]) + (int(b[1])-1)*10

        if self.legal_move(origin,destination) and self.board[origin].color == self.player_turn:
            self.log_move("".join(b),origin, destination, self.board[origin])
            self.toggle_turn()
        self.display()

    def display(self):
        # sys.stderr.write("\x1b[2J\x1b[H")
        for i in range(7,-1,-1):
            row =  "["+str(i+1)+"] "
            for j in range(1,9):
                if self.board[ 10*i + j]:
                    row += self.board[10*i + j].render()
                else:
                    row += ' _'
            try:
                log = self.log[i-8]
            except:
                log = ''
            print row + "    " + "".join(log)
        print  "     A|B|C|D|E|F|G|H"
