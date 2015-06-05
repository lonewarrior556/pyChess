from pieces import *
from helpers import *
import operator
import sys
import copy

class Board(object):

    def __init__(self):
        self.board = [False]*79
        self.populate()
        self.player_turn = 'white'
        self.log = [[]]
        self.game_over = False

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

    def toggle_turn(self):
        if self.player_turn == 'white':
            return 'black'
        else:
            return 'white'

    def log_move(self,b,origin, destination,piece):
        if len(self.log[-1]) == 2:
            self.log.append([])
        transition = ""
        in_check = " "
        if self.board[destination]:
            transition = 'x'
        self.move(origin,destination)
        if self.check(self.toggle_turn()):
            if self.mate(self.toggle_turn()):
                in_check = "#"
                self.game_over = True
            else:
                in_check = u'\u271D '
        elif self.mate(self.toggle_turn()):
            in_check = " DRAW 0.5 - 0.5"
            self.game_over = True

        self.log[-1].append(piece.notation+transition+b+in_check)

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
        b = self.king_position(color) or 0
        for i in range(79):
            if self.legal_move(i,b):
                return True
        return False

    def mate(self, color):
        for i in range(1,79):
            for j in range(1,79):
                if self.legal_move(i,j) and self.board[i].color == color:
                    new_board = copy.deepcopy(self)
                    new_board.move(i,j)
                    if not new_board.check(color):
                        return False
        return True


    def stale_mate():
        pass

    def legal_move(self, a, b):
        piece = self.board[a]
        if not piece:
            return False
        elif not self.clear_path(a,b,piece):
            return False
        elif  self.board[b] and self.board[b].color == piece.color:
            return False
        else:
            dupped_board = copy.deepcopy(self)
            dupped_board.move(a,b)
            if dupped_board.check(self.player_turn):
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
            self.player_turn = self.toggle_turn()
            self.display()
        else:
            print "illegal move"

    def display(self):
        sys.stderr.write("\x1b[2J\x1b[H\n")
        for i in range(7,-1,-1):
            row =  "  ["+str(i+1)+"] "
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
        print  "       A|B|C|D|E|F|G|H"
