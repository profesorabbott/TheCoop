def print_board(board):
    for i in board:
        print(i)

def player_input(team, dim1, dim2, board):
    
    if board[dim1][dim2] != "-":
        return("Non-valid space")
    else:
        board[dim1][dim2] = team
        return board
        
    
board = [["-","-","-"],["-","-","-"],["-","-","-"]]
print_board(board)

board = player_input("x",0,0,board)
print_board(board)