board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


def printBoard(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


def playerInput(board):
    inp = input("Please enter the numbers between 1-9: ")
    try:
        if int(inp) >= 1 and int(inp) <= 9 and board[int(inp) - 1] == "-":
            x = int(inp)
            board[x - 1] = currentPlayer
        elif int(inp) > 9:
            print("Please enter the number below 10")
        else:
            print("Ooops that spot has been already occupied!")
            switchPlayer()
    except ValueError:
        print("You have entered a string. Please enter a valid number between 1-9")


def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    if board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    if board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("\nIt's a tie! No one won.")
        gameRunning = False


def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


def checkWinner():
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        return comment()


def comment():
    global gameRunning
    print(f"The winner is {winner}")
    printBoard(board)
    gameRunning = False


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkTie(board)
    checkWinner()
    switchPlayer()
