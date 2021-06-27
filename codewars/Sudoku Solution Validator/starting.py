def valid_solution(board):
    #
    g1 = [row[:3] for row in board[:3]]
    return f'board is {board} and the result of this is {g1}'