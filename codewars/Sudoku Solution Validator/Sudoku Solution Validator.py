fname = 'Sudoku Solution Validator-log.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
validnums = ['1','2','3','4','5','6','7','8','9']
def valid_solution(board):
    #
    #board = [list(row) for row in list(board.split())]
    fhand.write(f'input is {board}\n\n\n\n\n')
    board = [str(item) for row in board for item in row]
    #fhand.write(f'input after str conversion is {board}\n')
    #g1 = [row[:3] for row in board[:3]]
    #g2 = [row[3:6] for row in board[:3]]
    #g3 = [row[6:9] for row in board[:3]]
    #g4 = [row[:3] for row in board[3:6]]
    #g5 = [row[3:6] for row in board[3:6]]
    #g6 = [row[6:9] for row in board[3:6]]
    #g7 = [row[:3] for row in board[6:9]]
    #g8 = [row[3:6] for row in board[6:9]]
    #g9 = [row[6:9] for row in board[6:9]]
    g1 = [item for row in board[:3] for item in row[:3]]
    g2 = [item for row in board[3:6] for item in row[:3]]
    g3 = [item for row in board[6:9] for item in row[:3]]
    g4 = [item for row in board[:3] for item in row[3:6]]
    g5 = [item for row in board[3:6] for item in row[3:6]]
    g6 = [item for row in board[6:9] for item in row[3:6]]
    g7 = [item for row in board[:3] for item in row[6:9]]
    g8 = [item for row in board[3:6] for item in row[6:9]]
    g9 = [item for row in board[6:9] for item in row[6:9]]
    grids = [g1, g2, g3, g4, g5, g6, g7, g8, g9]
    def checkrow(n) :
        for row in n:
            fhand.write(f'###CHECKING ROW {row}###\n#########\n')
            for item in row :
                fhand.write(f'{item}:\n')
                fhand.write(f'Item in validnums: {item in validnums}\n')
                fhand.write(f'Item count in row == 1: {row.count(item)==1}\n')
        result = [True if row.count(item)==1 and item in validnums else False for item in row for row in n]
        fhand.write(f'Result of checking all items is: {result}\n')
        fhand.write(f'Result of all() statement is: {all(i for i in result)}\n')
        return all(i for i in result)
    def checkcol(n) :
        columns = [[row[i] for row in n] for i in range(9)]
        fhand.write(f'actual columns is {columns}\n\n\n\n')
        for column in columns:
            fhand.write(f'###CHECKING COLUMN {column}###\n#########\n')
            for item in column:
                fhand.write(f'item is {item}\n')
                fhand.write(f'Item in validnums: {item in validnums}\n')
                fhand.write(f'Item count in column == 1: {column.count(item)==1}\n')
        result = [True if column.count(item)==1 and item in validnums else False for item in column for column in [[row[i] for row in n] for i in range(9)]]
        fhand.write(f'Result of checking all items is: {result}\n')
        fhand.write(f'Result of all() statement is: {all(i for i in result)}\n')
        return all(i for i in result)
    def checkgrid(n) :
        for grid in grids:
            fhand.write(f'###CHECKING GRID {grid}###\n#######\n')
            for item in grid:
                fhand.write(f'item is {item}\n')
                fhand.write(f'item in validnums: {item in validnums}\n')
                fhand.write(f'item count in grid == 1: {grid.count(item)==1}\n')
        result = [True if grid.count(item)==1 and item in validnums else False for item in grid for grid in grids]
        fhand.write(f'Result of checking all items is: {result}\n')
        fhand.write(f'Result of all() statement is: {all(i for i in result)}\n')
        return all(i for i in result)
        #result = [True if column.count(item)==1 and item in validnums else False for item in column for column in [[row[i] for row in n] for i in range(9)]]
        #fhand.write(f'Result of checking all items is: {result}\n')
        #fhand.write(f'Result of all() statement is: {all(i for i in result)}\n')
        #return all(i for i in result)
    results = [checkrow(board), checkcol(board), checkgrid(board)]
    fhand.write(f'List of only checkrow return is: {results}\n')
    fhand.write(f'Result of final all() statement is: {all(i for i in results)}\n')
    return all(i for i in results)
print(str(valid_solution(input())))