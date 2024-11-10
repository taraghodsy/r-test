a=[['x','o','o'],
    ['x','x','-'],
    ['o','o','x']]
def check_winer(board):
    for row in board:
        if row[0] == row[1] == row [2] and row!= '':
            return(row[0] ,"win")
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and  board[0][col] != " ":
            return(board[0][col] , "win")
    if board[0][0] == board[1][1] == board[2][2] and  board[0][0] != " ":
            return(board[0][0] , "win")
    if board[0][2] ==board[1][1] ==board[2][0] and board[0][0] != " ":
        return(board[0][2] ,"win")


print(check_winer(a))