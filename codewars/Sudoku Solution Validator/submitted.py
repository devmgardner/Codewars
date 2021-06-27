#I've left in all of my various testing lines and failed tries. Single comments are comments, triple comments are old lines.
#My custom snippet in VSCode auto-inserts the file lines below and generates a log filename for me based on my python filename.
fname = 'Sudoku Solution Validator-log.txt'
fhand = open(fname, 'w')
fhand.close()
fhand = open(fname, 'r+')
#Setting up a list of what is valid input for a sudoku board.
validnums = ['1','2','3','4','5','6','7','8','9']
def valid_solution(board):
    #
    #The line below was for when I was testing and wanted to be able to make my own input in my IDE.
    ###board = [list(row) for row in list(board.split())]
    #The line below is the input format I used when testing.
    #534678912 672195348 198342567 859761423 426853791 713924856 961537284 287419635 345286179
    fhand.write(f'input is {board}\n\n\n\n\n')
    ###board = [str(item) for row in board for item in row]
    ###fhand.write(f'input after str conversion is {board}\n')
    ###g1 = [row[:3] for row in board[:3]]
    ###g2 = [row[3:6] for row in board[:3]]
    ###g3 = [row[6:9] for row in board[:3]]
    ###g4 = [row[:3] for row in board[3:6]]
    ###g5 = [row[3:6] for row in board[3:6]]
    ###g6 = [row[6:9] for row in board[3:6]]
    ###g7 = [row[:3] for row in board[6:9]]
    ###g8 = [row[3:6] for row in board[6:9]]
    ###g9 = [row[6:9] for row in board[6:9]]
    #The lines below separate out each 3x3 grid in the board, from left to right and top to bottom.
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
                fhand.write(f'Item in validnums: {str(item) in validnums}\n')
                fhand.write(f'Item count in row == 1: {row.count(item)==1}\n')
        #The list comprehension below checks to ensure no number occurs more than once, and that all numbers in the row are valid, and iterates for each row in the input.
        result = [True if row.count(item)==1 and str(item) in validnums else False for item in row for row in n]
        fhand.write(f'Result of checking all items is: {result}\n')
        fhand.write(f'Result of all() statement is: {all(i for i in result)}\n')
        #This checks to ensure all 9 rows returned True.
        return all(i for i in result)
    def checkcol(n) :
        #This was one of the most annoying things to get working; I couldn't for the life of me get the output to be a list of lists of row[i]. I must have rewritten it a thousand times.
        columns = [[row[i] for row in n] for i in range(9)]
        fhand.write(f'actual columns is {columns}\n\n\n\n')
        for column in columns:
            fhand.write(f'###CHECKING COLUMN {column}###\n#########\n')
            for item in column:
                fhand.write(f'item is {item}\n')
                fhand.write(f'Item in validnums: {str(item) in validnums}\n')
                fhand.write(f'Item count in column == 1: {column.count(item)==1}\n')
        #This list comprehension is essentially the same as the row list, but slightly modified to iterate through each position in all 9 rows simultaneously.
        result = [True if column.count(item)==1 and str(item) in validnums else False for item in column for column in [[row[i] for row in n] for i in range(9)]]
        fhand.write(f'Result of checking all items is: {result}\n')
        fhand.write(f'Result of all() statement is: {all(i for i in result)}\n')
        return all(i for i in result)
    def checkgrid(n) :
        for grid in grids:
            fhand.write(f'###CHECKING GRID {grid}###\n#######\n')
            for item in grid:
                fhand.write(f'item is {item}\n')
                fhand.write(f'item in validnums: {str(item) in validnums}\n')
                fhand.write(f'item count in grid == 1: {grid.count(item)==1}\n')
        #Because the grids were set up, and added to a list, this list comprehension was incredibly easy to put together.
        result = [True if grid.count(item)==1 and str(item) in validnums else False for item in grid for grid in grids]
        fhand.write(f'Result of checking all items is: {result}\n')
        fhand.write(f'Result of all() statement is: {all(i for i in result)}\n')
        return all(i for i in result)
        ###result = [True if column.count(item)==1 and item in validnums else False for item in column for column in [[row[i] for row in n] for i in range(9)]]
        ###fhand.write(f'Result of checking all items is: {result}\n')
        ###fhand.write(f'Result of all() statement is: {all(i for i in result)}\n')
        ###return all(i for i in result)
    #This runs each function on the input successively, and appends the final True/False to a list.
    results = [checkrow(board), checkcol(board), checkgrid(board)]
    fhand.write(f'List of only checkrow return is: {results}\n')
    fhand.write(f'Result of final all() statement is: {all(i for i in results)}\n')
    #If all results are True, return True. If any result is False, return False.
    return all(i for i in results)
#The most I could possibly compact this code is as follows.
#def valid_solution(board):
#    grids=[[item for row in board[:3] for item in row[:3]], [item for row in board[3:6] for item in row[:3]], [item for row in board[6:9] for item in row[:3]], [item for row in board[:3] for item in row[3:6]], [item for row in board[3:6] for item in row[3:6]], [item for row in board[6:9] for item in row[3:6]], [item for row in board[:3] for item in row[6:9]], [item for row in board[3:6] for item in row[6:9]], [item for row in board[6:9] for item in row[6:9]]]
#    def checkrow(n):return all(i for i in [True if row.count(item)==1 and str(item) in ['1','2','3','4','5','6','7','8','9'] else False for row in n for item in row])
#    def checkcol(n):return all(i for i in [True if column.count(item)==1 and str(item) in ['1','2','3','4','5','6','7','8','9'] else False for column in [[row[i] for row in n] for i in range(9)] for item in column])
#    def checkgrid(n):return all(i for i in [True if grid.count(item)==1 and str(item) in ['1','2','3','4','5','6','7','8','9'] else False for grid in grids for item in grid])
#    return all(i for i in [checkrow(board), checkcol(board), checkgrid(board)])