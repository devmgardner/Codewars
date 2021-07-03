import itertools
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
    


    gs=[[x for r in puzzle[:3] for x in r[:3]], [x for r in puzzle[3:6] for x in r[:3]], [x for r in puzzle[6:9] for x in r[:3]], [x for r in puzzle[:3] for x in r[3:6]], [x for r in puzzle[3:6] for x in r[3:6]], [x for r in puzzle[6:9] for x in r[3:6]], [x for r in puzzle[:3] for x in r[6:9]], [x for r in puzzle[3:6] for x in r[6:9]], [x for r in puzzle[6:9] for x in r[6:9]]]
    cs=[[r[i] for r in n] for i in range(9)]





    cg(puzzle)
    cc(puzzle)
    cr(puzzle)
    while not valid_solution(puzzle):
        cg(puzzle)
        cc(puzzle)
        cr(puzzle)
    fhand.write(f'final puzzle is {puzzle}')
print(sudoku(input()))