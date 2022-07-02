def encode(s):
    def create_matrix(string):
        slist,length = list(string), len(string)
        matrix = []
        matrix.append(slist)
        #print(f'starting matrix is:')
        #print(matrix)
        def caesar_shift(inp):
            return inp[-1:] + inp[:-1]
        for i in range(length-1):
            slist = caesar_shift(slist)
            matrix.append(slist)
            #print(f'after iteration {i}, matrix is:')
            #for t in matrix:
            #    print(t)
        return matrix
    matrix = create_matrix(s)
    print(f'initial matrix is:')
    for i in matrix:
        print(i)
    matrix = sorted(matrix)
    print(f'sorted matrix is:')
    for i in matrix:
        print(i)
    final_column = ''.join([i[-1] for i in matrix])
    #print(f'final column is {final_column}')
    final_index = matrix.index(list(s))
    #print(f'final index is {final_index}')
    return (final_column,final_index)
print(encode('bananabar'))


def decode(s, n):
    matrix = []
    for i in range(len(s)):
        row = []
        for i in range(len(s)):
            row.append('0')
        matrix.append(row)
    for ind,char in enumerate(list(s)):
        matrix[ind][len(s)-1] = char
    for ind,char in enumerate(sorted(list(s))):
        matrix[ind][0] = char
    print(f'initial matrix during decode is:')
    for i in matrix:
        print(i)
    first_col = [row[0] for row in matrix]
    last_col = [row[-1] for row in matrix]
    zip_list = list(zip(last_col,first_col))
    for row in matrix:
        matrix[matrix.index(row)] = row[-1:] + row[:-1]
    #matrix[4] = list('bananabar')
    print(f'matrix after shifting characters is:')
    for i in matrix:
        print(i)

decode('nnbbraaaa',4)