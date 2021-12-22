import pandas as pd, numpy as np, itertools
fname = 'Sudoku Solution Validator-log.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]
validnums = [1,2,3,4,5,6,7,8,9]
def sudoku(puzzle):
    def isint(n):
        try:
            n += 1
            return True
        except TypeError:
            return False
    def gridnum(n):
        if row.index(n) < 3:
            if puzzle.index(row) < 3:
                return 1
            elif puzzle.index(row) < 6:
                return 4
            elif puzzle.index(row) < 9:
                return 7
        elif row.index(n) < 6:
            if puzzle.index(row) < 3:
                return 2
            elif puzzle.index(row) < 6:
                return 5
            elif puzzle.index(row) < 9:
                return 8
        elif row.index(n) < 9:
            if puzzle.index(row) < 3:
                return 3
            elif puzzle.index(row) < 6:
                return 6
            elif puzzle.index(row) < 9:
                return 9
    
    puzzle = puzzle.split()
    counter = itertools.count(1)
    temp = [[(char, next(counter)) for char in w] for w in puzzle]
    puzzle = pd.DataFrame.from_records(temp, index=[1,2,3,4,5,6,7,8,9], columns=['A','B','C','D','E','F','G','H','I'])




    for row in puzzle:
        for item in row:
            if not item == 0:
                item = f'im{item}'
            for num in validnums:
                if num in row: continue
                if num in [row[row.index(item)] for row in puzzle]: continue
                if num in grid: continue
                item = num







    griddict = {}
    griddict[1] = [(0,0)(0,1)(0,2)(1,0)(1,1)(1,2)(2,0)(2,1)(2,2)]
    griddict[2] = [(3,0)(3,1)(3,2)(4,0)(4,1)(4,2)(5,0)(5,1)(5,2)]
    griddict[3] = [(6,0)(6,1)(6,2)(7,0)(7,1)(7,2)(8,0)(8,1)(8,2)]
    griddict[4] = [(0,3)(0,4)(0,5)(1,3)(1,4)(1,5)(2,3)(2,4)(2,5)]
    griddict[5] = [(3,3)(3,4)(3,5)(4,3)(4,4)(4,5)(5,3)(5,4)(5,5)]
    griddict[6] = [(6,3)(6,4)(6,5)(7,3)(7,4)(7,5)(8,3)(8,4)(8,5)]
    griddict[7] = [(0,6)(0,7)(0,8)(1,6)(1,7)(1,8)(2,6)(2,7)(2,8)]
    griddict[8] = [(3,6)(3,7)(3,8)(4,6)(4,7)(4,8)(5,6)(5,7)(5,8)]
    griddict[9] = [(6,6)(6,7)(6,8)(7,6)(7,7)(7,8)(8,6)(8,7)(8,8)]

    numdict = {}
    for row in puzzle:
        for num in row:
            if not num == 0:
                numdict[f'{puzzle.index(row)}{row.index(num)}{gridnum[num]}'] = [False]
            elif num == 0:
                numdict[f'{puzzle.index(row)}{row.index(num)}{gridnum[num]}'] = [True]
    for row in npuzzle:
        for num in row:
            
    




    g1 = [item for row in puzzle[:3] for item in row[:3]]
    g2 = [item for row in puzzle[3:6] for item in row[:3]]
    g3 = [item for row in puzzle[6:9] for item in row[:3]]
    g4 = [item for row in puzzle[:3] for item in row[3:6]]
    g5 = [item for row in puzzle[3:6] for item in row[3:6]]
    g6 = [item for row in puzzle[6:9] for item in row[3:6]]
    g7 = [item for row in puzzle[:3] for item in row[6:9]]
    g8 = [item for row in puzzle[3:6] for item in row[6:9]]
    g9 = [item for row in puzzle[6:9] for item in row[6:9]]


    """return the solved puzzle as a 2d array of 9 x 9"""
    grids = [g1, g2, g3, g4, g5, g6, g7, g8, g9]
    c1 = [row[0] for row in puzzle]
    c2 = [row[1] for row in puzzle]
    c3 = [row[2] for row in puzzle]
    c4 = [row[3] for row in puzzle]
    c5 = [row[4] for row in puzzle]
    c6 = [row[5] for row in puzzle]
    c7 = [row[6] for row in puzzle]
    c8 = [row[7] for row in puzzle]
    c9 = [row[8] for row in puzzle]
    columns = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
    for row in puzzle:
        for i in row:
            if not i == 0:
                i = f'i{i}'
    
    for row in puzzle:
        for i in row:
            ind = row.index(i)
            for num in validnums:
                if num in row: continue
                if num in [row[ind] for row in puzzle]: continue
                if isint(i) == False: continue
                row[ind] = num
    print(puzzle)

    
    def valid_solution(board):
        gs=[[x for r in board[:3] for x in r[:3]], [x for r in board[3:6] for x in r[:3]], [x for r in board[6:9] for x in r[:3]], [x for r in board[:3] for x in r[3:6]], [x for r in board[3:6] for x in r[3:6]], [x for r in board[6:9] for x in r[3:6]], [x for r in board[:3] for x in r[6:9]], [x for r in board[3:6] for x in r[6:9]], [x for r in board[6:9] for x in r[6:9]]]
        def cr(n):return all(i for i in [True if r.count(x)==1 and str(x) in ['1','2','3','4','5','6','7','8','9'] else False for r in n for x in r])
        def cc(n):return all(i for i in [True if c.count(x)==1 and str(x) in ['1','2','3','4','5','6','7','8','9'] else False for c in [[r[i] for r in n] for i in range(9)] for x in c])
        def cg(n):return all(i for i in [True if g.count(x)==1 and str(x) in ['1','2','3','4','5','6','7','8','9'] else False for g in gs for x in g])
        return all(i for i in [cr(board), cc(board), cg(board)])


    print(valid_solution(puzzle))
    return puzzle
print(sudoku(puzzle))