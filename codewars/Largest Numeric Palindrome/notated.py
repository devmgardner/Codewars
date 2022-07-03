import itertools
def numeric_palindrome(*args):
    product_list = []
    # finds out if input is a palindrome or not
    # the input is an integer, so it first converts the integer to a string, then that string to a list,
    # then compares the ''.join string to its reversed ''.join string self
    def is_palindrome(inp):
        if ''.join(list(str(inp))) == ''.join(reversed(list(str(inp)))):
            return True
        else:
            return False
    # iterates through all input items and returns the total product
    def find_product(inp):
        count = 1
        for arg in inp:
            count *= arg
        return count
    # this gives us a number in the range "2" through "the length of the list of input items to the main function + 1"
    # this will be used to see how many of the input items we will be using
    for i in range(2,len(args)+1):
        # the line below iterates through all input items, choosing every possible permutation of i items
        for item in itertools.permutations(args,i):
            # for each possible permutation of i items, we find the total product of those items and append to the product_list
            product_list.append(find_product(item))
    palindrome_list = []
    # iterating through all products
    for item in product_list:
        # we take each product, turn it into a string, and find its length
        # then we go through the range "1" to "the length of the product + 1"
        for i in range(1,len(str(item))+1):
            # we are now iterating through every possible permutation of the digits of "item" with length "i"
            for perm in itertools.permutations(list(str(item)),i):
                # we now turn that list of digits into a string, and then into an integer
                # and pass that integer to the "is_palindrome" function
                # if it is a palindrome, we append it to the final palindrome_list
                if is_palindrome(int(''.join(perm))):
                    palindrome_list.append(int(''.join(perm)))
    #this is self-explanatory
    return max(palindrome_list)

print(numeric_palindrome(15,125,8))