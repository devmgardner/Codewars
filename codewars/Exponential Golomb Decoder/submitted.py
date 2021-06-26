#This code is incredibly messy and overcomplicated. It's just the way I do everything, and I'm trying to get better about it.
import re
def decoder(sequence):
    #I have a custom snippet in VSCode that sets up python test files for me, that includes creating a log file called (pythonfilename)-log.txt. This is so I can add write statements to every single operation to see if/when something goes wrong.
    dname = 'Exponential Golomb Decoder-log.txt'
    dhand = open(dname, 'w')
    dhand.close()
    dhand = open(dname, 'r+')
    output = []
    dhand.write(f'sequence is {sequence}\n')
    #The following line checks to see if any character other than '0' or '1' is present in the input sequence.
    if re.search('[^01]', sequence) : return ''
    while len(sequence) > 0 :
        #The following line matches zero or more '0's followed by exactly 1 '1'.
        zero = re.search('^(0*)1{1}', sequence).group(1)
        #The line below removes the match above from sequence, but only the first match.
        sequence = sequence.replace(zero, '', 1)
        lenzero = len(zero)
        dhand.write(f'match is {zero} with length of {lenzero}\n')
        dhand.write(f'removal of match results in {sequence}\n')
        #The line above and the lines below set the actual character value, and remove the character from the beginning of sequence.
        char = sequence[:lenzero + 1]
        dhand.write(f'actual number is {char}\n')
        sequence = sequence[lenzero + 1:]
        dhand.write(f'remaining sequence after removal of number is {sequence}\n')
        output.append(char)
    dhand.write(f'final list of matches is {output}\n')
    final = []
    #The simple loop below converts each actual character value into its decimal form, subtracts 1, and appends it to a list.
    for item in output :
        final.append(int(item, 2) - 1)
        dhand.write(f'conversion of number is {int(item, 2)}\n')
        dhand.write(f'number - 1 = {int(item, 2) - 1}\n')
    dhand.write(f'final decode is {final}\n')
    return final