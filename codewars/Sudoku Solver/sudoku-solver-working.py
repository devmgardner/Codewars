fname = 'sudoku-working-log.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
validnums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def valid_solution(board):
    gs=[[x for r in board[:3] for x in r[:3]], [x for r in board[3:6] for x in r[:3]], [x for r in board[6:9] for x in r[:3]], [x for r in board[:3] for x in r[3:6]], [x for r in board[3:6] for x in r[3:6]], [x for r in board[6:9] for x in r[3:6]], [x for r in board[:3] for x in r[6:9]], [x for r in board[3:6] for x in r[6:9]], [x for r in board[6:9] for x in r[6:9]]]
    def cr(n):return all(i for i in [True if r.count(x)==1 and str(x) in ['1','2','3','4','5','6','7','8','9'] else False for r in n for x in r])
    def cc(n):return all(i for i in [True if c.count(x)==1 and str(x) in ['1','2','3','4','5','6','7','8','9'] else False for c in [[r[i] for r in n] for i in range(9)] for x in c])
    def cg(n):return all(i for i in [True if g.count(x)==1 and str(x) in ['1','2','3','4','5','6','7','8','9'] else False for g in gs for x in g])
    return all(i for i in [cr(board), cc(board), cg(board)])

def sudoku(puzzle):
    puzzle = puzzle.split()
    temp = []
    for word in puzzle:
        newtemp = []
        for char in word:
            newtemp.append(int(char))
        temp.append(newtemp)
    puzzle = temp
    fhand.write(f'input is {puzzle}\n')
    """return the solved puzzle as a 2d array of 9 x 9"""
    #replace all 0s with any validnum not already in row
    for row in puzzle:
        fhand.write(f'current row is row #{puzzle.index(row)}\n')
        fhand.write(f'row contents are {row}\n')
        for i,rownum in enumerate(row):
            fhand.write(f'current rownum is {rownum}\n')
            for validnum in validnums:
                if rownum == 0:
                    fhand.write(f'rownum is 0, replacing with first validnum not in row\n')
                    fhand.write(f'checking {validnum} in row\n')
                    if not validnum in row:
                        fhand.write(f'{validnum} not in row, inserting\n')
                        row[i] = validnum
    def cg(n):
        gs=[[x for r in puzzle[:3] for x in r[:3]], [x for r in puzzle[3:6] for x in r[:3]], [x for r in puzzle[6:9] for x in r[:3]], [x for r in puzzle[:3] for x in r[3:6]], [x for r in puzzle[3:6] for x in r[3:6]], [x for r in puzzle[6:9] for x in r[3:6]], [x for r in puzzle[:3] for x in r[6:9]], [x for r in puzzle[3:6] for x in r[6:9]], [x for r in puzzle[6:9] for x in r[6:9]]]
        fhand.write(f'checking grids, current board is {puzzle}\n')
        for g in gs:
            fhand.write(f'----current grid is grid#{gs.index(g)}: {g}----\n')
            for x in g:
                for validnum in validnums:
                    if not g.count(x) == 1 and not validnum in g:
                        fhand.write(f'\tGRID\t\t\tgrid check, found error with number {x}, validnum {validnum} not in grid, replacing\n')
                        gridnumber = gs.index(g)
                        gridindexofx = g.index(x)
                        if gridnumber in range(0,3):
                            fhand.write(f'gridnumber is in first row of grids\n')
                            if gridindexofx in range(0,3):
                                fhand.write(f'index of x in grid is 1-3, must be in first row\n')
                                fhand.write(f'n[0] is {n[0]}\n')
                                fhand.write(f'3 * gridnumber is {3 * gridnumber}\n')
                                fhand.write(f'gridindexofx + (3 * gridnumber) is {gridindexofx + (3 * gridnumber)}\n')
                                n[0][gridindexofx + (3 * gridnumber)] = validnum
                            
                            elif gridindexofx in range(3,6):
                                fhand.write(f'index of x in grid is 4-6, must be in second row\n')
                                fhand.write(f'n[1] is {n[1]}\n')
                                fhand.write(f'3 * gridnumber is {3 * gridnumber}\n')
                                fhand.write(f'gridindexofx + (3 * gridnumber) is {gridindexofx + (3 * gridnumber)}\n')
                                n[1][gridindexofx + (3 * gridnumber)] = validnum
                            
                            elif gridindexofx in range(6,9):
                                fhand.write(f'index of x in grid is 7-9, must be in third row\n')
                                fhand.write(f'n[2] is {n[2]}\n')
                                fhand.write(f'3 * gridnumber is {3 * gridnumber}\n')
                                fhand.write(f'gridindexofx + (3 * gridnumber) is {gridindexofx + (3 * gridnumber)}\n')
                                n[2][gridindexofx + (3 * gridnumber)] = validnum
                        
                        
                        
                        elif gridnumber in range(3,6):
                            fhand.write(f'gridnumber is in second row of grids\n')
                            
                            if gridindexofx in range(0,3):
                                fhand.write(f'index of x in grid is 1-3, must be in fourth row\n')
                                fhand.write(f'n[3] is {n[3]}\n')
                                fhand.write(f'3 * gridnumber-3 is {3 * (gridnumber-3)}\n')
                                fhand.write(f'gridindexofx + (3 * gridnumber-3) is {gridindexofx + (3 * (gridnumber-3))}\n')
                                n[3][gridindexofx + (3 * (gridnumber-3))] = validnum
                            
                            elif gridindexofx in range(3,6):
                                fhand.write(f'index of x in grid is 4-6, must be in fifth row\n')
                                fhand.write(f'n[4] is {n[4]}\n')
                                fhand.write(f'3 * gridnumber is {3 * (gridnumber-3)}\n')
                                fhand.write(f'gridindexofx + (3 * (gridnumber-3))) is {gridindexofx + (3 * (gridnumber-3))}\n')
                                n[4][gridindexofx + (3 * (gridnumber-3))] = validnum
                            
                            elif gridindexofx in range(6,9):
                                fhand.write(f'index of x in grid is 7-9, must be in sixth row\n')
                                fhand.write(f'n[5] is {n[5]}\n')
                                fhand.write(f'3 * (gridnumber-3)) is {3 * (gridnumber-3)}\n')
                                fhand.write(f'gridindexofx + (3 * (gridnumber-3))) is {gridindexofx + (3 * (gridnumber-3))}\n')
                                n[5][gridindexofx + (3 * (gridnumber-3))] = validnum
                        
                        
                        
                        elif gridnumber in range(6,9):
                            fhand.write(f'gridnumber is in third row of grids\n')
                            if gridindexofx in range(0,3):
                                fhand.write(f'index of x in grid is 1-3, must be in seventh row\n')
                                fhand.write(f'n[6] is {n[6]}\n')
                                fhand.write(f'3 * (gridnumber-6) is {3 * (gridnumber-6)}\n')
                                fhand.write(f'gridindexofx + (3 * (gridnumber-6)) is {gridindexofx + (3 * (gridnumber-6))}\n')
                                n[6][gridindexofx + (3 * (gridnumber-6))] = validnum
                            
                            elif gridindexofx in range(3,6):
                                fhand.write(f'index of x in grid is 4-6, must be in eighth row\n')
                                fhand.write(f'n[7] is {n[7]}\n')
                                fhand.write(f'3 * (gridnumber-6) is {3 * (gridnumber-6)}\n')
                                fhand.write(f'gridindexofx + (3 * (gridnumber-6)) is {gridindexofx + (3 * (gridnumber-6))}\n')
                                n[7][gridindexofx + (3 * (gridnumber-6))] = validnum
                            
                            elif gridindexofx in range(6,9):
                                fhand.write(f'index of x in grid is 7-9, must be in ninth row\n')
                                fhand.write(f'n[8] is {n[8]}\n')
                                fhand.write(f'3 * (gridnumber-6) is {3 * (gridnumber-6)}\n')
                                fhand.write(f'gridindexofx + (3 * (gridnumber-6)) is {gridindexofx + (3 * (gridnumber-6))}\n')
                                n[8][gridindexofx + (3 * (gridnumber-6))] = validnum

    def cc(n):
        cs=[[r[i] for r in n] for i in range(9)]
        fhand.write(f'checking columns, current board is {puzzle}\n')
        for c in cs:
            fhand.write(f'----current column is {c}----\n')
            for i,x in enumerate(c):
                for validnum in validnums:
                    if not c.count(x) == 1 and not validnum in c:
                        fhand.write(f'\t\tCOLUMN\t\tcolumn check, found error with number {x}, validnum {validnum} not in column, replacing\n')
                        n[c.index(x)][cs.index(c)] = validnum

    def cr(n):
        fhand.write(f'checking rows, current board is {puzzle}\n')
        for r in n:
            fhand.write(f'----current row is {r}----\n')
            for i,x in enumerate(r):
                for validnum in validnums:
                    if not r.count(x) == 1 and not validnum in r:
                        fhand.write(f'\t\t\tROW\trow check, found error with number {x}, validnum {validnum} not in row, replacing\n')
                        n[n.index(r)][i] = validnum
    cg(puzzle)
    cc(puzzle)
    cr(puzzle)
    while not valid_solution(puzzle):
        cg(puzzle)
        cc(puzzle)
        cr(puzzle)
    fhand.write(f'final puzzle is {puzzle}')
print(sudoku(input()))