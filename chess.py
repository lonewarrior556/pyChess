import board
import os
import pickle
import re
def welcome():
    os.system('clear')
    print "\nwelcome to python chess!\nby Konrad Dudziak\n"

if __name__ == "__main__":

    welcome()
    load = raw_input("Load game? Y/n ").lower()
    while not load in ['y','n','yes','no','q']:
        print "try again.."
        load = raw_input("Load game? Y/n ").lower()
    if 'q' in load:
        exit()
    elif 'y' in load:
        files = os.listdir("./")
        dic = {}
        i = 1
        for x in files:
            if 'saved-game' in x:
                dic[str(i)] = x
                i+=1
        if len(dic) == 0:
            print "sorry, no saved games available"
        else:

            print "\nselect game by number\n"

            for key, name in dic.items():
                print key, name.replace('_saved-game', "")
            game_key = raw_input()
            while not game_key in dic:
                print "no file"
                game_key = raw_input()
            file = open(dic[game_key],'r')
            chess = pickle.load(file)
            file.close()

    try:
        chess.display()
        print "current turn "+ chess.player_turn
    except:
        chess = board.Board()
        chess.display()


    while not chess.game_over:
        user_input = raw_input("\nplease enter move: \n").lower()
        if 'save' in user_input:
            print "saving..."
            file_name = raw_input("select file name, no spaces please: ")
            save_name = file_name + "_saved-game"
            try:
                if file_name in os.listdir("./"):
                    if not raw_input("Overwrite " + file_name + "? Y" ).lower() in ['y','yes']:
                        continue
                file = open(save_name,'w+')
                pickle.dump(chess, file)
                file.close()
                print "saved " + file_name
                break
            except:
                print 'invalid file_name'
        elif 'exit' in user_input:
            confirmation = raw_input("are you sure you want to exit? Y").lower()
            if confirmation in ['y','yes']:
                break
        elif not re.search('^\s*[a-h]\s*[1-8]\s*,{1}\s*[a-h]\s*[1-8]\s*', user_input):
            print "please only 1 letter + number combinations seperated by 1 comma ie e2,e4 \nor write SAVE to save, EXIT to quit"
            continue
        else:
            user_input= user_input.split(",")
            chess.player_move(sorted(user_input[0])[::-1],sorted(user_input[1])[::-1])
    print "\nthanks for playing\n"

# enpassant
# promotions
# castling
