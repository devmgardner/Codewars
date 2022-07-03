import itertools
def numeric_palindrome(*args):
    print(f'args are:')
    for arg in args:
        print(arg)
    product_list = []
    #finds out if input is a palindrome or not
    def is_palindrome(inp):
        if ''.join(list(str(inp))) == ''.join(reversed(list(str(inp)))):
            return True
        else:
            return False
    #finds the product of all items in input
    def find_product(inp):
        print(f'beginning find_product, inp is {inp}')
        count = 1
        for arg in inp:
            count *= arg
        print(f'count at end of find_product is {count}')
        return count
    #finds products of all permutations of input items
    print(f'range is {range(2,len(args)+1)}')
    for i in range(2,len(args)+1):
        print(f'current i is {i}')
        for item in itertools.permutations(args,i):
            print(f'current item is {item}')
            product_list.append(find_product(item))
    print(f'product_list at end is {product_list}')
    #slices input into all possible slices, finds out if slice is a palindrome, and appends to palindrome_list
    def find_slices(inp):
        print(f'inp at beginning of find_slices is {inp}')
        inp = list(str(inp))
        print(f'inp list is {inp}')
        slice_list = [inp[i:j] for i in range(len(inp)) for j in range(i+1,len(inp)+1)]
        print(f'slice_list is:')
        for i in slice_list:
            print(f'{i}')
        return slice_list
    palindrome_list = []
    for item in product_list:
        slice_list = find_slices(item)
        for item_slice in slice_list:
            if is_palindrome(''.join(item_slice)):
                palindrome_list.append(int(''.join(item_slice)))
    print('final palindrome_list is:')
    for i in palindrome_list:
        print(i)
    return max(palindrome_list)
    
    
    
    #your code here

print(numeric_palindrome(15,125,8))