import random
from TicTacToe1 import display_board
from TicTacToe2 import check_winner, check_draw

print("Tic Tac Toe Game")

print("Position Guide")
print("1 | 2 | 3")
print("---------")
print("4 | 5 | 6")
print("---------")
print("7 | 8 | 9")

print("Start game")

while True:
    print("\n Select mode")
    print("1. Multiplayer")
    print("2. Single Player")

    try:
        mode = int(input("Enter Choice: "))
        if mode not in[1, 2]:
            print("Enter 1 or 2 only!")
            continue
        break
    except ValueError:
        print("Enter Numbers only")
        continue

# names
player1 = input("Enter Player 1 name(X): ")

if mode == 1:
    player2 = input("Enter Player 2 name(O): ")
else:
    player2 = "Computer"

# score
score_x = 0
score_y = 0

while True:
    board = [" "]*9
    player = "X"

    while True:
        display_board(board)
        
        if(player == "X"):
            print(player1, "(X) turn")

            try: 
                pos = int(input("Enter position from (1-9): "))
            except:
                print("Enter number only")
                continue

            if pos < 1 or pos > 9:
                print("Enter number between 1 to 9")
                continue

            if board[pos - 1] != " ":
                print("Already Filled!")
                continue

            board[pos - 1] = player

        else:
            if mode == 1:
                print(player2, "(O) turn")

                try:
                    pos = int(input("Enter the number btw (1 - 9): "))
                    if pos < 1 or pos > 9:
                        print("Enter the number btw (1 - 9)")
                        continue
                except ValueError:
                    print("Enter numbers only")
                    continue

                if board[pos - 1] != " ":
                    print("Already filled")
                    continue

                board[pos - 1] = "O"
            else:
                print("Computer (O) turn")
                empty = []

                for i in range(9):
                    if board[i] == " ":
                        empty.append(i)

                choice = random.choice(empty)
                board[choice] = "O"

        # check wins
        if check_winner(board, player):
            display_board(board)
            
            if(player == "X"):
                print(player1, "Wins")
                score_x = score_x + 1
            else:
                print(player2, "Wins")
                score_y = score_y + 1

            break

        if check_draw(board):
            display_board(board)
            print("Match draw")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"

    # score board
    print("\nScore board")
    print(player1, ":", score_x)
    print(player2, ":", score_y)

    again = input("play again? (y/n): ")
    if again != "y":
        print("Game over")
        break
        

