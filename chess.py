import os
import pickle
def welcome():
    os.system('clear')
    print "\nwelcome to python chess!\nby Konrad Dudziak\n"



if __name__ == "__main__":

    welcome()
    load = raw_input("Load game? Y/n ").lower()

    while not load in ['y','n','yes','no']:
        print "try again.."
        load = raw_input("Load game? Y/n ").lower()
    if 'y' in load:
        files = os.listdir("./")
        dic = {}
        i = 1
        for x in files:
            if 'saved-game' in x and not ".pyc" in x:
                dic[str(i)] = x
                i+=1
        if len(dic) == 0:
            print "sorry, no saved games available"
        else:

            print "\nselect game by number\n"

            for key, name in dic.items():
                print key, name.replace('saved-game.py', "")
            game_key = raw_input()
            while not game_key in dic:
                print "no file"
                game_key = raw_input()



    else:
        print "New game!"
        import board
        chess = board.Board()
        chess.display()
        
