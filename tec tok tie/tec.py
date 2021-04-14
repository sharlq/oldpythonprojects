board = ['' for x in range(10)]

def insertletters(letter,pos):
    board[pos]= letter
def isposfree(pos):
    return board[pos] ==''
def isfull(board):
    if board.count('') > 1:
        return False
    else:
        return True

def iswinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))



def printboard(board):
    print(" " + board[1]+ " " + " | "+" " + board[2]+ " " + " | "+" " + board[3]+ " "  )
    print("--------------")
    print(" " + board[4] + " " + " | " + " " + board[5] + " " + " | " + " " + board[6] + " ")
    print("--------------")
    print(" " + board[7] + " " + " | " + " " + board[8] + " " + " | " + " " + board[9] + " ")


def playermove():
    run = True
    while run:
        move = input("Please select the position to inter x between 1 and 9")
        try:
            move = int(move)
            if move > 0 and move <10 :
                if isposfree(move):
                    run = False
                    insertletters("x",move)
                else:
                    print("sorry this place is ocupide")
            else:
                print("please type a number between 1 and 9")
        except:
            print("please type a number")

def selectRandom(li):
    import random
    ln =len(li)
    r = random.randrange(0,ln)
    return li[r]

def computermove():
    possiablemoves = [x for x , letter in enumerate(board) if letter =="" and x !=0]
    move =0
    for let in ["0","x"]:
      for i in possiablemoves:
        boardcopy = board[:]
        boardcopy[i]= let
        if iswinner(boardcopy,let):
          move = i
          return move

    cornersOpen=[]
    for i in possiablemoves:
        if i in (1,3,7,9):
            cornersOpen.append(i)
    if len(cornersOpen)>0:
        move = selectRandom(cornersOpen)# ارجعلها
        return move
    if 5 in possiablemoves:
        move = 5
        return move
    edgeOpen = []
    for i in possiablemoves:
        if i in [2,4,5,8]:
          edgeOpen.append(i)

    if len(edgeOpen)>0:
        move = selectRandom(edgeOpen)

def main():
    print("welcome to the game!")
    printboard(board)
    while not(isfull(board)):
        if not(iswinner(board,"0")):
            playermove()
            printboard(board)
        else:
            print("sorry you loose!")
            break

        if not(iswinner(board, "x")):
            move = computermove()
            if move == 0:
                print("")
            else:
                insertletters("0",move)
                print("computer placed O on position", move, ":")
                printboard(board)
        else:
            print("you win!")
            break
    if isfull(board):
        print("Tie game")

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == "y":
        board = ["" for x in range(10)]
        print("---------------------------")
        main()
    else:
        break