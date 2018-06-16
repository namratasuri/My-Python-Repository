

# Initializing the game board


board = [str(z+1) for z in range(0, 9)]

# This is the print board function which prints out the state of the board


def print_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8] + '\n')


# Ask and validate player input

def get_player_input(isPlayer1Turn):
    if isPlayer1Turn:
        symbol = 'X'
        print("Player1: ")
    else:
        symbol = 'O'
        print("Player2: ")
    position = int(input("Please enter position on the board: "))

    if position not in range(1, 10):
        print("Please enter a valid number from 1 to 9")
        get_player_input()
    if board[position-1] == 'X' or board[position-1] == 'O':
        print("This position has already been taken, please enter another position")
        get_player_input()
    else:
        board[position - 1] = symbol
        return not isPlayer1Turn


# Check if game has been won by any player


def check_game_won():

   if board[0] == board[4] == board[8]:
       return True
   if board[2] == board[4] == board[6]:
       return True

   for x in range(0, 3):
       if board[x] == board[x+3] and board[x] == board[x+6]:
           return True
       if board[x*3] == board[x*3+1] and board[x*3] == board[x*3+2]:
          return True


def main():
    isPlayer1Turn = True
    isGameWon = False
    moves = 0
    while not isGameWon and moves < 9:
        isPlayer1Turn = get_player_input(isPlayer1Turn)
        isGameWon = check_game_won()
        moves += 1
        print_board()
    if isGameWon:
        if isPlayer1Turn:
            print("Game Won by Player2")
        else:
            print("Game Won by Player1")
    else:
        print("Game Draw")


if __name__ == "__main__":
    main()


