def sum_of_sums(n):
    return sum([i+1 for i in range(sum([sum([i+1 for i in range(i+1)]) for i in range(n)]))])
print(sum_of_sums(int(input())))