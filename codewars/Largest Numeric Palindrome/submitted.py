import itertools
def numeric_palindrome(*args):
    def find_product(inp):
        count = 1
        for arg in inp:
            count *= arg
        return count
    palindrome_list = [int(''.join(perm)) for item in [find_product(item) for i in range(2,len(args)+1) for item in itertools.permutations(args,i)] for i in range(1,len(str(item))+1) for perm in itertools.permutations(list(str(item)),i) if ''.join(list(str(int(''.join(perm))))) == ''.join(reversed(list(str(int(''.join(perm))))))]
    return max(palindrome_list)

print(numeric_palindrome(7,23,87,32210))