def check_winner(board, player):
    # rows
    if(board[0] == board[1] == board[2] == player):
        return True
    if(board[3] == board[4] == board[5] == player):
        return True
    if(board[6] == board[7] == board[8] == player):
        return True
    
    # columns
    if(board[0] == board[3] == board[6] == player):
        return True
    if(board[1] == board[4] == board[7] == player):
        return True
    if(board[2] == board[5] == board[8] == player):
        return True
    
    # diagonals
    if(board[0] == board[4] == board[8] == player):
        return True
    if(board[6] == board[4] == board[2] == player):
        return True
    
    return False

def check_draw(board):
    for i in board:
        if i == " ":
            return False
    return True
