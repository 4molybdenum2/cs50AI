from tictactoe import player,actions,result,winner,terminal,utility,minimax,max_value,min_value

X = "X"
O = "O"
EMPTY = None

board = [[O,X,EMPTY],
        [O,X,X],
        [O,O,X]]


# print(player(board))
# print(actions(board))
# print(result(board,(0,1)))
# print(winner(board))
# print(terminal(board))
# print(utility(board))
print(terminal(board))
print(winner(board))